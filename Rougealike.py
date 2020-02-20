import linecache
import os
import time
import urllib.request
import zipfile
from colorama import Fore, Back, Style, init
import keyboard
import random
import json
import threading
import pathlib
init(convert=True)
#chess pieces!

SystemInfo  = ["Build Version: 20/2/2020","1.0B2"]
LatestVer   = "ERROR"
Save = 0
Terrain = 0
#Below is Varaibles that are saved
PlayerInfo  = [0,0,random.randint(-2147483500,2147483500),random.randint(-2147483500,2147483500),50,25,5,1,0,500,"Hands",1,100,0,0,"Nothing",0,0,50,0,0,0,0] #0name,difficulty,x,y,hp,5atk,def,level,exp,gold,10EquipedWeaponName,EquipedWeaponAttack,EquipedWeaponHit,EquipedWeaponCritical,EquipedWeaponDurabilty,EquipedArmorName,EquippedArmourDefence,EquipedArmorDurabilty,Mana,Monolith Spell count,Last Village X Coord (20),Last Village Y Coord,Reputation
TerrainType = 0
TerrainTypeMeta = 0
Terrain  = 0
Resource = 0
ResourceAmmount = 0
Enemy   = [""]
Weather = 0
BattleLog = ["","","","","",""]
PlayerInventory = ["Pendant"]
PlayerInventoryAmmount = [1]
PlayerInventoryArmourDur = [0]
PlayerInventoryArmour    = ["Nothing"]
PlayerInventoryArmourDef = [0]
PlayerInventoryWeapon    = ["Hands"]
PlayerInventoryWeaponAtk = [0]
PlayerInventoryWeaponDur = [0]
PlayerInventoryWeaponCrt = [0]
PlayerInventoryWeaponHit = [100]
PlayerCurrentStats = [50,50] #HP,Mana
PlayerMagic      = ["Wait","Phonon","Panacea"]   # Name of magic
PlayerMagicType  = ["Damage","Damage","Heal"]   # HEAL - Vaule heals Damage - Damages the enemy
PlayerMagicValue = [1,25,40] # Damage of spell
PlayerMagicCost  = [0,5,5]   # How much does the spell cost to cast
DungeonData          = [0,0,0,0,0,0] # 0 - Size  1 - Direction      2-X     3-Y   4- Battle redirect flag 5 - boss multiplier
Log = []
FastTravelX = [0]
FastTravelY = [0]
PlayerQuestName       = [""]
PlayerQuestRewardType = [0]
PlayerQuestReqRes     = [""]
PlayerQuestReqAmm     = [0]
PlayerAchivements     = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
#WorldData Variables SHOULD NOT be modifyed instead unless its for a master branch (USE THE MOD API)
WorldDataTerrain            = ["in the grasslands","in the flatlands","in the mountains","in a town","in an abandoned town","near a volcano","on some hills","in a abandoned mine","in a valley","in a lake","in a beach","in a cave","in a taiga forest","in a swamp","in a forest","in a thick forest","on a hillside","on a cliffside","on some farmland","in a mesa","in the middle of a Desert","in a Oasis","inside of an abandoned cabin","on a Plateou","in snowy mountain","near a riverside"]
WorldDataMapIcon            = ["G","F","M","T","A","V","H","A","V","L","B","C","F","S","F","F","H","C","F","M","D","O","A","P","M","R"]
WorldDataTerrainColor       = ["GREEN","RESET","WHITE","RESET","RESET","RED","GREEN","WHITE","CYAN","BLUE","YELLOW","RESET","WHITE","GREEN","GREEN","GREEN","RESET","CYAN","YELLOW","YELLOW","YELLOW","BLUE","RESET","WHITE","WHITE","CYAN"]
WorldDataTerrainBrightness  = ["BRIGHT","NORMAL","BRIGHT","NORMAL","DIM","DIM","BRIGHT","DIM","BRIGHT","BRIGHT","NORMAL","DIM","BRIGHT","DIM","BRIGHT","DIM","DIM","DIM","BRIGHT","DIM","BRIGHT","DIM","DIM","BRIGHT","BRIGHT","DIM"]
WorldDataProffessionData    = [0,0,0,0,0,0,0,0,1,1,1,0,2,0,2,2,0,0,0,0,0,1,0,0,0,1]
WorldDataResource           = ["Apples","Bark","Berries","Blue Lilly Pads","Branches","Bundles of grass","Bundles of leaves","Bundles of wheat","Bushes","Cacti","Carrots","Dark wood logs","Emeralds","Fish","Flowers","Grass Fibers","Herbs","KG of Black Sand","KG of Sand","Lilly Pads","Litres of water","Magma Branches","Magma Logs","Magma stones","Moss","Mystical berries","Oak wood logs","Palm tree logs","Palm wood","Pink Lilly Pads","Potatoes","Redwood Branches","Redwood Logs","Seeds","Spruce Branches","Spruce logs"]
WorldDataResourceColor      = ["RED","WHITE","RED","BLUE","GREEN","GREEN","GREEN","YELLOW","WHITE","GREEN","YELLOW","WHITE","GREEN","CYAN","MAGENTA","GREEN","GREEN","WHITE","YELLOW","GREEN","BLUE","RED","RED","RED","GREEN","CYAN","RESET","YELLOW","YELLOW","MAGENTA","YELLOW","RED","RED","GREEN","CYAN","CYAN"]
WorldDataResourceBrightness = ["BRIGHT","DIM","BRIGHT","BRIGHT","DIM","DIM","BRIGHT","DIM","DIM","DIM","BRIGHT","DIM","BRIGHT","BRIGHT","BRIGHT","DIM","BRIGHT","DIM","DIM","DIM","BRIGHT","DIM","DIM","DIM","DIM","BRIGHT","BRIGHT","BRIGHT","BRIGHT","BRIGHT","DIM","DIM","NORMAL","NORMAL","DIM","DIM"]
WorldDataEnemyPrefix        = ["Angry","Armoured","Beserk","Crazed","Demonic","Enemy","Enraged","Fallen","Frenzied","Giant","Greater","Infested","Leaping","Lesser","Possessed","Skeleton"]
WorldDataEnemyName          = ["Archer","Artifact","Beast","Bull","Centaur","Demon","Dog","Elf","Fire","Fox","Giant","Goblin","God","Hunter","Ice","Madman","Ogre","Orc","Phantom","Rat","Relic","Robot","Skeleton","Soldier","Spider","Spirit","Troll","Villager","Warrior","Wolf","Zombie"]
WorldDataEnemySuffix        = ["Lord","Monster","King","Creature"]
WorldDataEnemyDrop          = ["Arrows","Odd artifact","Meat","Meat","Meat","Fire Dust","Meat","Fabric","Fire Dust","Meat","Meat","Gold Bar","Legendary Gem","Meat","Ice Dust","Faberic","Meat","Meat","Meat","Meat","Old Relic","Scrap Metal","Bone Dust","Scrap Metal","Meat","Spirit Dust","Meat","Meat","Old Spear","Meat","Old Flesh"]
WorldDataWeather            = ["","Sunny","Cloudy","Hot","Cold","Windy"]
WorldDataCaveGem            = ["Uncut Rubies","Uncut Emeralds","Uncut Saphires","Uncut Topaz","Uncut Diamonds","Uncut Opal"]
WorldDataMonolithSpell      = ["Heal I","Bolt","Risma","Aquious","Ignis","Terra","Heal II","Rarisma","Taifau","Odurzony","hladan","Tembung","Heal III"]#These are just words in other langauges
WorldDataMonolithSpellType  = ["HEAL","Damage","Damage","Damage","Damage","Damage","HEAL", "Damage","Damage", "Damage", "Damage","Damage",  "HEAL"]
WorldDataMonolithSpellValue = [80,20,25,25,35,30,30,110,60,50,80,100,100,200]
WorldDataMonolithSpellCost  = [5,15,25,20,40,20,10,75,40,10,75,90,60,100]
WorldDataCaveMetal          = ["Iron Ore","Coal","Copper Ore","Potassium Ore","Magnesium Ore","Steel","Urainium Ore","Malachite Ore","Stone","Clay","Silicon","Boron Ore","Carbon","Dawnite Ore","Uncut OpalQuartz Ore","Rolton Ore","Vibrainum Ore","Yosmite Ore","Yunotium Ore","Gallium Ore","Jabraca Ore","Platnum Ore","Cronite Ore","Adamite Ore","Ironite Ore"]

WorldDataCraftMetalReq      = ["","Iron Ore","Copper Ore","Potassium Ore","Magnesium Ore","Urainium Ore","Malachite Ore","Boron Ore","Dawnite Ore","Quartz Ore","Rolton Ore","Vibrainum Ore","Yosmite Ore","Yunotium Ore","Gallium Ore","Jabraca Ore","Platnum Ore","Cronite Ore","Adamite Ore","Ironite Ore"]
WorldDataCraftMetalProd     = ["","Iron Bar","Copper Bar","Potassium Bar","Magnesium Bar","Urainium Bar","Malachite Bar","Boron Bar","Dawnite Bar","Quartz Bar","Rolton Bar","Vibrainum Bar","Yosmite Bar","Yunotium Bar","Gallium Bar","Jabraca Bar","Platnum Bar","Cronite Bar","Adamite Bar","Ironite Bar"]
WorldDataCraftMetalAmm      = ["",3,3,3,3,5,5,2,10,1,5,3,5,5,5,5,5,3,10,5]

WorldDataCraftGemReq        = ["Uncut Rubies","Uncut Emeralds","Uncut Saphires","Uncut Topaz","Uncut Diamonds","Uncut Opal"]
WorldDataCraftGemProd       = ["Topaz","Saphires","Rubies","Emeralds","Diamonds","Opal"]
WorldDataCraftGemAmm        = [1,1,1,1,1,1,1]

WorldDataCraftWeaponAxeReq  = ["Copper Bar","Iron Bar","Magnesium Bar","Boron Bar","Gallium Bar","Rolton Bar","Yosmite Bar","Yunotium Bar","Jabraca Bar","Ironite Bar","Platnum Bar","Cronite Bar","Adamite Bar","Dawnite Bar","Malachite Bar"]
WorldDataCraftWeaponAxeProd = ["Copper Axe","Iron Axe","Magnesium Axe","Boron Axe","Gallium Axe","Rolton Axe","Yosmite Axe","Yunotium Axe","Jabraca Axe","Ironite Axe","Platnum Axe","Cronite Axe","Adamite Axe","Dawnite Axe","Malachite Axe"]
WorldDataCraftWeaponAxeAmm  = [2,6,10,16,19,23,27,35,42,47,52,57,63,69,76]

WorldDataCraftWeaponLbowProd = ["Copper Longbow","Iron Longbow","Magnesium Longbow","Boron Longbow","Gallium Longbow","Rolton Longbow","Yosmite Longbow","Yunotium Longbow","Jabraca Longbow","Ironite Longbow","Platnum Longbow","Cronite Longbow","Adamite Longbow","Dawnite Longbow","Malachite Longbow"]
WorldDataCraftWeaponLbowReq  = ["Copper Bar","Iron Bar","Magnesium Bar","Boron Bar","Gallium Bar","Rolton Bar","Yosmite Bar","Yunotium Bar","Jabraca Bar","Ironite Bar","Platnum Bar","Cronite Bar","Adamite Bar","Dawnite Bar","Malachite Bar"]
WorldDataCraftWeaponLbowAmm  = [12,16,20,36,49,53,57,65,72,77,82,87,93,96,98]

WorldDataCraftWeaponLanProd = ["Copper Lance","Iron Lance","Magnesium Lance","Boron Lance","Gallium Lance","Rolton Lance","Yosmite Lance","Yunotium Lance","Jabraca Lance","Ironite Lance","Platnum Lance","Cronite Lance","Adamite Lance","Dawnite Lance","Malachite Lance"]
WorldDataCraftWeaponLanReq  = ["Copper Bar","Iron Bar","Magnesium Bar","Boron Bar","Gallium Bar","Rolton Bar","Yosmite Bar","Yunotium Bar","Jabraca Bar","Ironite Bar","Platnum Bar","Cronite Bar","Adamite Bar","Dawnite Bar","Malachite Bar"]
WorldDataCraftWeaponLanAmm  = [2,6,10,16,19,23,27,35,42,47,52,57,63,69,76]

WorldDataCraftWeaponMacProd = ["Copper Mace","Iron Mace","Magnesium Mace","Boron Mace","Gallium Mace","Rolton Mace","Yosmite Mace","Yunotium Mace","Jabraca Mace","Ironite Mace","Platnum Mace","Cronite Mace","Adamite Mace","Dawnite Mace","Malachite Mace"]
WorldDataCraftWeaponMacReq  = ["Copper Bar","Iron Bar","Magnesium Bar","Boron Bar","Gallium Bar","Rolton Bar","Yosmite Bar","Yunotium Bar","Jabraca Bar","Ironite Bar","Platnum Bar","Cronite Bar","Adamite Bar","Dawnite Bar","Malachite Bar"]
WorldDataCraftWeaponMacAmm  = [2,6,10,16,19,23,27,35,42,47,52,57,63,69,76]

WorldDataCraftWeaponGSwoProd = ["Copper GreatSword","Iron GreatSword","Magnesium GreatSword","Boron GreatSword","Gallium GreatSword","Rolton GreatSword","Yosmite GreatSword","Yunotium GreatSword","Jabraca GreatSword","Ironite GreatSword","Platnum GreatSword","Cronite GreatSword","Adamite GreatSword","Dawnite GreatSword","Malachite GreatSword"]
WorldDataCraftWeaponGSwoReq  = ["Copper Bar","Iron Bar","Magnesium Bar","Boron Bar","Gallium Bar","Rolton Bar","Yosmite Bar","Yunotium Bar","Jabraca Bar","Ironite Bar","Platnum Bar","Cronite Bar","Adamite Bar","Dawnite Bar","Malachite Bar"]
WorldDataCraftWeaponGSwoAmm  = [12,16,20,26,29,33,37,45,52,57,62,67,76,79]

WorldDataCraftWeaponSSwoProd = ["Copper Shortsword","Iron Shortsword","Magnesium Shortsword","Boron Shortsword","Gallium Shortsword","Rolton Shortsword","Yosmite Shortsword","Yunotium Shortsword","Jabraca Shortsword","Ironite Shortsword","Platnum Shortsword","Cronite Shortsword","Adamite Shortsword","Dawnite Shortsword","Malachite Shortsword"]
WorldDataCraftWeaponSSwoReq  = ["Copper Bar","Iron Bar","Magnesium Bar","Boron Bar","Gallium Bar","Rolton Bar","Yosmite Bar","Yunotium Bar","Jabraca Bar","Ironite Bar","Platnum Bar","Cronite Bar","Adamite Bar","Dawnite Bar","Malachite Bar"]
WorldDataCraftWeaponSSwoAmm  = [3,5,8,9,12,15,23,26,28,29,35,48,56,64,72]

WorldDataCraftWeaponShuProd = ["Copper Shuriken","Iron Shuriken","Magnesium Shuriken","Boron Shuriken","Gallium Shuriken","Rolton Shuriken","Yosmite Shuriken","Yunotium Shuriken","Jabraca Shuriken","Ironite Shuriken","Platnum Shuriken","Cronite Shuriken","Adamite Shuriken","Dawnite Shuriken","Malachite Shuriken"]
WorldDataCraftWeaponShuReq  = ["Copper Bar","Iron Bar","Magnesium Bar","Boron Bar","Gallium Bar","Rolton Bar","Yosmite Bar","Yunotium Bar","Jabraca Bar","Ironite Bar","Platnum Bar","Cronite Bar","Adamite Bar","Dawnite Bar","Malachite Bar",]
WorldDataCraftWeaponShuAmm  = [1,3,5,8,12,14,17,18,21,24,26,29,32,35,38]

WorldDataCraftWeaponSbowProd = ["Copper Shortbow","Iron Shortbow","Magnesium Shortbow","Boron Shortbow","Gallium Shortbow","Rolton Shortbow","Yosmite Shortbow","Yunotium Shortbow","Jabraca Shortbow","Ironite Shortbow","Platnum Shortbow","Cronite Shortbow"]
WorldDataCraftWeaponSbowAmm  = [2,6,10,26,39,43,47,55,62,67,72,77,83,86,88]
WorldDataCraftWeaponSbowReq  = ["Copper Bar","Iron Bar","Magnesium Bar","Boron Bar","Gallium Bar","Rolton Bar","Yosmite Bar","Yunotium Bar","Jabraca Bar","Ironite Bar","Platnum Bar","Cronite Bar","Adamite Bar","Dawnite Bar","Malachite Bar",]

WorldDataCraftWeaponCbowProd = ["Copper Crossbow","Iron Crossbow","Magnesium Crossbow","Boron Crossbow","Gallium Crossbow","Rolton Crossbow","Yosmite Crossbow","Yunotium Crossbow","Jabraca Crossbow","Ironite Crossbow","Platnum Crossbow","Cronite Crossbow","Adamite Crossbow","Dawnite Crossbow","Malachite Crossbow"]
WorldDataCraftWeaponCbowReq  = ["Copper Bar","Iron Bar","Magnesium Bar","Boron Bar","Gallium Bar","Rolton Bar","Yosmite Bar","Yunotium Bar","Jabraca Bar","Ironite Bar","Platnum Bar","Cronite Bar","Adamite Bar","Dawnite Bar","Malachite Bar"]
WorldDataCraftWeaponCbowAmm  = [22,36,40,56,69,73,77,85,72,77,82,87,93,96,108]

WorldDataCraftArmorProd     = ["","Iron Armour","Quartz Armour","Rolton Armour","Jabraca Armour","Platnum Armour","Adamite Armour","Malachite Armour","Dawnite Armour"]
WorldDataCraftArmorReq      = ["","Iron Bar","Quartz Bar","Rolton Bar","Jabraca Bar","Platnum Bar","Adamite Bar","Malachite Bar","Dawnite Bar"]
WorldDataCraftArmorAmm      = ["",25,32,35,40,48,55,59,66,70,78]

WorldDataTradeProd          = ["Topaz","Saphires","Rubies","Emeralds","Diamonds","Opal","Iron Bar","Copper Bar","Potassium Bar","Magnesium Bar","Urainium Bar","Malachite Bar","Boron Bar","Dawnite Bar","Quartz Bar","Rolton Bar","Vibrainum Bar","Yosmite Bar","Yunotium Bar","Gallium Bar","Jabraca Bar","Platnum Bar","Cronite Bar","Adamite Bar","Ironite Bar","Apples","Bark","Berries","Blue Lilly Pads","Branches","Bundles of grass","Bundles of leaves","Bundles of wheat","Bushes","Cacti","Carrots","Dark wood logs","Emeralds","Fish","Flowers","Grass Fibers","Herbs","KG of Black Sand","KG of Sand","Lilly Pads","Litres of water","Magma Branches","Magma Logs","Magma stones","Moss","Mystical berries","Oak wood logs","Palm tree logs","Palm wood","Pink Lilly Pads","Potatoes","Redwood Branches","Redwood Logs","Seeds","Spruce Branches","Arrows","Bone Dust","Fabric","Fire Dust","Ice Dust","Meat","Odd artifact","Old Flesh","Old Relic","Old Spear","Scrap Metal","Spirit Dust"]
WorldDataTradePrice         = [50,70,80,100,150,250,500,250,50,245,750,5000,9500,4500,10000,100,100,500,100,3000,1000,1675,1500,750,2500,1000,10,5,25,35,5,5,5,50,10,65,15,75,250,150,15,20,100,1000,500,250,100,500,750,100,5,250,1000,100,100,2500,100,150,250,50,100,150,30,150,250,1000,1000,250,1500,2000,2000,250,100,1000]

