import linecache
import os
import time
import urllib.request
import zipfile
from colorama import Fore, Back, Style, init
import keyboard
import random
init(convert=True)
#chess pieces!

SystemInfo  = ["Build Version: 1/2/2020","1.0"]
LatestVer   = "ERROR"
PlayerInfo  = [0,0,0,0,50,25,5,1,0,500,"Hands",0,100,0,0,"Nothing",0,0,50,0] #0name,difficulty,x,y,hp,5atk,def,level,exp,gold,10EquipedWeaponName,EquipedWeaponAttack,EquipedWeaponHit,EquipedWeaponCritical,EquipedWeaponDurabilty,EquipedArmorName,EquippedArmourDefence,EquipedArmorDurabilty,Mana,Monolith Spell count (19)
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
PlayerMagicValue = [0,10,25]   # Damage of spell
PlayerMagicCost  = [0,5,5]   # How much does the spell cost to cast

#WorldData Variables SHOULD NOT be modifyed instead unless its for a master branch (USE THE MOD API)
WorldDataTerrain            = ["in the grasslands","in the flatlands","in the mountains","in a town","in an abandoned town","near a volcano","on some hills","in a abandoned mine","in a valley","in a lake","in a beach","in a cave","in a taiga forest","in a swamp","in a forest","in a thick forest","on a hillside","on a cliffside","on some farmland","in a mesa","in the middle of a Desert","in a Oasis","inside of an abandoned cabin","on a Plateou","in snowy mountain","near a riverside"]
WorldDataTerrainColor       = ["GREEN","RESET","WHITE","RESET","RESET","RED","GREEN","WHITE","CYAN","BLUE","YELLOW","RESET","WHITE","GREEN","GREEN","GREEN","RESET","CYAN","YELLOW","YELLOW","YELLOW","BLUE","RESET","WHITE","WHITE","CYAN"]
WorldDataTerrainBrightness  = ["BRIGHT","NORMAL","BRIGHT","NORMAL","DIM","DIM","BRIGHT","DIM","BRIGHT","BRIGHT","NORMAL","DIM","BRIGHT","DIM","BRIGHT","DIM","DIM","DIM","BRIGHT","DIM","BRIGHT","DIM","DIM","BRIGHT","BRIGHT","DIM"]
WorldDataResource           = ["Apples","Bark","Berries","Blue Lilly Pads","Branches","Bundles of grass","Bundles of leaves","Bundles of wheat","Bushes","Cacti","Carrots","Dark wood logs","Emeralds","Fish","Flowers","Grass Fibers","Herbs","KG of Black Sand","KG of Sand","Lilly Pads","Litres of water","Magma Branches","Magma Logs","Magma stones","Moss","Mystical berries","Oak wood logs","Palm tree logs","Palm wood","Pink Lilly Pads","Potatoes","Redwood Branches","Redwood Logs","Seeds","Spruce Branches","Spruce logs"]
WorldDataResourceColor      = ["RED","WHITE","RED","BLUE","GREEN","GREEN","GREEN","YELLOW","WHITE","GREEN","YELLOW","WHITE","GREEN","CYAN","MAGENTA","GREEN","GREEN","WHITE","YELLOW","GREEN","BLUE","RED","RED","RED","GREEN","CYAN","RESET","YELLOW","YELLOW","MAGENTA","YELLOW","RED","RED","GREEN","CYAN","CYAN"]
WorldDataResourceBrightness = ["BRIGHT","DIM","BRIGHT","BRIGHT","DIM","DIM","BRIGHT","DIM","DIM","DIM","BRIGHT","DIM","BRIGHT","BRIGHT","BRIGHT","DIM","BRIGHT","DIM","DIM","DIM","BRIGHT","DIM","DIM","DIM","DIM","BRIGHT","BRIGHT","BRIGHT","BRIGHT","BRIGHT","DIM","DIM","NORMAL","NORMAL","DIM","DIM"]
WorldDataEnemyPrefix        = ["Angry","Armoured","Beserk","Crazed","Demonic","Enemy","Enraged","Fallen","Frenzied","Giant","Greater","Infested","Leaping","Lesser","Possessed","Skeleton"]
WorldDataEnemyName          = ["Archer","Artifact","Beast","Bull","Centaur","Demon","Dog","Elf","Fire","Fox","Giant","Goblin","God","Hunter","Ice","Madman","Ogre","Orc","Phantom","Rat","Relic","Robot","Skeleton","Soldier","Spider","Spirit","Troll","Villager","Warrior","Wolf","Zombie"]
WorldDataEnemySuffix        = ["Lord","Monster","King","Creature"]
WorldDataWeather            = ["Sunny","Cloudy","Hot","Cold","Windy"]
WorldDataMonolithSpell      = ["Heal I","Bolt","Risma","Aquious","Ignis","Terra","Heal II","Rarisma","Taifau","Odurzony","hladan","Tembung","Heal III"]#These are just words in other langauges
WorldDataMonolithSpellType  = ["HEAL","Damage","Damage","Damage","Damage","Damage","HEAL", "Damage","Damage", "Damage", "Damage","Damage",  "HEAL"]
WorldDataMonolithSpellValue = [10,20,25,25,35,30,30,50,60,50,80,100,100,250]
WorldDataMonolithSpellCost  =  [5,15,25,20,40,20,10,75,40,10,75,90,60,100]