WorldDataLegendsForgeProd   = ["Crossbow of the god","Shortbow of the godless","Shuriken of the advocate","Shortsword of the void","GreatSword of the evangelical","Mace of malice","Achient Lance of the long forgoten","Longbow of far-sighted","Axe of the last"]
WorldDataLegendsForgeAmm    = [50,20,10,25,40,50,50,50,50]
def Intialise():    #Starts the game, Checks reqired modules are installed and runs AutoUpdate if enabled
    global SystemInfo
    global LatestVer
    global Log
    Log.append("Initalising game")

    try:
        Log.append("Attempting to make files")
        if os.path.exists(os.path.dirname(os.path.abspath(__file__)) + "\\WorldData"): 
            time.sleep(0)
        else:
            os.mkdir(os.path.dirname(os.path.abspath(__file__)) + "\\WorldData")

        if os.path.exists(os.path.dirname(os.path.abspath(__file__)) + "\\PlayerData"): 
            time.sleep(0)
        else:
            os.mkdir(os.path.dirname(os.path.abspath(__file__)) + "\\PlayerData")

        if os.path.exists(os.path.dirname(os.path.abspath(__file__)) + "\\PlayerData\\Slot1"): 
            time.sleep(0)
        else:
            os.mkdir(os.path.dirname(os.path.abspath(__file__)) + "\\PlayerData\\Slot1")

        if os.path.exists(os.path.dirname(os.path.abspath(__file__)) + "\\PlayerData\\Slot2"): 
            time.sleep(0)
        else:
            os.mkdir(os.path.dirname(os.path.abspath(__file__)) + "\\PlayerData\\Slot2")

        if os.path.exists(os.path.dirname(os.path.abspath(__file__)) + "\\PlayerData\\Slot3"): 
            time.sleep(0)
        else:
            os.mkdir(os.path.dirname(os.path.abspath(__file__)) + "\\PlayerData\\Slot3")

        if os.path.exists(os.path.dirname(os.path.abspath(__file__)) + "\\PlayerData\\Slot4"): 
            time.sleep(0)
        else:
            os.mkdir(os.path.dirname(os.path.abspath(__file__)) + "\\PlayerData\\Slot4")

        if os.path.exists(os.path.dirname(os.path.abspath(__file__)) + "\\PlayerData\\Slot15"): 
            time.sleep(0)
        else:
            os.mkdir(os.path.dirname(os.path.abspath(__file__)) + "\\PlayerData\\Slot5")
    except: #Fails if lack of perms or already there
        Log.append("Failed to make files (Probably already exist)")


    Log.append("Checking modules.")
    try:    
        #Checks if modules are installed
        import keyboard
        import colorama
        Log.append("Check passed")
    except: #Tries to Auto-Install modules
        Log.append("Check Failed.")
        print("You are missing required modules,\nWould you like to attempt to Auto-Install them?\n\nThis may fail if you are not an admin.\n(Y/N)")
        Select = input()
        Loop = 1
        while Loop == 1:
            if str(Select.upper()) == "Y":
                Log.append("Atempting to AutoInstall the modules")
                os.system("pip install colorama keyboard")
                Loop = 0
            elif str(Select.upper()) == "N":
                Log.append("User decided to quit")
                input("Very well then,\nPress enter to close the program")
                exit()  #Terminates if declines to install
        try:
            import keyboard
            import colorama 
        except:
            input("Failed to Auto-Install required modules...\nPlease open a Command Prompt (Preferably as admin) and type the following command\npip install colorama keyboard\n\nPress enter to leave.")
            exit()

    Log.append("Attempting to AutoUpdate.")
    print("Trying to check update servers...\n\nTired of seeing this?\nChange the autoupdater setting in Config.txt\nThis shouldn't take more than 30 seconds")
    TempStr = linecache.getline(os.path.dirname(os.path.abspath(__file__)) + "\\Config.txt",3)
    TempStr = TempStr.strip()
    if TempStr == "False":  #Checks if AutoUpdate is disabled if so then it goes to the menu
        LatestVer = "DISABLED"
        ModLoader()

    try:    #Tries to get check github
        urllib.request.urlretrieve("https://raw.githubusercontent.com/TMAltair/RougalikeRPG/master/metadata.txt",os.path.dirname(os.path.abspath(__file__)) + "\\meta.txt")
        LatestVer = str(linecache.getline(os.path.dirname(os.path.abspath(__file__)) + "\\meta.txt",3))
    except: #Upon any type of failure it skips AutoUpdate
        LatestVer = "Failed"
        ModLoader()
    LatestVer = LatestVer.strip()
    
    try:#Checks AutoUpdate
        testvar = LatestVer = int(linecache.getline(os.path.dirname(os.path.abspath(__file__)) + "\\meta.txt",7))
        if testvar == 1: 
            LatestVer = "GLOBALLY DISABLED"
            ModLoader()
    except:
        print()

    try: 
        os.remove(os.path.dirname(os.path.abspath(__file__)) + "\\Data\\meta.txt") # Tries to delete meta.txt if it exists
    except:
        time.sleep(0) 
    
    os.system("cls")
    if LatestVer != SystemInfo[1] and not LatestVer == "Failed": #Autoupdater code
        print("You are on version " + str(SystemInfo[1]) + "\nVersion " + str(LatestVer) + " is available\n\nUpdate? (Y/N)")
        Loop = 1
        while Loop == 1:
            if keyboard.is_pressed("y"):
                print("Starting update!\nThis shouldn't take more than 2 minutes")
                try:
                    os.mkdir("Rougalike " + LatestVer)
                except:
                    time.sleep(0)
                urllib.request.urlretrieve("https://raw.githubusercontent.com/TMAltair/RougalikeRPG/master/Rougealike.py",os.path.dirname(os.path.abspath(__file__)) + "\\Rougalike " + LatestVer +"\\Rougalike " + LatestVer + ".py")
                urllib.request.urlretrieve("https://raw.githubusercontent.com/TMAltair/RougalikeRPG/master/Data.zip",os.path.dirname(os.path.abspath(__file__)) + "\\Rougalike " + LatestVer +"\\Data.zip")
                with zipfile.ZipFile(os.path.dirname(os.path.abspath(__file__)) + "\\Rougalike " + LatestVer + "\\Data.zip", 'r') as zip_ref:
                    zip_ref.extractall(os.path.dirname(os.path.abspath(__file__)) + "\\Rougalike " + LatestVer)
                os.remove(os.path.dirname(os.path.abspath(__file__)) + "\\Rougalike " + LatestVer + "\\Data.zip")
                input("\n" + Fore.GREEN + "Update Complete!" + Fore.RESET + "\nTo run the latest version look for the folder called Rougalike " + LatestVer + "\n\nPress enter to close.\n")
                exit()
            elif keyboard.is_pressed("n"):
                LatestVer = "Declined"
                ModLoader()
    LatestVer = "Up to date"
    ModLoader()

def ModLoader():
    global WorldDataTerrain
    print("Initalising Mod loader")
    if os.path.exists(os.path.dirname(os.path.abspath(__file__)) + "\\Mods\\achivement.txt"):
        PlayerAchivements[0] = 1
        
    if os.path.exists(os.path.dirname(os.path.abspath(__file__)) + "\\Mods\\WorldDataTerrain.json"):
        destination = os.path.dirname(os.path.abspath(__file__)) + "\\Mods\\WorldDataTerrain.json"
        with open(destination) as file:
            TempString = json.load(file)
            WorldDataTerrain = WorldDataTerrain + TempString

    if os.path.exists(os.path.dirname(os.path.abspath(__file__)) + "\\Mods\\WorldDataMapIcon.json"):
        destination = os.path.dirname(os.path.abspath(__file__)) + "\\Mods\\WorldDataMapIcon.json"
        with open(destination) as file:
            TempString = json.load(file)
            WorldDataMapIcon  = WorldDataMapIcon  + TempString

    if os.path.exists(os.path.dirname(os.path.abspath(__file__)) + "\\Mods\\WorldDataTerrainColor.json"):
        destination = os.path.dirname(os.path.abspath(__file__)) + "\\Mods\\WorldDataTerrainColor.json"
        with open(destination) as file:
            TempString = json.load(file)
            WorldDataTerrainColor   = WorldDataTerrainColor   + TempString

    if os.path.exists(os.path.dirname(os.path.abspath(__file__)) + "\\Mods\\WorldDataTerrainBrightness.json"):
        destination = os.path.dirname(os.path.abspath(__file__)) + "\\Mods\\WorldDataTerrainBrightness.json"
        with open(destination) as file:
            TempString = json.load(file)
            WorldDataTerrainBrightness  = WorldDataTerrainBrightness + TempString

    if os.path.exists(os.path.dirname(os.path.abspath(__file__)) + "\\Mods\\WorldDataProffessionData.json"):
        destination = os.path.dirname(os.path.abspath(__file__)) + "\\Mods\\WorldDataProffessionData.json"
        with open(destination) as file:
            TempString = json.load(file)
            WorldDataProffessionData = WorldDataProffessionData + TempString

    if os.path.exists(os.path.dirname(os.path.abspath(__file__)) + "\\Mods\\WorldDataResource.json"):
        destination = os.path.dirname(os.path.abspath(__file__)) + "\\Mods\\WorldDataResource.json"
        with open(destination) as file:
            TempString = json.load(file)
            WorldDataResource = WorldDataResource  + TempString


    if os.path.exists(os.path.dirname(os.path.abspath(__file__)) + "\\Mods\\WorldDataResourceColor .json"):
        destination = os.path.dirname(os.path.abspath(__file__)) + "\\Mods\\WorldDataResourceColor .json"
        with open(destination) as file:
            TempString = json.load(file)
            WorldDataResourceColor  = WorldDataResourceColor   + TempString


    if os.path.exists(os.path.dirname(os.path.abspath(__file__)) + "\\Mods\\WorldDataResourceBrightness.json"):
        destination = os.path.dirname(os.path.abspath(__file__)) + "\\Mods\\WorldDataResourceBrightness.json"
        with open(destination) as file:
            TempString = json.load(file)
            WorldDataResourceBrightness = WorldDataResourceBrightness + TempString

    if os.path.exists(os.path.dirname(os.path.abspath(__file__)) + "\\Mods\\WorldDataEnemyPrefix.json"):
        destination = os.path.dirname(os.path.abspath(__file__)) + "\\Mods\\WorldDataEnemyPrefix.json"
        with open(destination) as file:
            TempString = json.load(file)
            WorldDataEnemyPrefix = WorldDataEnemyPrefix + TempString

    if os.path.exists(os.path.dirname(os.path.abspath(__file__)) + "\\Mods\\WorldDataEnemyName.json"):
        destination = os.path.dirname(os.path.abspath(__file__)) + "\\Mods\\WorldDataEnemyName.json"
        with open(destination) as file:
            TempString = json.load(file)
            WorldDataEnemyName = WorldDataEnemyName  + TempString

    if os.path.exists(os.path.dirname(os.path.abspath(__file__)) + "\\Mods\\WorldDataEnemySuffix .json"):
        destination = os.path.dirname(os.path.abspath(__file__)) + "\\Mods\\WorldDataEnemySuffix .json"
        with open(destination) as file:
            TempString = json.load(file)
            WorldDataEnemySuffix = WorldDataEnemySuffix + TempString

    if os.path.exists(os.path.dirname(os.path.abspath(__file__)) + "\\Mods\\WorldDataEnemyDrop.json"):
        destination = os.path.dirname(os.path.abspath(__file__)) + "\\Mods\\WorldDataEnemyDrop.json"
        with open(destination) as file:
            TempString = json.load(file)
            WorldDataEnemyDrop = WorldDataEnemyDrop  + TempString

    if os.path.exists(os.path.dirname(os.path.abspath(__file__)) + "\\Mods\\WorldDataCaveGem.json"):
        destination = os.path.dirname(os.path.abspath(__file__)) + "\\Mods\\WorldDataCaveGem.json"
        with open(destination) as file:
            TempString = json.load(file)
            WorldDataCaveGem = WorldDataCaveGem   + TempString

    if os.path.exists(os.path.dirname(os.path.abspath(__file__)) + "\\Mods\\WorldDataMonolithSpell.json"):
        destination = os.path.dirname(os.path.abspath(__file__)) + "\\Mods\\WorldDataMonolithSpell.json"
        with open(destination) as file:
            TempString = json.load(file)
            WorldDataMonolithSpell = WorldDataMonolithSpell + TempString

    if os.path.exists(os.path.dirname(os.path.abspath(__file__)) + "\\Mods\\WorldDataMonolithSpellType.json"):
        destination = os.path.dirname(os.path.abspath(__file__)) + "\\Mods\\WorldDataMonolithSpellType.json"
        with open(destination) as file:
            TempString = json.load(file)
            WorldDataMonolithSpellType = WorldDataMonolithSpellType  + TempString

    if os.path.exists(os.path.dirname(os.path.abspath(__file__)) + "\\Mods\\WorldDataMonolithSpellValue.json"):
        destination = os.path.dirname(os.path.abspath(__file__)) + "\\Mods\\WorldDataMonolithSpellValue.json"
        with open(destination) as file:
            TempString = json.load(file)
            WorldDataMonolithSpellValue = WorldDataMonolithSpellValue + TempString

    if os.path.exists(os.path.dirname(os.path.abspath(__file__)) + "\\Mods\\WorldDataMonolithSpellCost.json"):
        destination = os.path.dirname(os.path.abspath(__file__)) + "\\Mods\\WorldDataMonolithSpellCost.json"
        with open(destination) as file:
            TempString = json.load(file)
            WorldDataMonolithSpellCost = WorldDataMonolithSpellCost + TempString

    if os.path.exists(os.path.dirname(os.path.abspath(__file__)) + "\\Mods\\WorldDataCaveMetal.json"):
        destination = os.path.dirname(os.path.abspath(__file__)) + "\\Mods\\WorldDataCaveMetal.json"
        with open(destination) as file:
            TempString = json.load(file)
            WorldDataCaveMetal = WorldDataCaveMetal  + TempString

    if os.path.exists(os.path.dirname(os.path.abspath(__file__)) + "\\Mods\\WorldDataCraftMetalReq.json"):
        destination = os.path.dirname(os.path.abspath(__file__)) + "\\Mods\\WorldDataCraftMetalReq.json"
        with open(destination) as file:
            TempString = json.load(file)
            WorldDataCraftMetalReq = WorldDataCraftMetalReq + TempString

    if os.path.exists(os.path.dirname(os.path.abspath(__file__)) + "\\Mods\\WorldDataCraftMetalAmm.json"):
        destination = os.path.dirname(os.path.abspath(__file__)) + "\\Mods\\WorldDataCraftMetalAmm.json"
        with open(destination) as file:
            TempString = json.load(file)
            WorldDataCraftMetalAmm  = WorldDataCraftMetalAmm  + TempString

    if os.path.exists(os.path.dirname(os.path.abspath(__file__)) + "\\Mods\\WorldDataCraftMetalProd.json"):
        destination = os.path.dirname(os.path.abspath(__file__)) + "\\Mods\\WorldDataCraftMetalProd.json"
        with open(destination) as file:
            TempString = json.load(file)
            WorldDataCraftMetalAmm  = WorldDataCraftMetalProd   + TempString

    if os.path.exists(os.path.dirname(os.path.abspath(__file__)) + "\\Mods\\WorldDataCraftGemReq.json"):
        destination = os.path.dirname(os.path.abspath(__file__)) + "\\Mods\\WorldDataCraftGemReq.json"
        with open(destination) as file:
            TempString = json.load(file)
            WorldDataCraftGemReq = WorldDataCraftGemReq + TempString


    if os.path.exists(os.path.dirname(os.path.abspath(__file__)) + "\\Mods\\WorldDataCraftGemAmm.json"):
        destination = os.path.dirname(os.path.abspath(__file__)) + "\\Mods\\WorldDataCraftGemAmm.json"
        with open(destination) as file:
            TempString = json.load(file)
            WorldDataCraftGemAmm = WorldDataCraftGemAmm + TempString

    if os.path.exists(os.path.dirname(os.path.abspath(__file__)) + "\\Mods\\WorldDataCraftGemProd .json"):
        destination = os.path.dirname(os.path.abspath(__file__)) + "\\Mods\\WorldDataCraftGemProd.json"
        with open(destination) as file:
            TempString = json.load(file)
            WorldDataCraftGemProd = WorldDataCraftGemProd + TempString

    if os.path.exists(os.path.dirname(os.path.abspath(__file__)) + "\\Mods\\WorldDataCraftWeaponAxeReq.json"):
        destination = os.path.dirname(os.path.abspath(__file__)) + "\\Mods\\WorldDataCraftWeaponAxeReq.json"
        with open(destination) as file:
            TempString = json.load(file)
            WorldDataCraftWeaponAxeReq  = WorldDataCraftWeaponAxeReq  + TempString


    if os.path.exists(os.path.dirname(os.path.abspath(__file__)) + "\\Mods\\WorldDataCraftWeaponAxeAmm.json"):
        destination = os.path.dirname(os.path.abspath(__file__)) + "\\Mods\\WorldDataCraftWeaponAxeAmm.json"
        with open(destination) as file:
            TempString = json.load(file)
            WorldDataCraftWeaponAxeAmm   = WorldDataCraftWeaponAxeAmm   + TempString

    if os.path.exists(os.path.dirname(os.path.abspath(__file__)) + "\\Mods\\WorldDataCraftWeaponAxeProd.json"):
        destination = os.path.dirname(os.path.abspath(__file__)) + "\\Mods\\WorldDataCraftWeaponAxeProd.json"
        with open(destination) as file:
            TempString = json.load(file)
            WorldDataCraftWeaponAxeProd = WorldDataCraftWeaponAxeProd + TempString

    if os.path.exists(os.path.dirname(os.path.abspath(__file__)) + "\\Mods\\WorldDataCraftWeaponLbowProd.json"):
        destination = os.path.dirname(os.path.abspath(__file__)) + "\\Mods\\WorldDataCraftWeaponLbowProd.json"
        with open(destination) as file:
            TempString = json.load(file)
            WorldDataCraftWeaponLbowProd = WorldDataCraftWeaponLbowProd + TempString

    if os.path.exists(os.path.dirname(os.path.abspath(__file__)) + "\\Mods\\WorldDataCraftWeaponLbowReq.json"):
        destination = os.path.dirname(os.path.abspath(__file__)) + "\\Mods\\WorldDataCraftWeaponLbowReq.json"
        with open(destination) as file:
            TempString = json.load(file)
            WorldDataCraftWeaponLbowReq  = WorldDataCraftWeaponLbowReq  + TempString

    if os.path.exists(os.path.dirname(os.path.abspath(__file__)) + "\\Mods\\WorldDataCraftWeaponLbowAmm.json"):
        destination = os.path.dirname(os.path.abspath(__file__)) + "\\Mods\\WorldDataCraftWeaponLbowAmm.json"
        with open(destination) as file:
            TempString = json.load(file)
            WorldDataCraftWeaponLbowAmm   = WorldDataCraftWeaponLbowAmm   + TempString

    if os.path.exists(os.path.dirname(os.path.abspath(__file__)) + "\\Mods\\WorldDataCraftWeaponLanProd.json"):
        destination = os.path.dirname(os.path.abspath(__file__)) + "\\Mods\\WorldDataCraftWeaponLanProd.json"
        with open(destination) as file:
            TempString = json.load(file)
            WorldDataCraftWeaponLanProd = WorldDataCraftWeaponLanProd + TempString

    if os.path.exists(os.path.dirname(os.path.abspath(__file__)) + "\\Mods\\WorldDataCraftWeaponLanReq.json"):
        destination = os.path.dirname(os.path.abspath(__file__)) + "\\Mods\\WorldDataCraftWeaponLanReq.json"
        with open(destination) as file:
            TempString = json.load(file)
            WorldDataCraftWeaponLanReq = WorldDataCraftWeaponLanReq + TempString

    if os.path.exists(os.path.dirname(os.path.abspath(__file__)) + "\\Mods\\WorldDataCraftWeaponLanAmm.json"):
        destination = os.path.dirname(os.path.abspath(__file__)) + "\\Mods\\WorldDataCraftWeaponLanAmm.json"
        with open(destination) as file:
            TempString = json.load(file)
            WorldDataCraftWeaponLanAmm = WorldDataCraftWeaponLanAmm + TempString

    if os.path.exists(os.path.dirname(os.path.abspath(__file__)) + "\\Mods\\WorldDataCraftWeaponMacProd.json"):
        destination = os.path.dirname(os.path.abspath(__file__)) + "\\Mods\\WorldDataCraftWeaponMacProd.json"
        with open(destination) as file:
            TempString = json.load(file)
            WorldDataCraftWeaponMacProd = WorldDataCraftWeaponMacProd + TempString

    if os.path.exists(os.path.dirname(os.path.abspath(__file__)) + "\\Mods\\WorldDataCraftWeaponMacReq.json"):
        destination = os.path.dirname(os.path.abspath(__file__)) + "\\Mods\\WorldDataCraftWeaponMacReq.json"
        with open(destination) as file:
            TempString = json.load(file)
            WorldDataCraftWeaponMacReq = WorldDataCraftWeaponMacReq + TempString

    if os.path.exists(os.path.dirname(os.path.abspath(__file__)) + "\\Mods\\WorldDataCraftWeaponMacAmm.json"):
        destination = os.path.dirname(os.path.abspath(__file__)) + "\\Mods\\WorldDataCraftWeaponMacAmm.json"
        with open(destination) as file:
            TempString = json.load(file)
            WorldDataCraftWeaponMacAmm = WorldDataCraftWeaponMacAmm + TempString

    if os.path.exists(os.path.dirname(os.path.abspath(__file__)) + "\\Mods\\WorldDataCraftWeaponGSwoProd.json"):
        destination = os.path.dirname(os.path.abspath(__file__)) + "\\Mods\\WorldDataCraftWeaponGSwoProd.json"
        with open(destination) as file:
            TempString = json.load(file)
            WorldDataCraftWeaponGSwoProd = WorldDataCraftWeaponGSwoProd + TempString

    if os.path.exists(os.path.dirname(os.path.abspath(__file__)) + "\\Mods\\WorldDataCraftWeaponGSwoReq.json"):
        destination = os.path.dirname(os.path.abspath(__file__)) + "\\Mods\\WorldDataCraftWeaponGSwoReq.json"
        with open(destination) as file:
            TempString = json.load(file)
            WorldDataCraftWeaponGSwoReq =  WorldDataCraftWeaponGSwoReq + TempString

    if os.path.exists(os.path.dirname(os.path.abspath(__file__)) + "\\Mods\\WorldDataCraftWeaponGSwoAmm.json"):
        destination = os.path.dirname(os.path.abspath(__file__)) + "\\Mods\\WorldDataCraftWeaponGSwoAmm.json"
        with open(destination) as file:
            TempString = json.load(file)
            WorldDataCraftWeaponGSwoAmm = WorldDataCraftWeaponGSwoAmm  + TempString

    if os.path.exists(os.path.dirname(os.path.abspath(__file__)) + "\\Mods\\WorldDataCraftWeaponSSwoProd.json"):
        destination = os.path.dirname(os.path.abspath(__file__)) + "\\Mods\\WorldDataCraftWeaponSSwoProd.json"
        with open(destination) as file:
            TempString = json.load(file)
            WorldDataCraftWeaponSSwoProd  = WorldDataCraftWeaponSSwoProd   + TempString
   
    if os.path.exists(os.path.dirname(os.path.abspath(__file__)) + "\\Mods\\WorldDataCraftWeaponSSwoReq.json"):
        destination = os.path.dirname(os.path.abspath(__file__)) + "\\Mods\\WorldDataCraftWeaponSSwoReq.json"
        with open(destination) as file:
            TempString = json.load(file)
            WorldDataCraftWeaponSSwoReq  = WorldDataCraftWeaponSSwoReq  + TempString

    if os.path.exists(os.path.dirname(os.path.abspath(__file__)) + "\\Mods\\WorldDataCraftWeaponSSwoAmm.json"):
        destination = os.path.dirname(os.path.abspath(__file__)) + "\\Mods\\WorldDataCraftWeaponSSwoAmm.json"
        with open(destination) as file:
            TempString = json.load(file)
            WorldDataCraftWeaponSSwoAmm = WorldDataCraftWeaponSSwoAmm + TempString

    if os.path.exists(os.path.dirname(os.path.abspath(__file__)) + "\\Mods\\WorldDataCraftWeaponShuProd.json"):
        destination = os.path.dirname(os.path.abspath(__file__)) + "\\Mods\\WorldDataCraftWeaponShuProd.json"
        with open(destination) as file:
            TempString = json.load(file)
            WorldDataCraftWeaponShuProd = WorldDataCraftWeaponShuProd + TempString

    if os.path.exists(os.path.dirname(os.path.abspath(__file__)) + "\\Mods\\WorldDataCraftWeaponShuReq.json"):
        destination = os.path.dirname(os.path.abspath(__file__)) + "\\Mods\\WorldDataCraftWeaponShuReq.json"
        with open(destination) as file:
            TempString = json.load(file)
            WorldDataCraftWeaponShuReq = WorldDataCraftWeaponShuReq + TempString

    if os.path.exists(os.path.dirname(os.path.abspath(__file__)) + "\\Mods\\WorldDataCraftWeaponShuAmm.json"):
        destination = os.path.dirname(os.path.abspath(__file__)) + "\\Mods\\WorldDataCraftWeaponShuAmm.json"
        with open(destination) as file:
            TempString = json.load(file)
            WorldDataCraftWeaponShuAmm = WorldDataCraftWeaponShuAmm + TempString

    if os.path.exists(os.path.dirname(os.path.abspath(__file__)) + "\\Mods\\WorldDataCraftWeaponSbowProd.json"):
        destination = os.path.dirname(os.path.abspath(__file__)) + "\\Mods\\WorldDataCraftWeaponSbowProd.json"
        with open(destination) as file:
            TempString = json.load(file)
            WorldDataCraftWeaponSbowProd = WorldDataCraftWeaponSbowProd + TempString

    if os.path.exists(os.path.dirname(os.path.abspath(__file__)) + "\\Mods\\WorldDataCraftWeaponSbowAmm.json"):
        destination = os.path.dirname(os.path.abspath(__file__)) + "\\Mods\\WorldDataCraftWeaponSbowAmm.json"
        with open(destination) as file:
            TempString = json.load(file)
            WorldDataCraftWeaponSbowAmm = WorldDataCraftWeaponSbowAmm + TempString

    if os.path.exists(os.path.dirname(os.path.abspath(__file__)) + "\\Mods\\WorldDataCraftWeaponSbowReq.json"):
        destination = os.path.dirname(os.path.abspath(__file__)) + "\\Mods\\WorldDataCraftWeaponSbowReq.json"
        with open(destination) as file:
            TempString = json.load(file)
            WorldDataCraftWeaponSbowReq = WorldDataCraftWeaponSbowReq + TempString

    if os.path.exists(os.path.dirname(os.path.abspath(__file__)) + "\\Mods\\WorldDataCraftWeaponCbowProd.json"):
        destination = os.path.dirname(os.path.abspath(__file__)) + "\\Mods\\WorldDataCraftWeaponCbowProd.json"
        with open(destination) as file:
            TempString = json.load(file)
            WorldDataCraftWeaponCbowProd = WorldDataCraftWeaponCbowProd + TempString

    if os.path.exists(os.path.dirname(os.path.abspath(__file__)) + "\\Mods\\WorldDataCraftWeaponCbowReq.json"):
        destination = os.path.dirname(os.path.abspath(__file__)) + "\\Mods\\WorldDataCraftWeaponCbowReq.json"
        with open(destination) as file:
            TempString = json.load(file)
            WorldDataCraftWeaponCbowReq = WorldDataCraftWeaponCbowReq + TempString

    if os.path.exists(os.path.dirname(os.path.abspath(__file__)) + "\\Mods\\WorldDataCraftWeaponCbowAmm.json"):
        destination = os.path.dirname(os.path.abspath(__file__)) + "\\Mods\\WorldDataCraftWeaponCbowAmm.json"
        with open(destination) as file:
            TempString = json.load(file)
            WorldDataCraftWeaponCbowAmm = WorldDataCraftWeaponCbowAmm + TempString

    if os.path.exists(os.path.dirname(os.path.abspath(__file__)) + "\\Mods\\WorldDataCraftArmorProd.json"):
        destination = os.path.dirname(os.path.abspath(__file__)) + "\\Mods\\WorldDataCraftArmorProd.json"
        with open(destination) as file:
            TempString = json.load(file)
            WorldDataCraftArmorProd = WorldDataCraftArmorProd + TempString

    if os.path.exists(os.path.dirname(os.path.abspath(__file__)) + "\\Mods\\WorldDataCraftArmorReq.json"):
        destination = os.path.dirname(os.path.abspath(__file__)) + "\\Mods\\WorldDataCraftArmorReq.json"
        with open(destination) as file:
            TempString = json.load(file)
            WorldDataCraftArmorReq = WorldDataCraftArmorReq + TempString

    if os.path.exists(os.path.dirname(os.path.abspath(__file__)) + "\\Mods\\WorldDataCraftArmorAmm.json"):
        destination = os.path.dirname(os.path.abspath(__file__)) + "\\Mods\\WorldDataCraftArmorAmm.json"
        with open(destination) as file:
            TempString = json.load(file)
            WorldDataCraftArmorAmm = WorldDataCraftArmorAmm + TempString

    if os.path.exists(os.path.dirname(os.path.abspath(__file__)) + "\\Mods\\WorldDataTradeProd.json"):
        destination = os.path.dirname(os.path.abspath(__file__)) + "\\Mods\\WorldDataTradeProd.json"
        with open(destination) as file:
            TempString = json.load(file)
            WorldDataTradeProd = WorldDataTradeProd + TempString

    if os.path.exists(os.path.dirname(os.path.abspath(__file__)) + "\\Mods\\WorldDataTradePrice.json"):
        destination = os.path.dirname(os.path.abspath(__file__)) + "\\Mods\\WorldDataTradePrice.json"
        with open(destination) as file:
            TempString = json.load(file)
            WorldDataTradePrice = WorldDataTradePrice + TempString

    Menu()

def Menu(): #  Menu
    global LatestVer
    global PlayerInfo
    global Save
    global Log

    Log.append("Menu loaded")
    os.system("cls") #clears screen
    print("Rougealike RPG by TMAltair\n1) Play\n2) Load\n3) Guide\nQ) Quit\n\nVersion " + str(SystemInfo[1]) + " (" + str(SystemInfo[0]) + ")")
    if LatestVer == "Failed": #If an error occurs prints this
        Log.append("Auto Update failed")
        print("Could not talk to the AutoUpdate webpage.\nTo see if Rougealike has an update go to\nhttps://github.com/TMAltair/Roguealike/")
    elif LatestVer == "Declined": #If update is declined
        Log.append("Update declined.")
        print("Update available!\nPress U) to update!")
    elif LatestVer == "ERROR": #If auto update is not changed for some reason
        Log.append("Error occured in update (THIS SHOULD NOT HAPPEN)")
        print("An Error occured in the update.")
    elif LatestVer == "DISABLED": # If autoupdate is disabled in the Config.txt
        Log.append("Update is disabled")
        print("AutoUpdate is disabled.")
    elif LatestVer == "GLOBALLY DISABLED":
        Log.append("AutoUpdate is banned for this version")
        print("This version is currently banned from autoupdate")
    Loop = 1
    while Loop == 1:
        if keyboard.is_pressed("1"):
            os.system("cls")
            PlayerInfo[0] = str(input("Enter a name: "))
            Log.append("Player name set (" + str(PlayerInfo[0]) +")")
            PlayerInfo[1] = -1
            PlayerInfo[2] = 0
            PlayerInfo[3] = 0
            os.system("cls")
            Loop2 = 1
            print("Select a difficulty:\n1) Easy\nEnemies have less HP and do more damage\n\n2) Normal\nBattles should be fun\n\n3) Hard\nBattles require merticulous planning of healing and equipment\n\n4) Insane\n\"Good for short people who want to do somthing.\"")
            while Loop2 == 1:
                if keyboard.is_pressed("1"):
                    PlayerInfo[1] = 1
                    Loop2 = 2
                elif keyboard.is_pressed("2"):
                    PlayerInfo[1] = 2
                    Loop2 = 2
                elif keyboard.is_pressed("3"):
                    PlayerInfo[1] = 3
                    Loop2 = 2
                elif keyboard.is_pressed("4"):
                    PlayerInfo[1] = 4
                    Loop2 = 2
            Log.append("Difficulty set to " + str(PlayerInfo[1]))

            PlayerInfo[2] = 0   #X Coord
            PlayerInfo[3] = 0   #Y Coord 
            WorldGeneration()
        elif keyboard.is_pressed("2"):
            Save = 2 
            SaveLoad()
        elif keyboard.is_pressed("3"):
            Loop0 = 1
            Loop1 = 1
            os.system("cls")
            while Loop0 == 1:
                if Loop1 == 0:
                    time.sleep(5)
                    os.system("cls")

                print("Rougealike Guide\n\n1) Whats new?\n2) How do I play?\n3) How do I get more spells?\n4) How do I get better weapons or armor?\n5) Monoliths?\n6) Cave?\n7) Villages?\n8) Trader Outposts?\nQ) Quit")
                Loop1 = 1
                time.sleep(1)
                while Loop1 == 1:
                    if keyboard.is_pressed("1"):
                        print("Add info")
                        Loop1 = 0
                    elif keyboard.is_pressed("2"):
                        print("You can battle enemies to get stronger\nYou can also get resources in the world or you can mine them in a cave\nUsing these resources you can crafted powerful weapons and armor\n\nAfter this you can explore dungeons and fight powerful bosses\nOr if you don't want to do that you can complete quests.")
                        Loop1 = 0
                    elif keyboard.is_pressed("3"):
                        print("You can get more spells by finding a monolith (1/50 chance)")
                        Loop1 = 0
                    elif keyboard.is_pressed("4"):
                        print("You can get better weaponry or Armor by crafting it a villages which requrires ore")
                        Loop1 = 0
                    elif keyboard.is_pressed("5"):
                        print("A monolith is place where you can learn magic for free, It also increases your max mana by 5-15")
                        Loop1 = 0
                    elif keyboard.is_pressed("6"):
                        print("You can randomly find caves, and depending on the type it will contain different resources (Gems, Metals, ect)")
                        Loop1 = 0
                    elif keyboard.is_pressed("7"):
                        print("You can randomly find villages you can forge weapons and armor")
                        Loop1 = 0
                    elif keyboard.is_pressed("8"):
                        print("At trader outposts you can buy and sell items.")
                        Loop1 = 0
                    elif keyboard.is_pressed("Q"):
                        Menu()
        elif keyboard.is_pressed("u"):
            Intialise()

def WorldGeneration(): # Loads or generates terrain
    global PlayerInfo
    global TerrainType
    global TerrainTypeMeta
    global Terrain
    global Resource
    global ResourceAmmount
    global Enemy
    global Weather
    global Log
    global Terrain

    Log.append("World Generation")
    if os.path.exists(os.path.dirname(os.path.abspath(__file__)) + "\\WorldData\\X" + str(PlayerInfo[2]) + " Y" + str(PlayerInfo[3]) + ".txt"):  #Terrain that needs to be generated
        Log.append("Terrain already exists")
        TerrainType = int(linecache.getline(os.path.dirname(os.path.abspath(__file__)) + "\\WorldData\\X" + str(PlayerInfo[2]) + " Y" + str(PlayerInfo[3]) + ".txt",1))
        
        if TerrainType == 0:    #For standards
            Terrain = int(linecache.getline(os.path.dirname(os.path.abspath(__file__)) + "\\WorldData\\X" + str(PlayerInfo[2]) + " Y" + str(PlayerInfo[3]) + ".txt",2))
        else:   #For non standard Terrains
            TerrainTypeMeta = int(linecache.getline(os.path.dirname(os.path.abspath(__file__)) + "\\WorldData\\X" + str(PlayerInfo[2]) + " Y" + str(PlayerInfo[3]) + ".txt",2))

        Log.append("Set type meta as " + str(TerrainTypeMeta))
        Resource = [int(linecache.getline(os.path.dirname(os.path.abspath(__file__)) + "\\WorldData\\X" + str(PlayerInfo[2]) + " Y" + str(PlayerInfo[3]) + ".txt",3)),int(linecache.getline(os.path.dirname(os.path.abspath(__file__)) + "\\WorldData\\X" + str(PlayerInfo[2]) + " Y" + str(PlayerInfo[3]) + ".txt",5)),int(linecache.getline(os.path.dirname(os.path.abspath(__file__)) + "\\WorldData\\X" + str(PlayerInfo[2]) + " Y" + str(PlayerInfo[3]) + ".txt",7)),int(linecache.getline(os.path.dirname(os.path.abspath(__file__)) + "\\WorldData\\X" + str(PlayerInfo[2]) + " Y" + str(PlayerInfo[3]) + ".txt",9))]
        ResourceAmmount = [int(linecache.getline(os.path.dirname(os.path.abspath(__file__)) + "\\WorldData\\X" + str(PlayerInfo[2]) + " Y" + str(PlayerInfo[3]) + ".txt",4)),int(linecache.getline(os.path.dirname(os.path.abspath(__file__)) + "\\WorldData\\X" + str(PlayerInfo[2]) + " Y" + str(PlayerInfo[3]) + ".txt",6)),int(linecache.getline(os.path.dirname(os.path.abspath(__file__)) + "\\WorldData\\X" + str(PlayerInfo[2]) + " Y" + str(PlayerInfo[3]) + ".txt",8)),int(linecache.getline(os.path.dirname(os.path.abspath(__file__)) + "\\WorldData\\X" + str(PlayerInfo[2]) + " Y" + str(PlayerInfo[3]) + ".txt",10))]
       
        if random.randint(-24,8) > 0:
            Weather = random.randint(3,5)
        else:
            Weather = 0  
        Log.append("Set weather as " + str(Weather))
    else:   #Generates Terrain
        Log.append("Terrain doesn't exist")
        if random.randint(1,8) == 8: # 5% Chance 
            TerrainType = random.randint(1,4) # Terrain isn't needed to be generated
            TerrainTypeMeta = 0
        else:
            TerrainType = 0 # 0 is Normal Terrain
            Terrain  = random.randint(0,len(WorldDataTerrain)-1) # gets terrain
        Log.append("Set type meta as " + str(TerrainTypeMeta))
        Resource = [random.randint(-1,len(WorldDataResource)-1),random.randint(-10,len(WorldDataResource)-1),random.randint(-20,len(WorldDataResource)-1),random.randint(-30,len(WorldDataResource)-1)]
        ResourceAmmount = [random.randint(random.randint(1,5),random.randint(5,10)),random.randint(random.randint(1,5),random.randint(5,10)),random.randint(random.randint(1,5),random.randint(5,10)),random.randint(random.randint(1,5),random.randint(5,10))]
        Log.append("Attempting to write file")
        with open(os.path.dirname(os.path.abspath(__file__)) + "\\WorldData\\X" + str(PlayerInfo[2]) + " Y" + str(PlayerInfo[3]) + ".txt","w") as WorldFile:
            if TerrainType == 0:
                WorldFile.write(str(TerrainType) + "\n" + str(Terrain) + "\n" + str(Resource[0]) + "\n" + str(ResourceAmmount[0]) +  "\n" + str(Resource[1]) + "\n" + str(ResourceAmmount[1]) + "\n" +  str(Resource[2]) + "\n" + str(ResourceAmmount[2]) + "\n" + str(Resource[3]) + "\n" + str(ResourceAmmount[3]))
            else:
                WorldFile.write(str(TerrainType) + "\n" + str(TerrainTypeMeta) + "\n" + str(Resource[0]) + "\n" + str(ResourceAmmount[0]) +  "\n" + str(Resource[1]) + "\n" + str(ResourceAmmount[1]) + "\n" +  str(Resource[2]) + "\n" + str(ResourceAmmount[2]) + "\n" + str(Resource[3]) + "\n" + str(ResourceAmmount[3]))
            WorldFile.close()
        Log.append("Wrote file")
        if random.randint(-50,5) > 0:
            Weather = random.randint(1,2)
            if Weather == 1:
                ResourceAmmount[0] = ResourceAmmount[0] * random.randint(1,5)
                ResourceAmmount[1] = ResourceAmmount[1] * random.randint(1,5)
                ResourceAmmount[2] = ResourceAmmount[2] * random.randint(1,5)
                ResourceAmmount[3] = ResourceAmmount[3] * random.randint(1,5)
            elif Weather == 2:
                ResourceAmmount[0] = round(ResourceAmmount[0] / random.randint(1,5))
                ResourceAmmount[1] = round(ResourceAmmount[1] / random.randint(1,5))
                ResourceAmmount[2] = round(ResourceAmmount[2] / random.randint(1,5))
                ResourceAmmount[3] = round(ResourceAmmount[3] / random.randint(1,5))
        else:
            Weather = 0
    Log.append("Set weather as " + str(Weather))

    Enemy = [random.randint(0,1),random.randint(-10,len(WorldDataEnemyPrefix)-1),random.randint(0,len(WorldDataEnemyName)-1),random.randint(-10,len(WorldDataEnemySuffix)-1)] #0- 0/1 1 is enabled    1-Prefix (-1 if disabled)   2-Enemy name    3-Suffix (-1 if disabled) 
    World()