def Intialise():    #Starts the game, Checks reqired modules are installed and runs AutoUpdate if enabled
    global SystemInfo
    global LatestVer

    try:    #Checks if modules are installed
        import keyboard
        import colorama
    except: #Tries to Auto-Install modules
        print("You are missing required modules,\nWould you like to attempt to Auto-Install them?\n\nThis may fail if you are not an admin.\n(Y/N)")
        Select = input()
        Loop = 1
        while Loop == 1:
            if str(Select.upper()) == "Y":
                os.system("pip install colorama keyboard")
                Loop = 0
            elif str(Select.upper()) == "N":
                input("Very well then,\nPress enter to close the program")
                exit()  #Terminates if declines to install
        try:
            import keyboard
            import colorama 
        except:
            input("Failed to Auto-Install required modules...\nPlease open a Command Prompt (Preferably as admin) and type the following command\npip install colorama keyboard\n\nPress enter to leave.")
            exit()

    print("Trying to check update servers...\n\nTired of seeing this?\nChange the autoupdater setting in Config.txt\nThis shouldn't take more than 30 seconds")
    TempStr = linecache.getline(os.path.dirname(os.path.abspath(__file__)) + "\\Config.txt",3)
    TempStr = TempStr.strip()
    if TempStr == "False":  #Checks if AutoUpdate is disabled if so then it goes to the menu
        LatestVer = "DISABLED"
        Menu()

    try:    #Tries to get check github
        urllib.request.urlretrieve("https://raw.githubusercontent.com/TMAltair/RougalikeRPG/master/metadata.txt",os.path.dirname(os.path.abspath(__file__)) + "\\meta.txt")
        LatestVer = str(linecache.getline(os.path.dirname(os.path.abspath(__file__)) + "\\meta.txt",3))
    except: #Upon any type of failure it skips AutoUpdate
        LatestVer = "Failed"
        Menu()
    LatestVer = LatestVer.strip()
    
    try: # Tries to delete meta.txt if it exists
        os.remove(os.path.dirname(os.path.abspath(__file__)) + "\\Data\\meta.txt")
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
                Menu()
    LatestVer = "Up to date"
    Menu()

def Menu(): #  Menu
    global LatestVer
    global PlayerInfo

    os.system("cls") #clears screen
    print("Rougealike RPG by TMAltair\n1) Play\n2) Load\nQ) Quit\n\nVersion " + str(SystemInfo[1]) + " (" + str(SystemInfo[0]) + ")")
    
    if LatestVer == "Failed": #If an error occurs prints this
        print("Could not talk to the AutoUpdate webpage.\nTo see if Rougealike has an update go to\nhttps://github.com/TMAltair/Roguealike/")
    elif LatestVer == "Declined": #If update is declined 
        print("Update available!\nPress U) to update!")
    elif LatestVer == "ERROR": #If auto update is not changed for some reason
        print("An Error occured in the update.")
    elif LatestVer == "DISABLED": # If autoupdate is disabled in the Config.txt
        print("AutoUpdate is disabled.")
    elif LatestVer == "GLOBALLY DISABLED":
        print("AutoUpdate is disabled globally for now.")
    Loop = 1
    while Loop == 1:
        if keyboard.is_pressed("1"):
            os.system("cls")
            PlayerInfo[0] = str(input("Enter a name: "))
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


            PlayerInfo[2] = 0   #X Coord
            PlayerInfo[3] = 0   #Y Coord 
            WorldGeneration()
        elif keyboard.is_pressed("2"):
            print()
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

    if os.path.exists(os.path.dirname(os.path.abspath(__file__)) + "\\WorldData\\X" + str(PlayerInfo[2]) + " Y" + str(PlayerInfo[3]) + ".txt"):  #Terrain that needs to be generated
        TerrainType = int(linecache.getline(os.path.dirname(os.path.abspath(__file__)) + "\\WorldData\\X" + str(PlayerInfo[2]) + " Y" + str(PlayerInfo[3]) + ".txt",1))
        
        if TerrainType == 0:    #For standards
            Terrain = int(linecache.getline(os.path.dirname(os.path.abspath(__file__)) + "\\WorldData\\X" + str(PlayerInfo[2]) + " Y" + str(PlayerInfo[3]) + ".txt",2))
        else:   #For non standard Terrains
            TerrainTypeMeta = int(linecache.getline(os.path.dirname(os.path.abspath(__file__)) + "\\WorldData\\X" + str(PlayerInfo[2]) + " Y" + str(PlayerInfo[3]) + ".txt",2))

        Resource = [int(linecache.getline(os.path.dirname(os.path.abspath(__file__)) + "\\WorldData\\X" + str(PlayerInfo[2]) + " Y" + str(PlayerInfo[3]) + ".txt",3)),int(linecache.getline(os.path.dirname(os.path.abspath(__file__)) + "\\WorldData\\X" + str(PlayerInfo[2]) + " Y" + str(PlayerInfo[3]) + ".txt",5)),int(linecache.getline(os.path.dirname(os.path.abspath(__file__)) + "\\WorldData\\X" + str(PlayerInfo[2]) + " Y" + str(PlayerInfo[3]) + ".txt",7)),int(linecache.getline(os.path.dirname(os.path.abspath(__file__)) + "\\WorldData\\X" + str(PlayerInfo[2]) + " Y" + str(PlayerInfo[3]) + ".txt",9))]
        ResourceAmmount = [int(linecache.getline(os.path.dirname(os.path.abspath(__file__)) + "\\WorldData\\X" + str(PlayerInfo[2]) + " Y" + str(PlayerInfo[3]) + ".txt",4)),int(linecache.getline(os.path.dirname(os.path.abspath(__file__)) + "\\WorldData\\X" + str(PlayerInfo[2]) + " Y" + str(PlayerInfo[3]) + ".txt",6)),int(linecache.getline(os.path.dirname(os.path.abspath(__file__)) + "\\WorldData\\X" + str(PlayerInfo[2]) + " Y" + str(PlayerInfo[3]) + ".txt",8)),int(linecache.getline(os.path.dirname(os.path.abspath(__file__)) + "\\WorldData\\X" + str(PlayerInfo[2]) + " Y" + str(PlayerInfo[3]) + ".txt",10))]
       
        if random.randint(1,5) > 0:
            Weather = random.randint(1,2)
        else:
            Weather = 0  
    else:   #Generates Terrain
        if random.randint(1,25) == 25: # 4% Chance 
            TerrainType = random.randint(1,4) # Terrain isn't needed to be generated
            TerrainTypeMeta = 0
        else:
            TerrainType = 0 # 0 is Normal Terrain
            Terrain  = random.randint(0,len(WorldDataTerrain)-1) # gets terrain
        Resource = [random.randint(-1,len(WorldDataResource)-1),random.randint(-10,len(WorldDataResource)-1),random.randint(-20,len(WorldDataResource)-1),random.randint(-30,len(WorldDataResource)-1)]
        ResourceAmmount = [random.randint(random.randint(1,5),random.randint(5,10)),random.randint(random.randint(1,5),random.randint(5,10)),random.randint(random.randint(1,5),random.randint(5,10)),random.randint(random.randint(1,5),random.randint(5,10))]
            
        WorldFile = open(os.path.dirname(os.path.abspath(__file__)) + "\\WorldData\\X" + str(PlayerInfo[2]) + " Y" + str(PlayerInfo[3]) + ".txt","w")
        if TerrainType == 0:
            WorldFile.write(str(TerrainType) + "\n" + str(Terrain) + "\n" + str(Resource[0]) + "\n" + str(ResourceAmmount[0]) +  "\n" + str(Resource[1]) + "\n" + str(ResourceAmmount[1]) + "\n" +  str(Resource[2]) + "\n" + str(ResourceAmmount[2]) + "\n" + str(Resource[3]) + "\n" + str(ResourceAmmount[3]))
        else:
            WorldFile.write(str(TerrainType) + "\n" + str(TerrainTypeMeta) + "\n" + str(Resource[0]) + "\n" + str(ResourceAmmount[0]) +  "\n" + str(Resource[1]) + "\n" + str(ResourceAmmount[1]) + "\n" +  str(Resource[2]) + "\n" + str(ResourceAmmount[2]) + "\n" + str(Resource[3]) + "\n" + str(ResourceAmmount[3]))
        WorldFile.close()

        if random.randint(1,5) > 0:
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

    os.system("cls")
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

    if TerrainType == 0:
        print(Fore.__getattribute__(WorldDataTerrainColor[Terrain]) + Style.__getattribute__(WorldDataTerrainBrightness[Terrain]) + "You are " + str(WorldDataTerrain[Terrain]) + ".")
    else:
        if TerrainType == 1 and TerrainTypeMeta == 0:
            print("You are at a monolith.")
        elif TerrainType == 1 and TerrainTypeMeta == 1:
            print("You are at a old monolith.")
        elif TerrainType == 2 and TerrainTypeMeta == 0:
            print("You are at a cave.")
        elif TerrainType == 2 and TerrainTypeMeta == 1:
            print("You are at a collasped cave.")
        elif TerrainType == 3 and TerrainTypeMeta == 0:
            print("You are at a village.")
        elif TerrainType == 3 and TerrainTypeMeta == 1:
            print("You are at an abandoned village.")
        elif TerrainType == 4 and TerrainTypeMeta == 0:
            print("You are at a trader outpost.")
        elif TerrainType == 4 and TerrainTypeMeta == 1:
            print("You are at a destroyed outpost.")

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

    if Weather > 0:
        print(Fore.YELLOW + "It is also very " + WorldDataWeather[Weather] + "." + Fore.RESET)

    print(Fore.RESET + "\n\n1) Battle    2) Move      3) Collect Items\n4) Character 5) Save/Load 6) Quit")
    if TerrainType == 1 and TerrainTypeMeta == 0:
        print("7) Use Monolith")
    elif TerrainType == 2 and TerrainTypeMeta == 0:
        print("7) Mine")
    elif TerrainType == 3 and TerrainTypeMeta == 0:
        print("7) Enter Village")
    elif TerrainType == 4 and TerrainTypeMeta == 0:
        print("7) Trade")
    
    Loop = 1
    time.sleep(1)
    while Loop == 1:
        if keyboard.is_pressed("1"):   # Battle
            if Enemy[0] == 1:
                print("There's no enemy to battle!")
                time.sleep(2.5)
                World()
            else:
                Battle()
        elif keyboard.is_pressed("2"): # Movement
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
            TempInt = 0
            while TempInt <= int(len(Resource) - 1): #Just in case resource gets increased at some point
                print("loop")
                if Resource[TempInt] >= 0:
                    if WorldDataResource[Resource[TempInt]] in PlayerInventory:
                        PlayerInventoryAmmount[PlayerInventory.index(WorldDataResource[Resource[TempInt]])] = PlayerInventoryAmmount[PlayerInventory.index(WorldDataResource[Resource[TempInt]])] + ResourceAmmount[TempInt]
                    else:
                        PlayerInventory.append(WorldDataResource[Resource[TempInt]])
                        PlayerInventoryAmmount.append(ResourceAmmount[TempInt])
                    Resource[TempInt] = -1
                    ResourceAmmount[TempInt] = 0
                TempInt = TempInt + 1
            WorldFile = open(os.path.dirname(os.path.abspath(__file__)) + "\\WorldData\\X" + str(PlayerInfo[2]) + " Y" + str(PlayerInfo[3]) + ".txt","w")
            if TerrainType == 0:
                WorldFile.write(str(TerrainType) + "\n" + str(Terrain) + "\n" + str(Resource[0]) + "\n" + str(ResourceAmmount[0]) +  "\n" + str(Resource[1]) + "\n" + str(ResourceAmmount[1]) + "\n" +  str(Resource[2]) + "\n" + str(ResourceAmmount[2]) + "\n" + str(Resource[3]) + "\n" + str(ResourceAmmount[3]))
            else:
                WorldFile.write(str(TerrainType) + "\n" + str(TerrainTypeMeta) + "\n" + str(Resource[0]) + "\n" + str(ResourceAmmount[0]) +  "\n" + str(Resource[1]) + "\n" + str(ResourceAmmount[1]) + "\n" +  str(Resource[2]) + "\n" + str(ResourceAmmount[2]) + "\n" + str(Resource[3]) + "\n" + str(ResourceAmmount[3]))
            print(str(TerrainType) + "\n" + str(TerrainTypeMeta) + "\n" + str(Resource[0]) + "\n" + str(ResourceAmmount[0]) +  "\n" + str(Resource[1]) + "\n" + str(ResourceAmmount[1]) + "\n" +  str(Resource[2]) + "\n" + str(ResourceAmmount[2]) + "\n" + str(Resource[3]) + "\n" + str(ResourceAmmount[3]))
            WorldFile.close()   #This rewrites the world file to stop infinte resources
            World()
        elif keyboard.is_pressed("4"): # Character
            Loop3 = 1
            while Loop3 == 1:
                os.system("cls")
                print("Name: " + str(PlayerInfo[0]) + " Level: " + str(PlayerInfo[7]) +" (" + str(PlayerInfo[0]) + "/" + str(PlayerInfo[7] * 100) +")\nHP: " + str(PlayerCurrentStats[0])+ "/" + str(PlayerInfo[4]) + "  Mana: " + str(PlayerInfo[18]) + "/" + str(PlayerCurrentStats[1]) +"  Attack: " + str(PlayerInfo[5]) + "  Defence: " +  str(PlayerInfo[6]) + "\nLocation: X:" + str(PlayerInfo[3]) + " Y:" + str(PlayerInfo[4]) + "  Gold:" + str(PlayerInfo[9]) + "\nEquipped Weapon: " + str(PlayerInfo[10]) + "    Attack: " + str(PlayerInfo[11]) + "    Hit:" + str(PlayerInfo[12]) + "%   Critical:" + str(PlayerInfo[13]) + "%    Durabilty: " + str(PlayerInfo[14]) + "%\nEquipped Armour: " + str(PlayerInfo[15]) + "    Defence:" + str(PlayerInfo[16]) + "    Durabilty: " + str(PlayerInfo[17]) + "\n\n1) Equip Armor   2) Equip Weapons   3) View Items   Q) Go Back")
                Loop2 = 1
                time.sleep(1.5)
                while Loop2 == 1:
                    if keyboard.is_pressed("1"):  #Equip armor
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

                    elif keyboard.is_pressed("2"): #Equip Weapons
                        Loop2 = 1
                        while Loop2 == 1:
                            os.system("cls")
                            TempInt = 0
                            while TempInt <= int(len(PlayerInventoryWeapon)-1):
                                print(str(PlayerInventoryWeapon[TempInt]) + "  Attack: " + str(PlayerInventoryWeaponAtk[TempInt]) + "  Durability: " + str(PlayerInventoryWeaponDur[TempInt]) + "  Critical Rate: " + str(PlayerInventoryWeaponCrt[TempInt]) + "%   Hit Rate: " + str(PlayerInventoryWeaponHit[TempInt]) +   "%   ID: " + str(TempInt))
                                TempInt = TempInt + 1    

                            TempStr = input("You have curently equiped: " + PlayerInfo[10] + "  Attack: " + str(PlayerInfo[11]) + "  Durability: " + str(PlayerInfo[14]) + "  Critical Rate: " + str(PlayerInfo[13]) + "%  Hit Rate: " + str(PlayerInfo[12]) + "%\nType the id of an armour to equip it (or type leave with no capitals to leave)\n")
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
        
                    elif keyboard.is_pressed("3"): #Items
                        TempInt = 0
                        while TempInt <= int(len(PlayerInventory)-1):
                            print(str(PlayerInventory[TempInt]) + "  (" + str(PlayerInventoryAmmount[TempInt]) +")")
                            TempInt = TempInt + 1
                        input("Press enter to continue\n")
                        Loop2 = 0
                    
                    elif keyboard.is_pressed("Q"):
                        World()
        elif keyboard.is_pressed("5"):  # Saves and load
            SaveLoad()
        elif keyboard.is_pressed("6"):  # Quit
            print(Fore.RED + "Unless you have saved all data will be lost." + Fore.RESET + "\nAre you sure? (Y/N)")
            Loop3 = 1
            while Loop3 == 1:
                if keyboard.is_pressed("Y"):
                    exit()
                elif keyboard.is_pressed("N"):
                    World()