def World(): # Handles terrain and Player choices
    global PlayerInfo
    global BattleLog
    global PlayerInventory
    global PlayerInventoryAmmount
    global Resource
    global ResourceAmmount
    global PlayerInventoryArmourDur
    global PlayerInventoryArmour
    global PlayerInventoryArmourDef
    global PlayerInventoryWeapon
    global PlayerInventoryWeaponAtk
    global PlayerInventoryWeaponDur
    global PlayerInventoryWeaponCrt
    global PlayerInventoryWeaponHit
    global Save
    global Log
    global DungeonData
    global FastTravelX
    global FastTravelY
    global PlayerQuestName
    global PlayerQuestRewardType
    global PlayerQuestReqRes
    global PlayerQuestReqAmm
    global PlayerAchivements
    
    if PlayerInfo[4] >= 100 and PlayerInfo[5] >= 100 and PlayerInfo[6] >= 100:
        PlayerAchivements[3] = 1
    if PlayerInfo[7] >= 10:
        PlayerAchivements[4] = 1
    if PlayerInfo[7] >= 20:
        PlayerAchivements[5] = 1
    if PlayerInfo[2 or 3] == 2147483500 or 2147483500:
        PlayerAchivements[19] = 1
    if PlayerInfo [9] == 1000000:
        PlayerAchivements[20] = 1

    Log.append("Initalised world")
    os.system("cls")
    if DungeonData[4] == 1:
        Dungeon()

    BattleLog[0] = BattleLog[1] 
    BattleLog[1] = BattleLog[2]
    BattleLog[2] = BattleLog[3]
    BattleLog[3] = BattleLog[4]
    BattleLog[4] = BattleLog[5]
    BattleLog[5] = ""
    if BattleLog[0] != "":
        print(BattleLog[0])
    if BattleLog[1] != "":
        print(BattleLog[1])
    if BattleLog[2] != "":
        print(BattleLog[2])
    if BattleLog[3] != "":
        print(BattleLog[3])
    if BattleLog[4] != "":
        print(BattleLog[4])
    if BattleLog[5] != "":
        print(BattleLog[5])
    Log.append("Battle Log printed ")

    if TerrainType == 0:    #Terrain
        print(Fore.__getattribute__(WorldDataTerrainColor[Terrain]) + Style.__getattribute__(WorldDataTerrainBrightness[Terrain]) + "You are " + str(WorldDataTerrain[Terrain]) + ".")
    else:
        if TerrainType == 1 and TerrainTypeMeta == 0:
            print("You are at a monolith.")
        elif TerrainType == 2 and TerrainTypeMeta == 0:
            if ResourceAmmount[0] <= 5:
                print("You are at a cave")
                CaveType = 0
            else:
                print("You are at a gem cave")
                CaveType = 1
        elif TerrainType == 3 and TerrainTypeMeta == 0:
            print("You are at a village.")
            PlayerInfo[20] = PlayerInfo[2]
            PlayerInfo[21] = PlayerInfo[3]
            if PlayerInfo[2] not in FastTravelX or PlayerInfo[3] not in FastTravelY:
                FastTravelX.append(PlayerInfo[2])
                FastTravelY.append(PlayerInfo[3])
        elif TerrainType == 4 and TerrainTypeMeta == 0:
            print("You are at a trader outpost.")
        elif TerrainType == 5:
            print("There is a dungeon here.")    
        elif TerrainType == 6:
            print("There is a legends forge here.")  
        elif TerrainType == 7:
            print("There is a strange shop here.") 
        elif TerrainType == 8:
            print("There is a Noticeboard here") 

    TopRow = ["","",""]
    MidRow = ["","",""]
    LowRow = ["","",""]
    
    #map code
    if os.path.exists(os.path.dirname(os.path.abspath(__file__)) + "\\WorldData\\X" + str(int(PlayerInfo[2] - 1)) + " Y" + str(int(PlayerInfo[3] + 1)) + ".txt"):
        if int(linecache.getline(os.path.dirname(os.path.abspath(__file__)) + "\\WorldData\\X" + str(int(PlayerInfo[2] - 1)) + " Y" + str(int(PlayerInfo[3] + 1)) + ".txt",1)) == 0:
            TopRow[0] = "[ " + WorldDataMapIcon[int(linecache.getline(os.path.dirname(os.path.abspath(__file__)) + "\\WorldData\\X" + str(int(PlayerInfo[2] - 1)) + " Y" + str(int(PlayerInfo[3] + 1)) + ".txt",2))] + " ] "
        else:
            TopRow[0] = "[ ? ] "
    else:
        TopRow[0] = "[ # ] "

    if os.path.exists(os.path.dirname(os.path.abspath(__file__)) + "\\WorldData\\X" + str(int(PlayerInfo[2])) + " Y" + str(int(PlayerInfo[3] + 1)) + ".txt"):
        if int(linecache.getline(os.path.dirname(os.path.abspath(__file__)) + "\\WorldData\\X" + str(int(PlayerInfo[2])) + " Y" + str(int(PlayerInfo[3] + 1)) + ".txt",1)) == 0:
            TopRow[1] = "[ " + WorldDataMapIcon[int(linecache.getline(os.path.dirname(os.path.abspath(__file__)) + "\\WorldData\\X" + str(int(PlayerInfo[2])) + " Y" + str(int(PlayerInfo[3] + 1)) + ".txt",2))] + " ] "
        else:
            TopRow[1] = "[ ? ] "
    else:
        TopRow[1] = "[ # ] "

    if os.path.exists(os.path.dirname(os.path.abspath(__file__)) + "\\WorldData\\X" + str(int(PlayerInfo[2] + 1)) + " Y" + str(int(PlayerInfo[3] + 1)) + ".txt"):
        if int(linecache.getline(os.path.dirname(os.path.abspath(__file__)) + "\\WorldData\\X" + str(int(PlayerInfo[2] + 1)) + " Y" + str(int(PlayerInfo[3] + 1)) + ".txt",1)) == 0:
            TopRow[2] = "[ " + WorldDataMapIcon[int(linecache.getline(os.path.dirname(os.path.abspath(__file__)) + "\\WorldData\\X" + str(int(PlayerInfo[2] + 1)) + " Y" + str(int(PlayerInfo[3] + 1)) + ".txt",2))] + " ] "
        else:
            TopRow[2] = "[ ? ] "
    else:
        TopRow[2] = "[ # ] "

    if os.path.exists(os.path.dirname(os.path.abspath(__file__)) + "\\WorldData\\X" + str(int(PlayerInfo[2] - 1)) + " Y" + str(int(PlayerInfo[3])) + ".txt"):
        if int(linecache.getline(os.path.dirname(os.path.abspath(__file__)) + "\\WorldData\\X" + str(int(PlayerInfo[2] - 1)) + " Y" + str(int(PlayerInfo[3])) + ".txt",1)) == 0:
            MidRow[0] = "[ " + WorldDataMapIcon[int(linecache.getline(os.path.dirname(os.path.abspath(__file__)) + "\\WorldData\\X" + str(int(PlayerInfo[2] - 1)) + " Y" + str(int(PlayerInfo[3])) + ".txt",2))] + " ] "
        else:
            MidRow[0] = "[ ? ] "
    else:
        MidRow[0] = "[ # ] "

    if os.path.exists(os.path.dirname(os.path.abspath(__file__)) + "\\WorldData\\X" + str(int(PlayerInfo[2] )) + " Y" + str(int(PlayerInfo[3])) + ".txt"):
        if int(linecache.getline(os.path.dirname(os.path.abspath(__file__)) + "\\WorldData\\X" + str(int(PlayerInfo[2])) + " Y" + str(int(PlayerInfo[3])) + ".txt",1)) == 0:
            MidRow[1] = "[ " + WorldDataMapIcon[int(linecache.getline(os.path.dirname(os.path.abspath(__file__)) + "\\WorldData\\X" + str(int(PlayerInfo[2])) + " Y" + str(int(PlayerInfo[3])) + ".txt",2))] + " ] "
        else:
            MidRow[1] = "[ ? ] "
    else:
        MidRow[1] = "[ # ] "

    if os.path.exists(os.path.dirname(os.path.abspath(__file__)) + "\\WorldData\\X" + str(int(PlayerInfo[2] + 1)) + " Y" + str(int(PlayerInfo[3])) + ".txt"):
        if int(linecache.getline(os.path.dirname(os.path.abspath(__file__)) + "\\WorldData\\X" + str(int(PlayerInfo[2] + 1)) + " Y" + str(int(PlayerInfo[3])) + ".txt",1)) == 0:
            MidRow[2] = "[ " + WorldDataMapIcon[int(linecache.getline(os.path.dirname(os.path.abspath(__file__)) + "\\WorldData\\X" + str(int(PlayerInfo[2] + 1)) + " Y" + str(int(PlayerInfo[3])) + ".txt",2))] + " ] "
        else:
            MidRow[2] = "[ ? ] "
    else:
        MidRow[2] = "[ # ] "

    if os.path.exists(os.path.dirname(os.path.abspath(__file__)) + "\\WorldData\\X" + str(int(PlayerInfo[2] - 1)) + " Y" + str(int(PlayerInfo[3] - 1)) + ".txt"):
        if int(linecache.getline(os.path.dirname(os.path.abspath(__file__)) + "\\WorldData\\X" + str(int(PlayerInfo[2] - 1)) + " Y" + str(int(PlayerInfo[3] - 1)) + ".txt",1)) == 0:
            LowRow[0] = "[ " + WorldDataMapIcon[int(linecache.getline(os.path.dirname(os.path.abspath(__file__)) + "\\WorldData\\X" + str(int(PlayerInfo[2] - 1)) + " Y" + str(int(PlayerInfo[3] - 1)) + ".txt",2))] + " ] "
        else:
            LowRow[0] = "[ ? ] "
    else:
        LowRow[0] = "[ # ] "

    if os.path.exists(os.path.dirname(os.path.abspath(__file__)) + "\\WorldData\\X" + str(int(PlayerInfo[2])) + " Y" + str(int(PlayerInfo[3] - 1)) + ".txt"):
        if int(linecache.getline(os.path.dirname(os.path.abspath(__file__)) + "\\WorldData\\X" + str(int(PlayerInfo[2])) + " Y" + str(int(PlayerInfo[3] - 1)) + ".txt",1)) == 0:
            LowRow[1] = "[ " + WorldDataMapIcon[int(linecache.getline(os.path.dirname(os.path.abspath(__file__)) + "\\WorldData\\X" + str(int(PlayerInfo[2])) + " Y" + str(int(PlayerInfo[3] - 1)) + ".txt",2))] + " ] "
        else:
            LowRow[1] = "[ ? ] "
    else:
        LowRow[1] = "[ # ] "

    if os.path.exists(os.path.dirname(os.path.abspath(__file__)) + "\\WorldData\\X" + str(int(PlayerInfo[2] - 1)) + " Y" + str(int(PlayerInfo[3] - 1)) + ".txt"):
        if int(linecache.getline(os.path.dirname(os.path.abspath(__file__)) + "\\WorldData\\X" + str(int(PlayerInfo[2] - 1)) + " Y" + str(int(PlayerInfo[3] - 1)) + ".txt",1)) == 0:
            LowRow[2] = "[ " + WorldDataMapIcon[int(linecache.getline(os.path.dirname(os.path.abspath(__file__)) + "\\WorldData\\X" + str(int(PlayerInfo[2] - 1)) + " Y" + str(int(PlayerInfo[3] - 1)) + ".txt",2))] + " ] "
        else:
            LowRow[2] = "[ ? ] "
    else:
        LowRow[2] = "[ # ] "

    #Terrain code
    Log.append("Printed Terrain")
    ResourceText = "There are "
    if Resource[0] >= 0:
        ResourceText = ResourceText + str(Fore.__getattribute__(WorldDataResourceColor[Resource[0]]) + Style.__getattribute__(WorldDataResourceBrightness[Resource[0]]) + str(ResourceAmmount[0]) + " " + str(WorldDataResource[Resource[0]]) + Fore.RESET + ", ")
    if Resource[1] >= 0:
        ResourceText = ResourceText + str(Fore.__getattribute__(WorldDataResourceColor[Resource[1]]) + Style.__getattribute__(WorldDataResourceBrightness[Resource[1]]) + str(ResourceAmmount[1]) + " " + str(WorldDataResource[Resource[1]]) + Fore.RESET + ", ")
    if Resource[2] >= 0:
        ResourceText = ResourceText + str(Fore.__getattribute__(WorldDataResourceColor[Resource[2]]) + Style.__getattribute__(WorldDataResourceBrightness[Resource[2]]) + str(ResourceAmmount[2]) + " " + str(WorldDataResource[Resource[2]]) + Fore.RESET + ", ")
    if Resource[3] >= 0:
        ResourceText = ResourceText + str(Fore.__getattribute__(WorldDataResourceColor[Resource[3]]) + Style.__getattribute__(WorldDataResourceBrightness[Resource[3]]) + str(ResourceAmmount[3]) + " " + str(WorldDataResource[Resource[3]]))
    if ResourceText == "There are ":
        time.sleep(0)
    else:
        print(Fore.RESET + str(ResourceText) + Fore.RESET)
    Log.append("Printed resource")

    #Enemy code
    EnemyText = ""
    if Enemy[0] == 0:
        EnemyText = Fore.RED + "There is a "
    if Enemy[1] >= 0:
        EnemyText = EnemyText + WorldDataEnemyPrefix[Enemy[1]] + " "
    if Enemy[0] == 0:
        EnemyText = EnemyText + WorldDataEnemyName[Enemy[2]] + " "
    if Enemy[3] >= 0:
        EnemyText = EnemyText + WorldDataEnemySuffix[Enemy[3]]
    if Enemy[0] == 0:
        print(EnemyText + " here.")
    Log.append("Printed enemy")

    if Weather > 0:
        print(Fore.YELLOW + "It is also very " + WorldDataWeather[Weather] + "." + Fore.RESET)
    Log.append("Printed Weather")

    print(Fore.RESET + "\n\n1) Battle    2) Move      3) Collect Items     " + str(TopRow[0]) +  str(TopRow[1]) + str(TopRow[2]) + "\n4) Character 5) Save/Load 6) Quit              " + str(MidRow[0]) +  str(MidRow[1]) + str(MidRow[2]))
    
    if TerrainType == 1 and TerrainTypeMeta == 0:
        print("7) Use Monolith                                " + str(LowRow[0]) + str(LowRow[1]) + str(LowRow[2]))
    elif TerrainType == 2 and TerrainTypeMeta == 0:
        print("7) Mine                                        " + str(LowRow[0]) + str(LowRow[1]) + str(LowRow[2]))
    elif TerrainType == 3 and TerrainTypeMeta == 0:
        print("7) Enter Village                               " + str(LowRow[0]) + str(LowRow[1]) + str(LowRow[2]))
    elif TerrainType == 4 and TerrainTypeMeta == 0:
        print("7) Trade                                       " + str(LowRow[0]) + str(LowRow[1]) + str(LowRow[2]))
    elif TerrainType == 5 and TerrainTypeMeta == 0:
        print("7) Enter Dungeon                               " + str(LowRow[0]) + str(LowRow[1]) + str(LowRow[2]))
    elif TerrainType == 6 and TerrainTypeMeta == 0:
        print("7) Enter Forge                                 " + str(LowRow[0]) + str(LowRow[1]) + str(LowRow[2]))
    elif TerrainType == 7 and TerrainTypeMeta == 0:
        print("7) Enter Shop                                  " + str(LowRow[0]) + str(LowRow[1]) + str(LowRow[2]))
    elif TerrainType == 8 and TerrainTypeMeta == 0:
        print("7) Read Noticeboard                            " + str(LowRow[0]) + str(LowRow[1]) + str(LowRow[2]))
    else:
        if  WorldDataProffessionData[Terrain] == 1:
            print("8) Fish                                        "+ str(LowRow[0]) + str(LowRow[1]) + str(LowRow[2]))
        elif WorldDataProffessionData[Terrain] == 2:
            print("8) Log                                         " + str(LowRow[0]) + str(LowRow[1]) + str(LowRow[2])) 
        else:
            time.sleep(0)
            print("                                               " + str(LowRow[0]) + str(LowRow[1]) + str(LowRow[2]))
    Log.append("Printed Options")

    Loop = 1
    time.sleep(1)
    Log.append("Initalised options loop")
    while Loop == 1:
        if keyboard.is_pressed("1"):   # Battle
            Log.append("Battle")
            if Enemy[0] == 1:
                print("There's no enemy to battle!")
                time.sleep(2.5)
                World()
            else:
                Battle()
        elif keyboard.is_pressed("2"): # Movement
            Log.append("Moving")
            print("\nSelect a direction to move\n         (1)\n        North\n(4) West     East (2)\n        South\n         (3)")
            time.sleep(1)

            if random.randint(1,10) == 1:   #Ambush code
                os.system("cls")
                print("You were ambushed!")
                BattleLog[5] = "You tryed to move but you were ambushed!"
                time.sleep(1)
                Battle()
            Loop = 1
            while Loop == 1: # Move code
                if keyboard.is_pressed("1"):
                    PlayerInfo[3] = PlayerInfo[3] + 1
                    BattleLog[5] = "Moved North"
                    WorldGeneration()
                elif keyboard.is_pressed("2"):
                    PlayerInfo[2] = PlayerInfo[2] + 1
                    BattleLog[5] = "Moved East"
                    WorldGeneration()
                elif keyboard.is_pressed("3"):
                    PlayerInfo[3] = PlayerInfo[3] - 1
                    BattleLog[5] = "Moved South"
                    WorldGeneration()
                elif keyboard.is_pressed("4"):
                    PlayerInfo[2] = PlayerInfo[2] - 1
                    BattleLog[5] = "Moved West"
                    WorldGeneration()
        elif keyboard.is_pressed("3"): # Collection
            Log.append("Collection")
            if sum(PlayerInventoryAmmount) >= 20 * PlayerInfo[7]:
                print("You are carrying too much.")
                PlayerAchivements[15] = 1
                time.sleep(1.5)
                World()

            TempInt = 0
            while TempInt <= int(len(Resource) - 1): #Just in case resource gets increased at some point
                if Resource[TempInt] >= 0:
                    if WorldDataResource[Resource[TempInt]] in PlayerInventory:
                        PlayerInventoryAmmount[PlayerInventory.index(WorldDataResource[Resource[TempInt]])] = PlayerInventoryAmmount[PlayerInventory.index(WorldDataResource[Resource[TempInt]])] + ResourceAmmount[TempInt]
                    else:
                        PlayerInventory.append(WorldDataResource[Resource[TempInt]])
                        PlayerInventoryAmmount.append(ResourceAmmount[TempInt])
                    Resource[TempInt] = -1
                    ResourceAmmount[TempInt] = 0
                TempInt = TempInt + 1

            with open(os.path.dirname(os.path.abspath(__file__)) + "\\WorldData\\X" + str(PlayerInfo[2]) + " Y" + str(PlayerInfo[3]) + ".txt","w") as WorldFile:
                if TerrainType == 0:
                    WorldFile.write(str(TerrainType) + "\n" + str(Terrain) + "\n" + str(Resource[0]) + "\n" + str(ResourceAmmount[0]) +  "\n" + str(Resource[1]) + "\n" + str(ResourceAmmount[1]) + "\n" +  str(Resource[2]) + "\n" + str(ResourceAmmount[2]) + "\n" + str(Resource[3]) + "\n" + str(ResourceAmmount[3]))
                else:
                    WorldFile.write(str(TerrainType) + "\n" + str(TerrainTypeMeta) + "\n" + str(Resource[0]) + "\n" + str(ResourceAmmount[0]) +  "\n" + str(Resource[1]) + "\n" + str(ResourceAmmount[1]) + "\n" +  str(Resource[2]) + "\n" + str(ResourceAmmount[2]) + "\n" + str(Resource[3]) + "\n" + str(ResourceAmmount[3]))
                WorldFile.close()   #This rewrites the world file to stop infinte resources
            World()
        elif keyboard.is_pressed("4"): # Character
            Log.append("Printing character")
            Loop3 = 1
            while Loop3 == 1:
                os.system("cls")
                print("Name: " + str(PlayerInfo[0]) + " Level: " + str(PlayerInfo[7]) +" (" + str(PlayerInfo[8]) + "/" + str(PlayerInfo[7] * 1000) +")\nHP: " + str(PlayerCurrentStats[0])+ "/" + str(PlayerInfo[4]) + "  Mana: " + str(PlayerInfo[18]) + "/" + str(PlayerCurrentStats[1]) +"  Attack: " + str(PlayerInfo[5]) + "  Defence: " +  str(PlayerInfo[6]) + "\nLocation: X:" + str(PlayerInfo[2]) + " Y:" + str(PlayerInfo[3]) + "  Gold:" + str(PlayerInfo[9]) + "  Reputation: " + str(PlayerInfo[22]) + "\nEquipped Weapon: " + str(PlayerInfo[10]) + "    Attack: " + str(PlayerInfo[11]) + "    Hit:" + str(PlayerInfo[12]) + "%   Critical:" + str(PlayerInfo[13]) + "%    Durabilty: " + str(PlayerInfo[14]) + "%\nEquipped Armour: " + str(PlayerInfo[15]) + "    Defence:" + str(PlayerInfo[16]) + "    Durabilty: " + str(PlayerInfo[17]) + "\n\n1) Equip Armor   2) Equip Weapons   3) View Items   4) Fast Travel\n5) Quests        6) Achivements     Q) Go Back")
                Loop2 = 1
                time.sleep(1.5)
                while Loop2 == 1:
                    if keyboard.is_pressed("1"):   # Equip armor
                        TempInt = 0
                        while TempInt <= int(len(PlayerInventoryArmour) - 1):
                            print(PlayerInventoryArmour[TempInt] + "  Defence: " + str(PlayerInventoryArmourDef[TempInt]) + "  Durability: " + str(PlayerInventoryArmourDur[TempInt]) + "  ID: " + str(TempInt))
                            TempInt = TempInt + 1
                        TempStr = input("\n\nEquiped: " + str(PlayerInfo[15]) + "  Defence: " + str(PlayerInfo[16]) + "  Durability: " + str(PlayerInfo[17]) + "Type the id of an armor to equip it (or type leave with no capitals to leave)\n")
                        TempInt = 0 

                        if TempStr == "leave":
                            World()

                        try:
                            TempStr = int(TempStr)
                        except:
                            TempInt = 1 #Raises a flag to prevent a str from being interpreted
                        else:
                            TempInt = 0 
                            int(TempStr) #You either die a String or live long enough to become a interger

                        if TempInt == 0 and int(len(PlayerInventoryArmour)-1) >= TempStr:
                            PlayerInventoryArmour.append(PlayerInfo[15]) #Adds Equipped Armor to PlayerInventory
                            PlayerInventoryArmourDef.append(PlayerInfo[16])
                            PlayerInventoryArmourDur.append(PlayerInfo[17])
                            PlayerInfo[15] = PlayerInventoryArmour[TempStr] #Sets new Armor as Equiped
                            PlayerInfo[16] = PlayerInventoryArmourDef[TempStr]
                            PlayerInfo[17] = PlayerInventoryArmourDur[TempStr]
                            PlayerInventoryArmour.pop(TempStr)  #Removes new armor from inventory
                            PlayerInventoryArmourDef.pop(TempStr)
                            PlayerInventoryArmourDur.pop(TempStr)
                            print("Equipped " + str(PlayerInfo[15]))
                            time.sleep(1)
                            Loop2 = 0
                        else:
                            print("an error occured while processing your ID, please use numbers only for IDs and your ID exists.")
                    elif keyboard.is_pressed("2"): # Equip Weapons
                        Loop2 = 1
                        while Loop2 == 1:
                            os.system("cls")
                            TempInt = 0
                            while TempInt <= int(len(PlayerInventoryWeapon)-1):
                                print(str(PlayerInventoryWeapon[TempInt]) + "  Attack: " + str(PlayerInventoryWeaponAtk[TempInt]) + "  Durability: " + str(PlayerInventoryWeaponDur[TempInt]) + "  Critical Rate: " + str(PlayerInventoryWeaponCrt[TempInt]) + "%   Hit Rate: " + str(PlayerInventoryWeaponHit[TempInt]) +   "%   ID: " + str(TempInt))
                                TempInt = TempInt + 1    

                            TempStr = input("You have curently equiped: " + PlayerInfo[10] + "  Attack: " + str(PlayerInfo[11]) + "  Durability: " + str(PlayerInfo[14]) + "  Critical Rate: " + str(PlayerInfo[13]) + "%  Hit Rate: " + str(PlayerInfo[12]) + "%\nType the id of a weapon to equip it (or type leave with no capitals to leave)\n")
                            TempInt = 0
                            if TempStr == "leave":
                                World()
                            try:
                                TempStr = int(TempStr)  #Ironic
                            except:
                                TempInt = 1
                            else:
                                TempInt = 0
                                int(TempStr)

                            if TempInt == 0 and int(len(PlayerInventoryWeapon)-1) >= TempStr:
                                PlayerInventoryWeapon.append(PlayerInfo[10])
                                PlayerInventoryWeaponAtk.append(PlayerInfo[11])
                                PlayerInventoryWeaponDur.append(PlayerInfo[14])
                                PlayerInventoryWeaponHit.append(PlayerInfo[12])
                                PlayerInventoryWeaponCrt.append(PlayerInfo[13])
                                PlayerInfo[10] = PlayerInventoryWeapon[TempStr]
                                PlayerInfo[11] = PlayerInventoryWeaponAtk[TempStr]
                                PlayerInfo[14] = PlayerInventoryWeaponDur[TempStr]
                                PlayerInfo[13] = PlayerInventoryWeaponCrt[TempStr]
                                PlayerInfo[12] = PlayerInventoryWeaponHit[TempStr]              
                                PlayerInventoryWeapon.pop(TempStr)
                                PlayerInventoryWeaponAtk.pop(TempStr)
                                PlayerInventoryWeaponDur.pop(TempStr)
                                PlayerInventoryWeaponCrt.pop(TempStr)
                                PlayerInventoryWeaponHit.pop(TempStr)
                                print("Equipped: " + str(PlayerInfo[10]))
                                time.sleep(1.5)
                                World()
                            else:
                                print("an error occured while processing your ID, please use numbers only for IDs and your ID exists.")
                    elif keyboard.is_pressed("3"): # Items
                        TempInt = 0
                        while TempInt <= int(len(PlayerInventory)-1):
                            print(str(PlayerInventory[TempInt]) + "  (" + str(PlayerInventoryAmmount[TempInt]) +")")
                            TempInt = TempInt + 1
                        input("Press enter to continue\n")
                        Loop2 = 0
                    elif keyboard.is_pressed("4"): # Fast Travel
                        TempInt = 0
                        print("You can fast travel to any village you've been to.")
                        while TempInt <= len(FastTravelX) - 1:
                            print(str(TempInt) + ")  X:" + str(FastTravelX[TempInt]) + " Y:" + str(FastTravelY[TempInt]))
                            TempInt = TempInt + 1
                        Loop0 = 1
                        while Loop0 == 1:
                            print("\nType the number in brackets to travel to it")
                            time.sleep(2)
                            TempInt = input()
                            try:
                                TempInt = int(TempInt)
                                TestVar = FastTravelY[TempInt]
                                TestVar = TestVar
                            except:
                                print("That ID is invalid.")
                            else:
                                TempInt = int(TempInt)
                                Loop0 = 2
                        
                        PlayerAchivements[12] = 1
                        PlayerInfo[2] = FastTravelX[TempInt]
                        PlayerInfo[3] = FastTravelY[TempInt]
                        WorldGeneration()
                    elif keyboard.is_pressed("5"): # Quests
                        TempInt = 1
                        while TempInt <= len(PlayerQuestName) - 1:  #Checks if any are complete
                            if PlayerQuestReqRes[TempInt] in PlayerInventory:
                                if PlayerQuestReqAmm >= PlayerInventoryAmmount[PlayerInventory.index(PlayerQuestReqRes[TempInt])]:
                                    PlayerInventoryAmmount[PlayerInventory.index(PlayerQuestReqRes[TempInt])] = PlayerInventoryAmmount[PlayerInventory.index(PlayerQuestReqRes[TempInt])] - PlayerQuestReqAmm[TempInt]
                                    if PlayerQuestRewardType == 1:
                                        PlayerInventory.append(WorldDataCaveGem[random.randint(0,WorldDataCaveGem - 1)])
                                    else:
                                        PlayerInventory.append(WorldDataCaveMetal[random.randint(0,WorldDataCaveMetal - 1)])
                                    PlayerInventoryAmmount.append(random.randint(1,10))
                                    PlayerQuestName.pop(TempInt)
                                    PlayerQuestReqAmm.pop(TempInt)
                                    PlayerQuestReqRes.pop(TempInt)
                                    PlayerQuestRewardType.pop(TempInt)
                                    if PlayerInventoryAmmount[PlayerInventory.index(PlayerQuestReqRes[TempInt])] <= 0:
                                        PlayerInventoryAmmount.pop(PlayerInventory.index(PlayerQuestReqRes[TempInt]))
                                        PlayerInventory.pop(PlayerInventory.index(PlayerQuestReqRes[TempInt]))
                                    TempInt = TempInt + 1
                                else:
                                    TempInt = TempInt + 1
                            else:
                                TempInt = TempInt + 1
                        
                        TempInt = 1
                        while TempInt <= len(PlayerQuestName) - 1:
                            print(str(PlayerQuestName[TempInt]) + " - Requires " + str(PlayerQuestReqAmm[TempInt]) + " x " + str(PlayerQuestReqRes[TempInt]))    
                            TempInt = TempInt + 1
                        input("\nPress Enter to continue")
                        World()
                    elif keyboard.is_pressed("6"): # Achivements
                        print("\n\nLimitless\nExpand the limits by using mods")
                        if PlayerAchivements[0] == 1:
                            print(Fore.GREEN + "Complete" + Fore.RESET)
                        else:
                            print(Fore.RED + "Not Complete." + Fore.RESET)

                        print("\n\nGodlike\nBuy a stat gem")
                        if PlayerAchivements[1] == 1:
                            print(Fore.GREEN + "Complete" + Fore.RESET)
                        else:
                            print(Fore.RED + "Not Complete." + Fore.RESET)
                        
                        print("\n\nChallenger I\nGet 100 points in ATK, DEF and HP")
                        if PlayerAchivements[2] == 1:
                            print(Fore.GREEN + "Complete" + Fore.RESET)
                        else:
                            print(Fore.RED + "Not Complete." + Fore.RESET)

                        print("\n\nChallenger II\nGet to level 10")
                        if PlayerAchivements[3] == 1:
                            print(Fore.GREEN + "Complete" + Fore.RESET)
                        else:
                            print(Fore.RED + "Not Complete." + Fore.RESET)

                        print("\n\nA certified challeger\nGet to level 20")
                        if PlayerAchivements[4] == 1:
                            print(Fore.GREEN + "Complete" + Fore.RESET)
                        else:
                            print(Fore.RED + "Not Complete." + Fore.RESET)

                        print("\n\nOn the defensive\nUse defence")
                        if PlayerAchivements[5] == 1:
                            print(Fore.GREEN + "Complete" + Fore.RESET)
                        else:
                            print(Fore.RED + "Not Complete." + Fore.RESET)

                        print("\n\nCourt jester\nUse magic")
                        if PlayerAchivements[6] == 1:
                            print(Fore.GREEN + "Complete" + Fore.RESET)
                        else:
                            print(Fore.RED + "Not Complete." + Fore.RESET)

                        print("\n\nZeppeli!\nUnlock all magic")#
                        if PlayerAchivements[7] == 1:
                            print(Fore.GREEN + "Complete" + Fore.RESET)
                        else:
                            print(Fore.RED + "Not Complete." + Fore.RESET)

                        print("\n\nGone missing\nEnter a dungeon")
                        if PlayerAchivements[8] == 1:
                            print(Fore.GREEN + "Complete" + Fore.RESET)
                        else:
                            print(Fore.RED + "Not Complete." + Fore.RESET)

                        print("\n\nGone fishing\nCatch a fish")
                        if PlayerAchivements[9] == 1:
                            print(Fore.GREEN + "Complete" + Fore.RESET)
                        else:
                            print(Fore.RED + "Not Complete." + Fore.RESET)

                        print("\n\nSalesman\nSell somthing at a outpost")
                        if PlayerAchivements[10] == 1:
                            print(Fore.GREEN + "Complete" + Fore.RESET)
                        else:
                            print(Fore.RED + "Not Complete." + Fore.RESET)

                        print("\n\nTimber!\nSuccessfully log a tree")
                        if PlayerAchivements[11] == 1:
                            print(Fore.GREEN + "Complete" + Fore.RESET)
                        else:
                            print(Fore.RED + "Not Complete." + Fore.RESET)

                        print("\n\nQuantum!\nUse fast travel")
                        if PlayerAchivements[12] == 1:
                            print(Fore.GREEN + "Complete" + Fore.RESET)
                        else:
                            print(Fore.RED + "Not Complete." + Fore.RESET)

                        print("\n\nAlvor\nForge somthing")
                        if PlayerAchivements[13] == 1:
                            print(Fore.GREEN + "Complete" + Fore.RESET)
                        else:
                            print(Fore.RED + "Not Complete." + Fore.RESET)

                        print("\n\nA gift from the gods\nForge a legendary weapon")
                        if PlayerAchivements[14] == 1:
                            print(Fore.GREEN + "Complete" + Fore.RESET)
                        else:
                            print(Fore.RED + "Not Complete." + Fore.RESET)

                        print("\n\nSpace?\nCarry too much")
                        if PlayerAchivements[15] == 1:
                            print(Fore.GREEN + "Complete" + Fore.RESET)
                        else:
                            print(Fore.RED + "Not Complete." + Fore.RESET)

                        if PlayerAchivements[16] == 1:
                            print("\n\nThe Wizards Ransom\nComplete the final battle")
                            print(Fore.GREEN + "Complete" + Fore.RESET)

                        if PlayerAchivements[1 and 2 and 3 and 4 and 5 and 6 and 7 and 8 and 9 and 10 and 11 and 12 and 13 and 14 and 15 and 16] == 1:
                            PlayerAchivements[17] = 1
                            print("\n\nTrancendence \nBring color to the bland image by getting all normal achivements\n" + Fore.GREEN + "Complete" + Fore.RESET)

                        if PlayerAchivements[18] == 1:
                            print("\n\nnerd\nMessage TMAltair or be smart enough to unlock it\n" + Fore.GREEN + "Complete" + Fore.RESET)

                        if PlayerAchivements[19] == 1:
                            print("\n\nWord Aesthetics\nReach the world border" + Fore.GREEN + "Complete" + Fore.RESET)

                        if PlayerAchivements[20] == 1:
                            print("\n\nYoshi\nCommit tax fraud and have 1 mil gold at one time" + Fore.GREEN + "Complete" + Fore.RESET)
                        
                        if PlayerAchivements[18 and 19 and 20] == 1:
                            PlayerAchivements[21] = 1
                            print("\n\nPet cheetah\nStop time by getting all secret achivements" + Fore.GREEN + "Complete" + Fore.RESET)

                        if PlayerAchivements[21  and 15] == 1:
                            print("\n\nall stones aquired\nbeat the russian at his own game by unlocking all achivements" + Fore.GREEN + "Complete" + Fore.RESET) 
                            #Stonks
                        
                        input("Press enter to continue")
                        World()
                    elif keyboard.is_pressed("Q"): # Leave
                        World()
        elif keyboard.is_pressed("5"): # Saves and load
            Log.append("Sending to save")
            Save = 0
            SaveLoad()
        elif keyboard.is_pressed("6"): # Quit
            Log.append("Quit")
            print(Fore.RED + "Unless you have saved all data will be lost." + Fore.RESET + "\nAre you sure? (Y/N)")
            Loop3 = 1
            while Loop3 == 1:
                if keyboard.is_pressed("Y"):
                    exit()
                elif keyboard.is_pressed("N"):
                    World()
        elif keyboard.is_pressed("7"): # Non-Standard terrains
            Log.append("Non-Standard Terrains")
            if TerrainType == 1:    # Monoliths:
                PlayerInfo[18] = int(PlayerInfo[18] + random.randint(1,15))
                print("You put your hand to the monolith")
                if PlayerInfo[19] < len(WorldDataMonolithSpell)-1:
                    print("The monolith shoots a beam into the sky, and seconds later you can use a new spell, " + str(WorldDataMonolithSpell[PlayerInfo[19]]))
                    PlayerMagic.append(WorldDataMonolithSpell[PlayerInfo[19]])
                    PlayerMagicCost.append(WorldDataMonolithSpellCost[PlayerInfo[19]])
                    PlayerMagicType.append(WorldDataMonolithSpellType[PlayerInfo[19]])
                    PlayerMagicValue.append(WorldDataMonolithSpellValue[PlayerInfo[19]])
                    PlayerInfo[19] = PlayerInfo[19] + 1

                    os.remove(os.path.dirname(os.path.abspath(__file__)) + "\\WorldData\\X" + str(PlayerInfo[2]) + " Y" + str(PlayerInfo[3]) + ".txt")
                    WorldGeneration()
                else:      
                    PlayerAchivements[7] = 1        
                    print("The monlith seems to have no more infomation to bestow upon you.\nIt fears you have have grown too powerful.")
            elif TerrainType == 2:  # Caves
                    if CaveType == 0:
                       CaveResource =  WorldDataCaveMetal[random.randint(0,len(WorldDataCaveMetal) - 1)]
                    else:
                       CaveResource =  WorldDataCaveGem[random.randint(0,len(WorldDataCaveGem) - 1)]
                    CaveAmmount = random.randint(1,10)
                    print("Mined " + str(CaveAmmount) + " " + str(CaveResource))
                    time.sleep(2.5)

                    if CaveResource in PlayerInventory:
                        PlayerInventoryAmmount[PlayerInventory.index(CaveResource)] = PlayerInventoryAmmount[PlayerInventory.index(CaveResource)] + CaveAmmount
                    else:
                        PlayerInventory.append(CaveResource)
                        PlayerInventoryAmmount.append(CaveAmmount)
                        
                    if random.randint(0,10) == 0:    
                        os.remove(os.path.dirname(os.path.abspath(__file__)) + "\\WorldData\\X" + str(PlayerInfo[2]) + " Y" + str(PlayerInfo[3]) + ".txt")
                    WorldGeneration()
            elif TerrainType == 3:  # Villages
                # Crafting modes 0 -  just add to inventory 1 - Mark as equipable weapon (adds to playerInventoryWeapons) 2- Mark as equipable Armour (PlayerInventoryArmour)
                os.system("cls")
                print(Fore.RESET+ "You are at a village\n1) Use Workbench\n2) use Forge\nQ) leave")
                if PlayerInfo[22] < 10 and PlayerInfo[22] > 0:
                    print("Upon entering the village you recive some gold for killing some monsters!")
                    PlayerInfo[9] = PlayerInfo[9] + random.randint(1,PlayerInfo[22] * 100)
                    PlayerInfo[22] = 0
                elif PlayerInfo[22] > 10 and PlayerInfo[22] > 10:
                    print("Upon entering the village you recive some bonus XP for killing some monsters!")
                    PlayerInfo[8] = PlayerInfo[8] + random.randint(1,PlayerInfo[22] * 100)
                    PlayerInfo[22] = 0
                BattleLog[5] = "You visted a Village"        
                tm = 1
                time.sleep(1)
                while tm == 1:
                    if keyboard.is_pressed("1"):    #Workbench code
                        A = 1
                        time.sleep(1)
                        while A == 1: 
                            os.system("cls")
                            print("What do you want to craft\n1) Items\n2) Armor\n3) Weapons\n")
                            B = 1
                            time.sleep(0.5)
                            while B == 1:   #Gets crafting group
                                if keyboard.is_pressed("1"): #Sets opperating mode to 0
                                    C = 1
                                    print("\nCraft:\n1) Metal\n2) Gem\n")
                                    time.sleep(0.5)
                                    while C == 1:
                                        CraftMode = 0
                                        if keyboard.is_pressed("1"):
                                            Craft = "Metal"
                                            ReqResource = WorldDataCraftMetalReq #What Resource Required
                                            Product     = WorldDataCraftMetalProd     #What will be given to the player
                                            ReqAmmount  = WorldDataCraftMetalAmm
                                            C = 0
                                            B = 0
                                        elif keyboard.is_pressed("2"):
                                            Craft  = "Gem"
                                            ReqResource = WorldDataCraftGemReq #What Resource Required
                                            Product     = WorldDataCraftGemProd     #What will be given to the player
                                            ReqAmmount  = WorldDataCraftGemAmm
                                            C = 0
                                            B = 0
                                elif keyboard.is_pressed("2"): #Sets Opperating mode to 1
                                    CraftMode = 1
                                    Craft = "Armour"
                                    ReqResource = WorldDataCraftArmorReq #What Resource Required
                                    Product     = WorldDataCraftArmorProd     #What will be given to the player
                                    ReqAmmount  = WorldDataCraftArmorAmm
                                    C = 0
                                    B = 0
                                elif keyboard.is_pressed("3"): #Sets Opperating mode to 1
                                    C = 1
                                    CraftMode = 2
                                    print("\nCraft:\n1) Axe\n2) Greatsword\n3) Lance\n4) Longbow\n5) Mace\n6) Shuriken\n7) Shortsword\n8) Shortbow\n9) Crossbow")
                                    time.sleep(1)
                                    while C == 1:
                                        if keyboard.is_pressed("1"):
                                            Craft = "Axe"
                                            ReqResource = WorldDataCraftWeaponAxeReq #What Resource Required
                                            Product     = WorldDataCraftWeaponAxeProd     #What will be given to the player
                                            ReqAmmount  = WorldDataCraftWeaponAxeAmm
                                            C = 0
                                            B = 0
                                        elif keyboard.is_pressed("2"):
                                            Craft = "GSwo"
                                            ReqResource = WorldDataCraftWeaponGSwoReq  #What Resource Required
                                            Product     = WorldDataCraftWeaponGSwoProd #What will be given to the player
                                            ReqAmmount  = WorldDataCraftWeaponGSwoAmm
                                            C = 0
                                            B = 0
                                        elif keyboard.is_pressed("3"):
                                            Craft = "Lance"
                                            ReqResource = WorldDataCraftWeaponLanReq  #What Resource Required
                                            Product     = WorldDataCraftWeaponLanProd #What will be given to the player
                                            ReqAmmount  = WorldDataCraftWeaponLanAmm
                                            C = 0
                                            B = 0
                                        elif keyboard.is_pressed("4"):
                                            Craft = "LBow"
                                            ReqResource = WorldDataCraftWeaponLbowReq  #What Resource Required
                                            Product     = WorldDataCraftWeaponLbowProd #What will be given to the player
                                            ReqAmmount  = WorldDataCraftWeaponLbowAmm
                                            C = 0
                                            B = 0
                                        elif keyboard.is_pressed("5"):
                                            Craft = "Mace"
                                            ReqResource = WorldDataCraftWeaponMacReq  #What Resource Required
                                            Product     = WorldDataCraftWeaponMacProd #What will be given to the player
                                            ReqAmmount  = WorldDataCraftWeaponMacAmm
                                            C = 0
                                            B = 0
                                        elif keyboard.is_pressed("6"):
                                            Craft = "Shu"
                                            ReqResource = WorldDataCraftWeaponShuReq  #What Resource Required
                                            Product     = WorldDataCraftWeaponShuProd #What will be given to the player
                                            ReqAmmount  = WorldDataCraftWeaponShuAmm
                                            C = 0
                                            B = 0
                                        elif keyboard.is_pressed("7"):
                                            Craft = "SSwo"
                                            ReqResource = WorldDataCraftWeaponSSwoReq  #What Resource Required
                                            Product     = WorldDataCraftWeaponSSwoProd #What will be given to the player
                                            ReqAmmount  = WorldDataCraftWeaponSSwoAmm
                                            C = 0
                                            B = 0
                                        elif keyboard.is_pressed("8"):
                                            Craft = "SBow"
                                            ReqResource = WorldDataCraftWeaponSbowReq  #What Resource Required
                                            Product     = WorldDataCraftWeaponSbowProd #What will be given to the player
                                            ReqAmmount  = WorldDataCraftWeaponSbowAmm
                                            C = 0
                                            B = 0
                                        elif keyboard.is_pressed("9"):
                                            Craft = "CBow"
                                            ReqResource = WorldDataCraftWeaponCbowReq  #What Resource Required
                                            Product     = WorldDataCraftWeaponCbowProd #What will be given to the player
                                            ReqAmmount  = WorldDataCraftWeaponCbowAmm
                                            C = 0
                                            B = 0
                            G = 1
                            while G == 1:
                                Temp = 1 # What line number to start from (Don't change)
                                while Temp <= len(Product)-1:    #Gets data
                                    if Temp == 1:
                                        RedText   = []   #Items that cannot be crafted (Internal)
                                        GreenProd = [""] #Items that can be crafted    (Internal)
                                        GreenAmmount  = [""]
                                        GreenResource = [""]
                                        RedTxt   = "" # Text shown to player   (Things that the player has enough of)
                                        Greentxt = "" # Text shown to player (Things that the player has some of)
                                        Redtxt   = "" # Text show to player    (Things that the player has none of)

                                    if ReqResource[Temp] in PlayerInventory: #Checks if player has ReqResource
                                        if ReqAmmount[Temp] <= PlayerInventoryAmmount[PlayerInventory.index(ReqResource[Temp])]: #Checks if player has enough of ReqResource
                                            GreenProd.append(Product[Temp]) #If both checks pass then they can craft it  (Added to GreenText)
                                            GreenAmmount.append(ReqAmmount[Temp])
                                            GreenResource.append(ReqResource[Temp])
                                            Greentxt = Greentxt + str(len(GreenProd) - 1) + ") " +  Product[Temp] + " - Requires: " + str(ReqResource[Temp]) + " (" + str(PlayerInventoryAmmount[PlayerInventory.index(ReqResource[Temp])]) + " / " + str(ReqAmmount[Temp]) + ")\n"
                                        else:
                                            RedText.append(ReqResource[Temp]) # If it fails its added to RedText
                                            RedTxt = RedTxt + Product[Temp] + " - Requires: " + str(ReqResource[Temp]) + " (" + str(PlayerInventoryAmmount[PlayerInventory.index(ReqResource[Temp])]) + " / " + str(ReqAmmount[Temp]) + ")\n"
                                    else:
                                        RedText.append(ReqResource[Temp]) # If it fails its added to RedText
                                        Redtxt = Redtxt + Product[Temp] + " - Requires: " + str(ReqResource[Temp]) + " (0 / " + str(ReqAmmount[Temp]) + ")\n"

                                    Temp = Temp + 1 # Increments Temp by 1 to do the next line
                                
                                print(str(Fore.GREEN + Greentxt + Fore.RED + RedTxt + Redtxt + Fore.RESET)) # Displays items in order of craftibilty
                                E = 1
                                while E == 1:   # Displays and gets input
                                    Select = input("Type the number in brackets to craft the corresponding item, then press enter\nTo leave press 0\n")
                                    
                                    try: #checks if input is a number
                                        Select = int(Select)
                                    except: #if not a number then it will loop
                                        print("That isn't a number, make sure there is no characters in the input.\n")
                                    else: #if it passes above check then this is executed
                                        try: #Tests that the number is a element in GreenText
                                            testvar = GreenProd[Select]
                                            testvar = testvar
                                        except: #If not in list then loop
                                            print("That number isn't valid, make sure it's a number in the brackets.")
                                        else:
                                            E = 2
                                
                                if Select == 0:
                                    WorldGeneration()

                                TempAmmount = PlayerInventoryAmmount[PlayerInventory.index(GreenResource[Select])] - GreenAmmount[Select]
                                if TempAmmount <= 0: #Removes required resource and if below 0 will remove the resource from the player inventory 
                                    PlayerInventoryAmmount.pop(PlayerInventory.index(GreenResource[Select]))
                                    PlayerInventory.pop(GreenResource[Select])
                                else:
                                    PlayerInventoryAmmount[PlayerInventory.index(GreenResource[Select])] = TempAmmount 

                                if CraftMode == 0: # For items
                                    if GreenProd[Select] in PlayerInventory:
                                        PlayerInventoryAmmount[PlayerInventory.index(GreenProd[Select])] = PlayerInventoryAmmount[PlayerInventory.index(GreenProd[Select])] + 1
                                    else:
                                        PlayerInventory.append(GreenProd[Select])
                                        PlayerInventoryAmmount.append(1)
                                    print("Crafted 1 x " + str(GreenProd[Select]))
                                elif CraftMode == 1:    #For Armour
                                    PlayerInventoryArmour.append(GreenProd[Select])
                                    PlayerInventoryArmourDef.append(random.randint(Product.index(GreenProd[Select]) * 10,Product.index(GreenProd[Select]) * 100))
                                    PlayerInventoryArmourDur.append(random.randint(Product.index(GreenProd[Select]) * 10,Product.index(GreenProd[Select]) * 100))
                                    print("Crafted 1 x " + str(GreenProd[Select]) + " - Def: " + str(PlayerInventoryArmourDef[len(PlayerInventoryArmourDef) - 1]) + " Durabilty: " + str(PlayerInventoryArmourDef[len(PlayerInventoryArmourDur) - 1]))
                                elif CraftMode == 2:    #For weapons
                                    #And then I saw him, torch in hand, He laid it out what he had planned.
                                    print("Crafted 1 x " + str(GreenProd[Select]) + " - Atk: " + str(PlayerInventoryWeaponAtk[len(PlayerInventoryWeaponAtk) - 1]) + " Durabilty: " + str(PlayerInventoryWeaponDur[len(PlayerInventoryWeaponDur) - 1]) + " Hit: " + str(PlayerInventoryWeaponHit[len(PlayerInventoryWeaponHit) - 1]) + "% Critical: " + str(PlayerInventoryWeaponCrt[len(PlayerInventoryWeaponCrt) - 1])) 
                                    if Craft == "GSwo":
                                        PlayerInventoryWeapon.append(GreenProd[Select])
                                        PlayerInventoryWeaponAtk.append(random.randint(Product.index(GreenProd[Select]) * 10,Product.index(GreenProd[Select]) * 100))
                                        PlayerInventoryWeaponHit.append(random.randint(random.randint(50,75),random.randint(75,100)))
                                        PlayerInventoryWeaponCrt.append(random.randint(random.randint(10,25),random.randint(25,50)))
                                        PlayerInventoryWeaponDur.append(random.randint(Product.index(GreenProd[Select]) * 50,Product.index(GreenProd[Select]) * 100))
                                    elif Craft == "SSwo":
                                        PlayerInventoryWeapon.append(GreenProd[Select])
                                        PlayerInventoryWeaponAtk.append(random.randint(Product.index(GreenProd[Select]) * 10,Product.index(GreenProd[Select]) * 200))
                                        PlayerInventoryWeaponHit.append(random.randint(random.randint(0,25),random.randint(25,50)))
                                        PlayerInventoryWeaponCrt.append(random.randint(random.randint(0,10),random.randint(10,25)))
                                        PlayerInventoryWeaponDur.append(random.randint(Product.index(GreenProd[Select]) * 1,Product.index(GreenProd[Select]) * 10))
                                    elif Craft == "Lance":
                                        PlayerInventoryWeapon.append(GreenProd[Select])
                                        PlayerInventoryWeaponAtk.append(random.randint(Product.index(GreenProd[Select]) * 10,Product.index(GreenProd[Select]) * 100))
                                        PlayerInventoryWeaponHit.append(100)
                                        PlayerInventoryWeaponCrt.append(random.randint(random.randint(0,5),random.randint(5,10)))
                                        PlayerInventoryWeaponDur.append(random.randint(Product.index(GreenProd[Select]) * 10,Product.index(GreenProd[Select]) * 100))
                                    elif Craft == "LBow":
                                        PlayerInventoryWeapon.append(GreenProd[Select])
                                        PlayerInventoryWeaponAtk.append(random.randint(Product.index(GreenProd[Select]) * 25,Product.index(GreenProd[Select]) * 50))
                                        PlayerInventoryWeaponHit.append(random.randint(75,100))
                                        PlayerInventoryWeaponCrt.append(random.randint(random.randint(0,15),random.randint(15,30)))
                                        PlayerInventoryWeaponDur.append(random.randint(Product.index(GreenProd[Select]) * 500,Product.index(GreenProd[Select]) * 1000))
                                    elif Craft == "Mace":
                                        PlayerInventoryWeapon.append(GreenProd[Select])
                                        PlayerInventoryWeaponAtk.append(random.randint(Product.index(GreenProd[Select]) * 50,Product.index(GreenProd[Select]) * 100))
                                        PlayerInventoryWeaponHit.append(random.randint(1,50))
                                        PlayerInventoryWeaponCrt.append(random.randint(random.randint(0,15),random.randint(15,30)))
                                        PlayerInventoryWeaponDur.append(random.randint(Product.index(GreenProd[Select]) * 10,Product.index(GreenProd[Select]) * 100))
                                    elif Craft == "Axe":
                                        PlayerInventoryWeapon.append(GreenProd[Select])
                                        PlayerInventoryWeaponAtk.append(random.randint(Product.index(GreenProd[Select]) * 100,Product.index(GreenProd[Select]) * 250))
                                        PlayerInventoryWeaponHit.append(random.randint(1,33))
                                        PlayerInventoryWeaponCrt.append(random.randint(random.randint(0,15),random.randint(20,75)))
                                        PlayerInventoryWeaponDur.append(random.randint(Product.index(GreenProd[Select]) * 1,Product.index(GreenProd[Select]) * 100))
                                    elif Craft == "Shu":
                                        PlayerInventoryWeapon.append(GreenProd[Select])
                                        PlayerInventoryWeaponAtk.append(random.randint(Product.index(GreenProd[Select]) * 100,Product.index(GreenProd[Select]) * 300))
                                        PlayerInventoryWeaponHit.append(random.randint(1,25))
                                        PlayerInventoryWeaponCrt.append(random.randint(random.randint(0,5),random.randint(5,10)))
                                        PlayerInventoryWeaponDur.append(random.randint(Product.index(GreenProd[Select]) * 10,Product.index(GreenProd[Select]) * 50))
                                    elif Craft == "SBow":
                                        PlayerInventoryWeapon.append(GreenProd[Select])
                                        PlayerInventoryWeaponAtk.append(random.randint(Product.index(GreenProd[Select]) * 100,Product.index(GreenProd[Select]) * 300))
                                        PlayerInventoryWeaponHit.append(random.randint(1,25))
                                        PlayerInventoryWeaponCrt.append(random.randint(50,75))
                                        PlayerInventoryWeaponDur.append(random.randint(Product.index(GreenProd[Select]) * 10,Product.index(GreenProd[Select]) * 50))
                                    elif Craft == "CBow":
                                        PlayerInventoryWeapon.append(GreenProd[Select])
                                        PlayerInventoryWeaponAtk.append(random.randint(Product.index(GreenProd[Select]) *500,Product.index(GreenProd[Select]) * 1500))
                                        PlayerInventoryWeaponHit.append(random.randint(95,100))
                                        PlayerInventoryWeaponCrt.append(100)
                                        PlayerInventoryWeaponDur.append(random.randint(Product.index(GreenProd[Select]) * 1000,Product.index(GreenProd[Select]) * 5000))
                    elif keyboard.is_pressed("2"):  #Forge Code
                        os.system("cls")
                        print("You can improve a Weapon/Armor here\n\n1) Improve Weapons\n2) Improve Armor\nQ) Leave")
                        time.sleep(1)
                        Loop0 = 1 
                        while Loop0 == 1:
                            if keyboard.is_pressed("1"):    #Weapons
                                TempInt = 0
                                while TempInt <= len(PlayerInventoryWeapon) - 1:
                                    print(str(TempInt) + ") " + str(PlayerInventoryWeapon[TempInt]) + " - Requires: " + str(round(int(PlayerInventoryWeaponAtk[TempInt] + PlayerInventoryWeaponDur[TempInt]))) + " gold")
                                    TempInt = TempInt + 1
                                Loop1 = 1
                                while Loop1 == 1:
                                    TempInt = input("\nSelect a number in brackets to improve it for that ammount of gold (or type leave to leave)\n")
                                    if TempInt == "leave":
                                        WorldGeneration()
                                    try:
                                        TempInt = int(TempInt)
                                        Testvar = PlayerInventoryWeapon[TempInt]
                                        Testvar = Testvar
                                    except:
                                        print("This ID is invalid, make sure it's in brackets and a number")
                                    else:
                                        if PlayerInfo[9] >= int(PlayerInventoryWeaponAtk[TempInt] + PlayerInventoryWeaponDur[TempInt]):
                                            PlayerInfo[9] = PlayerInfo[9] - int(PlayerInventoryWeaponAtk[TempInt] + PlayerInventoryWeaponDur[TempInt])
                                            Loop1 = 0
                                        else:
                                            print("You dont have enough gold.")

                                PlayerAchivements[13] = 1
                                PlayerInventoryWeaponAtk[TempInt] = int(PlayerInventoryWeaponAtk[TempInt]  + 1) * 2
                                PlayerInventoryWeaponDur[TempInt] = int(PlayerInventoryWeaponDur[TempInt] + 1) * 2
                                Loop0 = 0
                                print("Improved " + str(PlayerInventoryWeapon[TempInt]))
                                time.sleep(1.5)
                                World()
                            elif keyboard.is_pressed("2"):    #Armor
                                TempInt = 0
                                while TempInt <= len(PlayerInventoryArmour) - 1:
                                    print(str(TempInt) + ") " + str(PlayerInventoryArmour[TempInt]) + " - Requires: " + str(round(int(PlayerInventoryArmourDef[TempInt] + PlayerInventoryArmourDur[TempInt]))) + " gold")
                                    TempInt = TempInt + 1
                                Loop1 = 1
                                while Loop1 == 1:
                                    TempInt = input("\nSelect a number in brackets to improve it for that ammount of gold (or type leave to leave)\n")
                                    if TempInt == "leave":
                                        WorldGeneration()
                                    try:
                                        TempInt = int(TempInt)
                                        Test = PlayerInventoryArmour[TempInt]
                                    except:
                                        print("This ID is invalid, make sure it's in brackets and a number")
                                    else:
                                        if PlayerInfo[9] >= int(PlayerInventoryArmourDef[TempInt] + PlayerInventoryArmourDur[TempInt]):
                                            PlayerInfo[9] = PlayerInfo[9] - int(PlayerInventoryArmourDef[TempInt] + PlayerInventoryArmourDur[TempInt])
                                            Loop1 = 0
                                        else:
                                            print("You dont have enough gold.")

                                PlayerAchivements[13] = 1
                                PlayerInventoryArmourDef[TempInt] = int(PlayerInventoryArmourDef[TempInt]  + 1) * 2
                                PlayerInventoryArmourDur[TempInt] = int(PlayerInventoryArmourDur[TempInt] + 1) * 2
                                Loop0 = 0
                                print("Improved " + str(PlayerInventoryArmour[TempInt]))
                                time.sleep(1.5)
                                World()
                            elif keyboard.is_pressed("Q"):
                                WorldGeneration()
                    elif keyboard.is_pressed("Q"):
                        WorldGeneration()
            elif TerrainType == 4:  # Trader Outpost
                Loop1 = 1
                while Loop1 == 1:
                    TempInt = 0
                    GreenText = [""]
                    while TempInt <= int(len(WorldDataTradeProd)-1):
                        if WorldDataTradeProd[TempInt] in PlayerInventory and PlayerInventoryAmmount[PlayerInventory.index(WorldDataTradeProd[TempInt])] > 0:
                            GreenText.append(WorldDataTradeProd[TempInt])
                            print(str(int(len(GreenText)-1)) + ") " + str(WorldDataTradeProd[TempInt]) + "   sells for: " + str(WorldDataTradePrice[TempInt]) + " gold      You have: " + str(PlayerInventoryAmmount[PlayerInventory.index(WorldDataTradeProd[TempInt])]))
                            TempInt = TempInt + 1
                        else:
                            TempInt = TempInt + 1

                    Loop2 = 1
                    while Loop2 == 1:
                        print("Type the number in brackets then press enter to sell one of that item.\nPress 0  to leave")
                        TempInt = input()
                        try:
                            TempInt = int(TempInt)
                            testvar = GreenText[TempInt]
                        except:
                            print("That ID is invalid.\nMake sure that the number has no spaces,")
                        else:
                            TempInt = int(TempInt)
                            Loop2 = 0
                    
                    if TempInt == 0:
                        WorldGeneration()
                    PlayerAchivements[10] = 1
                    if PlayerInventoryAmmount[PlayerInventory.index(GreenText[TempInt])] - 1 <= 0:
                        PlayerInventoryAmmount.pop(PlayerInventory.index(GreenText[TempInt]))
                        PlayerInventory.pop(PlayerInventory.index(GreenText[TempInt]))
                    else:
                        PlayerInventoryAmmount[PlayerInventory.index(GreenText[TempInt])] = PlayerInventoryAmmount[PlayerInventory.index(GreenText[TempInt])] - 1
                    
                    PlayerInfo[9] = PlayerInfo[9] + WorldDataTradePrice[WorldDataTradeProd.index(GreenText[TempInt])]
                    print("Sold 1 x " + str(GreenText[TempInt]) + " for " + str(WorldDataTradePrice[WorldDataTradeProd.index(GreenText[TempInt])]) + " Gold.")
                    time.sleep(1)
                    os.system("cls")
            elif TerrainType == 5:  # Dungeons
                PlayerAchivements[8] = 1
                DungeonData = [random.randint(1,PlayerInfo[7] * 10),random.randint(1,4),0,0,0]
                Dungeon()
            elif TerrainType == 6:  # Legendary Forge
                print("You seem to be able to forge weapons of magnificent power here.\nTo craft the weapons here you need to kill gods.")
                TempInt = 0
                while TempInt <= len(WorldDataLegendsForgeProd) - 1:
                    print(str(TempInt) + ") " + str(WorldDataLegendsForgeProd[TempInt]) + " - Requires " + str(WorldDataLegendsForgeAmm[TempInt]) + " Legends gems") 
                    TempInt = TempInt  + 1
                Loop0 = 1
                while Loop0 == 1:
                    TempInt = input("\nSelect a number in brackets, if you have enough legendary gems you will craft it (Type leave to leave)\n")
                    if TempInt == "leave":
                        WorldGeneration
                    try:
                        TempInt = int(TempInt)
                        Test = WorldDataLegendsForgeProd[TempInt]
                    except:
                        print("Thats no a valid ID (Make sure its a number)") 
                    else:
                        if "Legendary Gem" in PlayerInventory:
                            if PlayerInventoryAmmount[PlayerInventory.index("Legendary Gem")] >= WorldDataLegendsForgeAmm[TempInt]:
                                TempInt = int(TempInt)
                                Loop0 = 0
                            else:
                                print("You don't enough Legendary Gems")
                        else:
                            print("You don't have any Legendary Gems!")
                            WorldGeneration()
                
                print("Crafted " + str(WorldDataLegendsForgeProd[TempInt]))
                PlayerInventoryAmmount[PlayerInventory.index("Legendary Gem")] = PlayerInventoryAmmount[PlayerInventory.index("Legendary Gem")] - WorldDataLegendsForgeAmm[TempInt]
                PlayerInventoryWeapon.append(WorldDataLegendsForgeProd[TempInt])
                PlayerInventoryWeaponHit.append(100)
                PlayerInventoryWeaponCrt.append(100)
                if TempInt == 0:
                    PlayerInventoryWeaponAtk.append(random.randint(10000,100000))
                    PlayerInventoryWeaponDur.append(random.randint(5000,50000))
                elif TempInt == 1:
                    PlayerInventoryWeaponAtk.append(random.randint(1000,10000))
                    PlayerInventoryWeaponDur.append(random.randint(500,5000))
                elif TempInt == 2:
                    PlayerInventoryWeaponAtk.append(random.randint(5000,25000))
                    PlayerInventoryWeaponDur.append(random.randint(10,1000))
                elif TempInt == 3:
                    PlayerInventoryWeaponAtk.append(random.randint(5000,25000))
                    PlayerInventoryWeaponDur.append(random.randint(1000,10000))
                elif TempInt == 4:
                    PlayerInventoryWeaponAtk.append(random.randint(5000,50000))
                    PlayerInventoryWeaponDur.append(random.randint(1000,10000))
                elif TempInt == 5:
                    PlayerInventoryWeaponAtk.append(random.randint(5000,50000))
                    PlayerInventoryWeaponDur.append(random.randint(10000,100000))
                elif TempInt == 6:
                    PlayerInventoryWeaponAtk.append(random.randint(50000,5000000))
                    PlayerInventoryWeaponDur.append(random.randint(100,100000))
                elif TempInt == 7:
                    PlayerInventoryWeaponAtk.append(random.randint(1000,10000))
                    PlayerInventoryWeaponDur.append(random.randint(100,10000))
                elif TempInt == 8:
                    PlayerInventoryWeaponAtk.append(random.randint(1000,10000))
                    PlayerInventoryWeaponDur.append(random.randint(1000,10000))
                elif TempInt == 9:
                    PlayerInventoryWeaponAtk.append(random.randint(1000,10000))
                    PlayerInventoryWeaponDur.append(random.randint(1000,10000))
                
                PlayerAchivements[14] = 1
                os.remove(os.path.dirname(os.path.abspath(__file__)) + "\\WorldData\\X" + str(PlayerInfo[2]) + " Y" + str(PlayerInfo[3]) + ".txt")
                WorldGeneration()
            elif TerrainType == 7:  # Shady shop
                os.system("cls")
                print("You are at a strange shop\nAs you enter, you see lots of special pristinely-cut crystals\n\nYour gold: "  + str(PlayerInfo[9]) + "\n1) Health Crystal\n2) Defence Crystal\n3) Attack Crystal\nQ) Leave\n\nThe shopkeeper tells you that each crystal will boost your stats perminantly for 500 gold")
                time.sleep(1.5)
                Loop1 = 1
                while Loop1 == 1:#hp,5atk,def
                    if keyboard.is_pressed("1") and PlayerInfo[9] >= 500:
                        if PlayerInfo[9] >= 500: 
                            PlayerInfo[4] = PlayerInfo[4] + random.randint(20,50)
                            Loop1 = 0
                        else:
                            print("You don't have enough gold")
                    elif keyboard.is_pressed("2") and PlayerInfo[9] >= 500:
                        if PlayerInfo[9] >= 500:
                            PlayerInfo[5] = PlayerInfo[5] + random.randint(20,50)
                            Loop1 = 0
                        else:
                            print("You don't have enough gold")
                    elif keyboard.is_pressed("3"):
                        if PlayerInfo[9] >= 500:
                            PlayerInfo[6] = PlayerInfo[6] + random.randint(20,50)
                            Loop1 = 0
                        else:
                            print("You don't have enough gold")
                    elif keyboard.is_pressed("Q"):
                        os.remove(os.path.dirname(os.path.abspath(__file__)) + "\\WorldData\\X" + str(PlayerInfo[2]) + " Y" + str(PlayerInfo[3]) + ".txt")
                        WorldGeneration()
                PlayerInfo[9] = PlayerInfo[9] - 500
                os.remove(os.path.dirname(os.path.abspath(__file__)) + "\\WorldData\\X" + str(PlayerInfo[2]) + " Y" + str(PlayerInfo[3]) + ".txt")
                PlayerAchivements[1] = 1
                print("Suddenly the shop vanishes!")
                time.sleep(1.5)
                WorldGeneration()
            elif TerrainType == 8:  # Noticeboard
                print("You read a post on the notice board")
                time.sleep(1)
                if random.randint(1,2) == 1:    #Collect Quest (Can find in terrains)
                    TempInt = random.randint(0,len(WorldDataResource) - 1)
                    PlayerQuestName.append(str("Collect " + str(WorldDataResource[TempInt])))
                    PlayerQuestReqRes.append(str(WorldDataResource[TempInt]))
                    PlayerQuestReqAmm.append(random.randint(1,10))
                else:
                    TempInt = random.randint(0,len(WorldDataEnemyDrop) - 1)
                    PlayerQuestName.append(str("Kill monsters to collect " + str(WorldDataEnemyDrop[TempInt])))
                    PlayerQuestReqRes.append(str(WorldDataEnemyDrop[TempInt]))
                    PlayerQuestReqAmm.append(random.randint(1,10))
                if random.randint(1,2) == 1:
                    PlayerQuestRewardType.append(1)
                else:
                    PlayerQuestRewardType.append(2)
                os.remove(os.path.dirname(os.path.abspath(__file__)) + "\\WorldData\\X" + str(PlayerInfo[2]) + " Y" + str(PlayerInfo[3]) + ".txt")
                WorldGeneration()
        elif keyboard.is_pressed("8") and WorldDataProffessionData[Terrain] > 0: # Proffessions
            if WorldDataProffessionData[Terrain] == 1:      #fishing
                print("You started fishing")
                time.sleep(random.randint(1,7))
                if random.randint(1,4) == 1:
                    print("You caught a fish!")
                    PlayerAchivements[9] = 1
                    if "Fish" in PlayerInventory:
                        PlayerInventoryAmmount[PlayerInventory.index("Fish")] = PlayerInventoryAmmount[PlayerInventory.index("Fish")] + 1
                    else:
                        PlayerInventory.append("Fish")
                        PlayerInventoryAmmount.append(1)
                else:
                    print("You caught nothing.")
                time.sleep(1)
                World()
            elif WorldDataProffessionData[Terrain] == 2:    #Logging
                print("You started cutting down trees.")
                time.sleep(random.randint(1,7))
                if random.randint(1,4) == 1:
                    PlayerAchivements[11] = 1
                    print("You got some useable logs!")
                    if "Fish" in PlayerInventory:
                        PlayerInventoryAmmount[PlayerInventory.index("Fish")] = PlayerInventoryAmmount[PlayerInventory.index("Fish")] + random.randint(1,5)
                    else:
                        PlayerInventory.append("Logs")
                        PlayerInventoryAmmount.append(random.randint(1,5))
                else:
                    print("None of the wood is usable.")
                time.sleep(1)
                World()

def SaveLoad(): 
    global PlayerInfo
    global BattleLog
    global PlayerInventory
    global PlayerInventoryAmmount
    global PlayerInventoryArmourDur
    global PlayerInventoryArmour
    global PlayerInventoryArmourDef
    global PlayerInventoryWeapon
    global PlayerInventoryWeaponAtk
    global PlayerInventoryWeaponDur
    global PlayerInventoryWeaponCrt
    global PlayerInventoryWeaponHit
    global PlayerCurrentStats
    global PlayerMagic
    global PlayerMagicType
    global PlayerMagicValue
    global PlayerMagicCost
    global FastTravelY
    global FastTravelX
    global Log

    Log.append("Log menu")
    os.system("cls")
    if Save == 0:
        print("1) Save\n2) Load\nQ) Go Back")
        Loop = 1
        while Loop == 1:
            if keyboard.is_pressed("1"):
                Mode = 1
                Loop = 2
            elif keyboard.is_pressed("2"):
                Mode = 2
                Loop = 2
            elif keyboard.is_pressed("Q"):
                WorldGeneration()
            
    elif Save == 2:
        Mode = 2

    print("Select a slot (1-5)")
    time.sleep(1)
    A = 1
    while A == 1:
        if keyboard.is_pressed("1"):
            SlotNo = "Slot1"
            A = 0
        elif keyboard.is_pressed("2"):
            SlotNo = "Slot2"
            A = 0
        elif keyboard.is_pressed("3"):
            SlotNo = "Slot3"
            A = 0
        elif keyboard.is_pressed("4"):
            SlotNo = "Slot4"
            A = 0
        elif keyboard.is_pressed("5"):
            SlotNo = "Slot5"
            A = 0

    if Mode == 1: # Save
        destination = os.path.dirname(os.path.abspath(__file__)) + "\\PlayerData\\" + SlotNo + "\\PlayerMagicCost.json"
        with open(destination, "w+") as file:
            json.dump(PlayerMagicCost, file)

        destination = os.path.dirname(os.path.abspath(__file__)) + "\\PlayerData\\" + SlotNo + "\\PlayerMagicValue.json"
        with open(destination, "w+") as file:
            json.dump(PlayerMagicValue, file)

        destination = os.path.dirname(os.path.abspath(__file__)) + "\\PlayerData\\" + SlotNo + "\\PlayerMagicType.json"
        with open(destination, "w+") as file:
            json.dump(PlayerMagicType, file)

        destination = os.path.dirname(os.path.abspath(__file__)) + "\\PlayerData\\" + SlotNo + "\\PlayerMagic.json"
        with open(destination, "w+") as file:
            json.dump(PlayerMagic, file)

        destination = os.path.dirname(os.path.abspath(__file__)) + "\\PlayerData\\" + SlotNo + "\\PlayerCurrentStats.json"
        with open(destination, "w+") as file:
            json.dump(PlayerCurrentStats, file)

        destination = os.path.dirname(os.path.abspath(__file__)) + "\\PlayerData\\" + SlotNo + "\\PlayerInventoryWeaponHit.json"
        with open(destination, "w+") as file:
            json.dump(PlayerInventoryWeaponHit, file)

        destination = os.path.dirname(os.path.abspath(__file__)) + "\\PlayerData\\" + SlotNo + "\\PlayerInventoryWeaponCrt.json"
        with open(destination, "w+") as file:
            json.dump(PlayerInventoryWeaponCrt, file)

        destination = os.path.dirname(os.path.abspath(__file__)) + "\\PlayerData\\" + SlotNo + "\\PlayerInventoryWeaponDur.json"
        with open(destination, "w+") as file:
            json.dump(PlayerInventoryWeaponDur, file)

        destination = os.path.dirname(os.path.abspath(__file__)) + "\\PlayerData\\" + SlotNo + "\\PlayerInventoryWeaponAtk.json"
        with open(destination, "w+") as file:
            json.dump(PlayerInventoryWeaponAtk, file)

        destination = os.path.dirname(os.path.abspath(__file__)) + "\\PlayerData\\" + SlotNo + "\\PlayerInventoryWeapon.json"
        with open(destination, "w+") as file:
            json.dump(PlayerInventoryWeapon, file)

        destination = os.path.dirname(os.path.abspath(__file__)) + "\\PlayerData\\" + SlotNo + "\\PlayerInventoryArmourDef.json"
        with open(destination, "w+") as file:
            json.dump(PlayerInventoryArmourDef, file)

        destination = os.path.dirname(os.path.abspath(__file__)) + "\\PlayerData\\" + SlotNo + "\\PlayerInventoryArmourDur.json"
        with open(destination, "w+") as file:
            json.dump(PlayerInventoryArmourDur, file)

        destination = os.path.dirname(os.path.abspath(__file__)) + "\\PlayerData\\" + SlotNo + "\\PlayerInventoryArmour.json"
        with open(destination, "w+") as file:
            json.dump(PlayerInventoryArmour, file)

        destination = os.path.dirname(os.path.abspath(__file__)) + "\\PlayerData\\" + SlotNo + "\\PlayerInventoryAmmount.json"
        with open(destination, "w+") as file:
            json.dump(PlayerInventoryAmmount, file)

        destination = os.path.dirname(os.path.abspath(__file__)) + "\\PlayerData\\" + SlotNo + "\\PlayerInventory.json"
        with open(destination, "w+") as file:
            json.dump(PlayerInventory, file)

        destination = os.path.dirname(os.path.abspath(__file__)) + "\\PlayerData\\" + SlotNo + "\\PlayerInfo.json"
        with open(destination, "w+") as file:
            json.dump(PlayerInfo, file)

        destination = os.path.dirname(os.path.abspath(__file__)) + "\\PlayerData\\" + SlotNo + "\\FastTravelY.json"
        with open(destination, "w+") as file:
            json.dump(FastTravelY, file)

        destination = os.path.dirname(os.path.abspath(__file__)) + "\\PlayerData\\" + SlotNo + "\\FastTravelX.json"
        with open(destination, "w+") as file:
            json.dump(FastTravelY, file)

        print("Save complete!")
        time.sleep(2.5)
        WorldGeneration()

    elif Mode == 2:

        destination = os.path.dirname(os.path.abspath(__file__)) + "\\PlayerData\\" + str(SlotNo) + "\\PlayerInfo.json"
        with open(destination) as file:
            PlayerInfo = json.load(file)

        destination = os.path.dirname(os.path.abspath(__file__)) + "\\PlayerData\\" + str(SlotNo) + "\\PlayerInventory.json"
        with open(destination) as file:
            PlayerInventory = json.load(file)
            
        destination = os.path.dirname(os.path.abspath(__file__)) + "\\PlayerData\\" + str(SlotNo) + "\\PlayerInventoryAmmount.json"
        with open(destination) as file:
            PlayerInventoryAmmount = json.load(file)

        destination = os.path.dirname(os.path.abspath(__file__)) + "\\PlayerData\\" + str(SlotNo) + "\\PlayerInventoryArmour.json"
        with open(destination) as file:
            PlayerInventoryArmour = json.load(file)            

        destination = os.path.dirname(os.path.abspath(__file__)) + "\\PlayerData\\" + str(SlotNo) + "\\PlayerInventoryArmourDur.json"
        with open(destination) as file:
            PlayerInventoryArmourDur = json.load(file)

        destination = os.path.dirname(os.path.abspath(__file__)) + "\\PlayerData\\" + str(SlotNo) + "\\PlayerInventoryArmourDef.json"
        with open(destination) as file:
            PlayerInventoryArmourDef = json.load(file)

        destination = os.path.dirname(os.path.abspath(__file__)) + "\\PlayerData\\" + str(SlotNo) + "\\PlayerInventoryWeapon.json"
        with open(destination) as file:
            PlayerInventoryWeapon = json.load(file)

        destination = os.path.dirname(os.path.abspath(__file__)) + "\\PlayerData\\" + str(SlotNo) + "\\PlayerInventoryWeaponAtk.json"
        with open(destination) as file:
            PlayerInventoryWeaponAtk = json.load(file)

        destination = os.path.dirname(os.path.abspath(__file__)) + "\\PlayerData\\" + str(SlotNo) + "\\PlayerInventoryWeaponCrt.json"
        with open(destination) as file:
            PlayerInventoryWeaponCrt = json.load(file)

        destination = os.path.dirname(os.path.abspath(__file__)) + "\\PlayerData\\" + str(SlotNo) + "\\PlayerInventoryWeaponHit.json"
        with open(destination) as file:
            PlayerInventoryWeaponHit = json.load(file)

        destination = os.path.dirname(os.path.abspath(__file__)) + "\\PlayerData\\" + str(SlotNo) + "\\PlayerCurrentStats.json"
        with open(destination) as file:
            PlayerCurrentStats = json.load(file)

        destination = os.path.dirname(os.path.abspath(__file__)) + "\\PlayerData\\" + str(SlotNo) + "\\PlayerMagic.json"
        with open(destination) as file:
            PlayerMagic = json.load(file)

        destination = os.path.dirname(os.path.abspath(__file__)) + "\\PlayerData\\" + str(SlotNo) + "\\PlayerMagicType.json"
        with open(destination) as file:
            PlayerMagicType = json.load(file)

        destination = os.path.dirname(os.path.abspath(__file__)) + "\\\PlayerData\\" + str(SlotNo) + "\\PlayerMagicValue.json"
        with open(destination) as file:
            PlayerMagicValue = json.load(file)

        destination = os.path.dirname(os.path.abspath(__file__)) + "\\PlayerData\\" + str(SlotNo) + "\\PlayerMagicCost.json"
        with open(destination) as file:
            PlayerMagicCost = json.load(file)

        destination = os.path.dirname(os.path.abspath(__file__)) + "\\PlayerData\\" + str(SlotNo) + "\\FastTravelY.json"
        with open(destination) as file:
            FastTravelY = json.load(file)

        destination = os.path.dirname(os.path.abspath(__file__)) + "\\PlayerData\\" + str(SlotNo) + "\\FastTravelX.json"
        with open(destination) as file:
            FastTravelX = json.load(file)

        print("Load complete!")
        time.sleep(2.5)
        WorldGeneration()