def SaveLoad():
    print("SaveLoad")

def Battle():
    EnemyMult = int(round(len(WorldDataEnemyName[Enemy[2]]) / random.randint(1,25)))
    if Enemy[0] >= 0:
        EnemyMult = EnemyMult + int(round(len(WorldDataEnemyPrefix[Enemy[1]]) / 10))
    if Enemy[3] >= 0:
        EnemyMult = EnemyMult + int(round(len(WorldDataEnemySuffix[Enemy[3]]) / 10))

    if EnemyMult > 1:
        EnemyMult = 2

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
        while Loop2 == 1:
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
                            PlayerCurrentStats[1] = PlayerCurrentStats[1] - PlayerMagicCost[TempStr]
                            if PlayerMagicType[TempStr].upper() == "DAMAGE":
                                print("\nYou casted " + str(PlayerMagic[TempStr]))
                                Attack = PlayerMagicValue[TempStr]
                            elif PlayerMagicType[TempStr].upper() == "HEAL":
                                print("\nYou casted " + str(PlayerMagic[TempStr]))
                                PlayerCurrentStats[0] = PlayerCurrentStats[0] + PlayerMagicValue[TempStr]   
                                if PlayerInfo[4] < PlayerCurrentStats[0]:
                                    PlayerCurrentStats[0] = PlayerInfo[4]

            elif keyboard.is_pressed("3"):
                Def = Def * 2
                Loop2 = 0
            elif keyboard.is_pressed("4"):
                if random.randint(0,1) == 0:
                    World()
                else:
                    print("Couldn't run!")
                    Loop2 = 0
        
        EnemyAttack = EnemyATK + random.randint(-10 * PlayerInfo[7],10 * PlayerInfo[7])
        EnemyAttack = EnemyAttack - PlayerInfo[6]
        EnemyHP = EnemyHP - Attack
        if EnemyAttack <= 0:
            EnemyAttack = 0
        PlayerCurrentStats[0] = PlayerCurrentStats[0] - EnemyAttack

        if EnemyHP <= 0:
            #PlayerInfo  = [0,0,0,0,50,25,5,1,0,500,"Hands",0,100,0,0,"Nothing",0,0,50,0] #0name,difficulty,x,y,hp,5atk,def,level,exp,gold,10EquipedWeaponName,EquipedWeaponAttack,EquipedWeaponHit,EquipedWeaponCritical,EquipedWeaponDurabilty,EquipedArmorName,EquippedArmourDefence,EquipedArmorDurabilty,Mana,Monolith Spell count (19)
            PlayerInfo[8] = PlayerInfo[8] + random.randint(0,250) #XP
            PlayerInfo[9] = PlayerInfo[9] + random.randint(random.randint(1,250),300) # Gold
            if PlayerInfo[8] > PlayerInfo[7] * 1000:
                print("You Leveled up!")
                PlayerInfo[7] = PlayerInfo[7] + 1
                PlayerInfo[8] = 0
                PlayerInfo[4] = PlayerInfo[4] + random.randint(1,25)
                PlayerInfo[5] = PlayerInfo[5] + random.randint(1,25)
                PlayerInfo[6] = PlayerInfo[6] + random.randint(1,25)
                time.sleep(5)
            else:
                print("")
            World()
            
        if PlayerCurrentStats[0] <= 0:
            Death()

def Death():
    print("You died.")
    time.sleep(100)

Intialise() #Starts the game after all functions are declared