def Battle():
    global PlayerCurrentStats
    global PlayerInfo
    global Log
    global Dungeon
    global PlayerAchivements

    Log.append("Battle initalised")
    if DungeonData[4] != 1:
        EnemyMult = int(round(len(WorldDataEnemyName[Enemy[2]]) / random.randint(1,25)))
        if Enemy[0] >= 0:
            EnemyMult = EnemyMult + int(round(len(WorldDataEnemyPrefix[Enemy[1]]) / 10))
        if Enemy[3] >= 0:
            EnemyMult = EnemyMult + int(round(len(WorldDataEnemySuffix[Enemy[3]]) / 10))

        if EnemyMult > 1:
            EnemyMult = 2
    else:
        print("A powerful enemy appeared!")
        EnemyMult = random.randint(5,10)

    try:    #it crashes sometimes and i don't know why can @someone please help
        EnemyHP = random.randint(int(round(0.8 * PlayerInfo[4])),int(round(EnemyMult * PlayerInfo[4])))
        EnemyMAX = EnemyHP  # for display   
        EnemyATK = random.randint(round(0.8 * PlayerInfo[5]),round(EnemyMult * PlayerInfo[5]))
        EnemyDEF = random.randint(round(0.8 * PlayerInfo[6]),round(EnemyMult * PlayerInfo[6]))
    except:# Should Randint not do its job right it clones the players stats
        EnemyHP = PlayerInfo[4]
        EnemyMAX = EnemyHP
        EnemyATK = PlayerInfo[5]
        EnemyDEF = PlayerInfo[6]
    else:
        EnemyHP = random.randint(int(round(0.8 * PlayerInfo[4])),int(round(EnemyMult * PlayerInfo[4])))
        EnemyMAX = EnemyHP  # for display   
        EnemyATK = random.randint(round(0.8 * PlayerInfo[5]),round(EnemyMult * PlayerInfo[5]))
        EnemyDEF = random.randint(round(0.8 * PlayerInfo[6]),round(EnemyMult * PlayerInfo[6]))

    PlayerCurrentStats[1] = PlayerInfo[18]    #Maxes Mana
    Loop1 = 1

    while Loop1 == 1:#Battle Loop
        print("\n\nHP: " + str(PlayerCurrentStats[0]) + "/" + str(PlayerInfo[4]) + "         Mana: " + str(PlayerCurrentStats[1]) + "/" + str(PlayerInfo[18]) + "\nEnemy HP: " + str(EnemyHP) + "/" + str(EnemyMAX) + "\n\n1) Attack      2) Magic\n3) Defend      4) Run\n\n")
        Loop2 = 1
        time.sleep(1)
        while Loop2 == 1:   # Player Options
            Def = PlayerInfo[6]

            if keyboard.is_pressed("1"):    #10EquipedWeaponName,EquipedWeaponAttack,EquipedWeaponHit,EquipedWeaponCritical,EquipedWeaponDurabilty
                Attack = PlayerInfo[5] + PlayerInfo[11]

                if PlayerInfo[10] != "Hands":
                    PlayerInfo[14] = PlayerInfo[14] - random.randint(0,1)

                if PlayerInfo[14] >= 0 and random.randint(1,100) <= PlayerInfo[13] and PlayerInfo[10] != "Hands":
                    Attack = PlayerInfo[5]
                    print("You landed a critical hit.")

                if PlayerInfo[14] <= 0 and PlayerInfo[10] != "Hands" and random.randint(1,100) <= PlayerInfo[12] :#if any1 lands a critical miss message me
                    Attack = 0
                    print("Your attack missed.")

                Attack = Attack - EnemyDEF
                if Attack <= 0:
                    Attack = 0 #Prevents enemy being healed from a attack
                
                Loop2 = 0
            elif keyboard.is_pressed("2"):
                TempInt = 0
                PlayerAchivements[6] = 1
                while TempInt <= int(len(PlayerMagic)-1):
                    print(str(PlayerMagic[TempInt]) + "  Cost: " + str(PlayerMagicCost[TempInt]) + " Effect: " + str(PlayerMagicValue[TempInt]) + " " + str(PlayerMagicType[TempInt]) + " ID: " + str(TempInt))
                    TempInt = TempInt + 1
                Loop3 = 1
                while Loop3 == 1:
                    TempStr = input("Type an ID of a spell to cast, then press enter\n")
                    try:
                        TempStr = int(TempStr)
                        test = PlayerMagic[TempStr]
                        test = test
                    except:
                        print("That was a invalid ID, make sure the ID is valid and is a number")
                    else:
                        TempStr = int(TempStr)
                        if PlayerCurrentStats[1] - PlayerMagicCost[TempStr] <= 0:
                            print("Not enough mana")
                        else:
                            Loop2 = 0
                            Loop3 = 0
                            Attack = 0 
                            PlayerCurrentStats[1] = PlayerCurrentStats[1] - PlayerMagicCost[TempStr]
                            if PlayerMagicType[TempStr].upper() == "DAMAGE":
                                print("\nYou casted " + str(PlayerMagic[TempStr]))
                                Attack = PlayerMagicValue[TempStr]
                            elif PlayerMagicType[TempStr].upper() == "HEAL":
                                print("\nYou casted " + str(PlayerMagic[TempStr]) + "\nHealed " +  str(PlayerMagicValue[TempStr]) + " HP   (" + str(PlayerCurrentStats[0]) + " -> " + str(int(PlayerCurrentStats[0] + PlayerMagicValue[TempStr])) + ")")
                                PlayerCurrentStats[0] = PlayerCurrentStats[0] + PlayerMagicValue[TempStr]   
                                if PlayerInfo[4] < PlayerCurrentStats[0]:
                                    PlayerCurrentStats[0] = PlayerInfo[4]

            elif keyboard.is_pressed("3"):
                Def = Def * 2
                Attack = 0
                PlayerAchivements[5] = 1
                Loop2 = 0
            elif keyboard.is_pressed("4"):
                Attack = 0
                if random.randint(0,1) == 0:
                    World()
                else:
                    print("Couldn't run!")
                    Loop2 = 0
        
        EnemyAttack = EnemyATK + random.randint(-10 * PlayerInfo[7],10 * PlayerInfo[7])
        EnemyAttack = EnemyAttack - Def
        EnemyHP = EnemyHP - Attack
        if EnemyAttack <= 0:
            EnemyAttack = 0
        PlayerCurrentStats[0] = PlayerCurrentStats[0] - EnemyAttack

        print("Enemy did " + str(EnemyAttack) + " damage\nYou did " + str(Attack) + " damage")

        if Weather == 3 and PlayerInfo[14] != "Nothing":
            print("You also took " + str(round(PlayerInfo[4] / 5)) + " from the hot weather!")
            PlayerCurrentStats[0] = PlayerCurrentStats[0] - round(PlayerInfo[4] / 5)

        if Weather == 4 and PlayerInfo[14] == "Nothing":
            print("You also took " + str(round(PlayerInfo[4] / 5)) + " from the cold weather!")
            PlayerCurrentStats[0] = PlayerCurrentStats[0] - round(PlayerInfo[4] / 5)

        if EnemyHP <= 0:
            #PlayerInfo  = [0,0,0,0,50,25,5,1,0,500,"Hands",0,100,0,0,"Nothing",0,0,50,0] #0name,difficulty,x,y,hp,5atk,def,level,exp,gold,10EquipedWeaponName,EquipedWeaponAttack,EquipedWeaponHit,EquipedWeaponCritical,EquipedWeaponDurabilty,EquipedArmorName,EquippedArmourDefence,EquipedArmorDurabilty,Mana,Monolith Spell count (19)
            PlayerInfo[8] = PlayerInfo[8] + random.randint(0,250) #XP
            PlayerInfo[9] = PlayerInfo[9] + random.randint(random.randint(1,250),300) # Gold
            PlayerInfo[22] = PlayerInfo[22] + random.randint(0,2)
            print("You got XP, Gold and some reputation for killing the monster!")
            PlayerCurrentStats[0] = PlayerInfo[4] - random.randint(1,10)
            if random.randint(1,5) == 5:
                print("The enemy dropped a " + str(WorldDataEnemyDrop[Enemy[1]]) + ".")
                if WorldDataEnemyDrop[Enemy[1]] in PlayerInventory:
                    PlayerInventoryAmmount[WorldDataEnemyDrop[Enemy[1]]] = PlayerInventoryAmmount[WorldDataEnemyDrop[Enemy[1]]] + random.randint(1,2)
                else:
                    PlayerInventory.append(WorldDataEnemyDrop[Enemy[1]])
                    PlayerInventoryAmmount.append(random.randint(1,2))

            if DungeonData[4] == 1:
                print("You got bonus EXP and Gold for defeating the boss")
                PlayerInfo[8] = PlayerInfo[8] + random.randint(1000,5000) #XP
                PlayerInfo[9] = PlayerInfo[9] + random.randint(1000,10000) # Gold
            if PlayerInfo[8] > PlayerInfo[7] * 1000:
                print("You Leveled up\nYour stats have improved.")
                PlayerInfo[7] = PlayerInfo[7] + 1
                PlayerInfo[8] = 0
                PlayerInfo[4] = PlayerInfo[4] + random.randint(1,25)
                PlayerInfo[5] = PlayerInfo[5] + random.randint(1,25)
                PlayerInfo[6] = PlayerInfo[6] + random.randint(1,25)
            else:
                print("")
            time.sleep(2.5)
            if PlayerInfo[7] == 25:
                PlayerInfo[7] = PlayerInfo[7] + 1
                PlayerAchivements[16] = 1
                Battle()
            if DungeonData[4] == 1:
                DungeonData[4] = 1

                Dungeon()
            else:
                World()
        elif PlayerCurrentStats[0] <= 0:
            Death()

def Death():
    global Log
    global Save
    global PlayerInfo
    Log.append("Player died")
    print(Fore.RED + "You died." + Fore.RESET + "\n\n1) Load a previous save\n2) Go go main menu\n3) Respawn\n4) Quit")
    Loop1 = 1
    time.sleep(1)
    while Loop1 == 1:
        if keyboard.is_pressed("1"):
            Save = 2
            SaveLoad()
        elif keyboard.is_pressed("2"):
            Intialise()
        elif keyboard.is_pressed("3"):
            PlayerInfo[2] = PlayerInfo[20]
            PlayerInfo[3] = PlayerInfo[21]
            PlayerInfo[7] = 0
            PlayerInfo[8] = 0
            PlayerCurrentStats[0] = PlayerInfo[4]
            WorldGeneration()
        elif keyboard.is_pressed("4"):
            exit()

def Dungeon():
    global DungeonData
    global PlayerInfo
    global PlayerAchivements

    os.system("cls")
    Loop0 = 1
    while Loop0 == 1:
        if DungeonData[0] <= 0:
            print("Escaping from the dungeon seems to have made you stronger")
            PlayerInfo[4] = PlayerInfo[4] + random.randint(1,20)
            PlayerInfo[5] = PlayerInfo[5] + random.randint(1,20)
            PlayerInfo[6] = PlayerInfo[6] + random.randint(1,20)
            time.sleep(1)
            os.remove(os.path.dirname(os.path.abspath(__file__)) + "\\WorldData\\X" + str(PlayerInfo[2]) + " Y" + str(PlayerInfo[3]) + ".txt")
            DungeonData = [0,0,0,0,0]
            WorldGeneration()
        if random.randint(1,2) == 1:
            if DungeonData[1] == 1:
                print("A light emminates in front of you.")
            elif DungeonData[1] == 2:
                print("A light illuminates behind you.")
        print("You are in a dungeon\nA Monster lurks in the darkness\n1) Move    2) Battle")
        print(str(DungeonData))
        time.sleep(1)
        Loop1 = 1
        while Loop1 == 1:
            if keyboard.is_pressed("1"):
                print("\nSelect a direction to move\n         (1)\n        North\n(4) West     East (2)\n        South\n         (3)")
                Loop2 = 1
                time.sleep(1)
                while Loop2 == 1:
                    if keyboard.is_pressed("1") or keyboard.is_pressed("2"):
                        if DungeonData[1] == 1:
                            print("It seems you moved in the right direction")
                            time.sleep(1)
                            DungeonData[0] = DungeonData[0] - 1
                        Loop2 = 0
                        Loop1 = 0
                    elif keyboard.is_pressed("3") or keyboard.is_pressed("4"):
                        if DungeonData[1] == 3:
                            print("It seems you moved in the right direction")
                            time.sleep(1)
                            DungeonData[0] = DungeonData[0] - 1
                        Loop2 = 0
                        Loop1 = 0 
                DungeonData[1] = random.randint(1,2)
                Dungeon() 
            elif keyboard.is_pressed("2"):
                DungeonData[4] = 1
                Battle()


Intialise() #Starts the game after all functions are declared