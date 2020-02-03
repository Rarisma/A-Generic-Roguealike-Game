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
PlayerInfo  = [0,0,0,0,50,25,5,1,0,500,"Hands",0,100,0,0,"Nothing",0,0] #name,difficulty,x,y,hp,atk,def,level,exp,gold,EquipedWeaponName,EquipedWeaponAttack,EquipedWeaponHit,EquipedWeaponCritical,EquipedWeaponDurabilty,EquipedArmorName,EquippedArmourDefence,EquipedArmorDurabilty
TerrainType = 0
TerrainTypeMeta = 0
Terrain  = 0
Resource = 0
ResourceAmmount = 0
Enemy   = [""]
Weather = 0
BattleLog = ["","","","","",""]
PlayerInventory = []
PlayerInventoryAmmount = []
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

    Loop = 1
    while Loop == 1:
        if keyboard.is_pressed("1"):
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


    Enemy = [random.randint(0,1),random.randint(-1,len(WorldDataEnemyPrefix)-1),random.randint(0,len(WorldDataEnemyName)-1),random.randint(-1,len(WorldDataEnemySuffix)-1)] #0- 0/1 1 is enabled    1-Prefix (-1 if disabled)   2-Enemy name    3-Suffix (-1 if disabled) 


    World()

def World(): # Handles terrain and Player choices
    global PlayerInfo
    global BattleLog
    global PlayerInventory
    global PlayerInventoryAmmount
    global Resource
    global ResourceAmmount

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
        print(Fore.RESET + str(ResourceText) + Fore.RESET + ".")

    EnemyText = ""
    if Enemy[0] == 0:
        EnemyText = Fore.RED + "There is a "
    if Enemy[1] != -1:
        EnemyText = EnemyText + WorldDataEnemyPrefix[Enemy[1]] + " "
    if Enemy[0] == 0:
        EnemyText = EnemyText + WorldDataEnemyName[Enemy[2]] + " "
    if Enemy[3]!= -1:
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
                print("Battle") 
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
        elif keyboard.is_pressed("4"): 
            TempStr = "Name: " + str(PlayerInfo[0]) + " Level: " + str(PlayerInfo[7]) +" (" + str(PlayerInfo[0]) + "/" + str(PlayerInfo[7] * 100) +")"+ "\n" 
            TempStr = TempStr + "Max HP: " + str(PlayerInfo[4]) + "  Attack: " + str(PlayerInfo[5]) + "  Defence: " +  str(PlayerInfo[6]) + "\nLocation: X:" + str(PlayerInfo[3]) + " Y:" + str(PlayerInfo[4]) + "  Gold:" + str(PlayerInfo[9]) + "\nEquipped Weapon: " + str(PlayerInfo[10]) + "    Attack: " + str(PlayerInfo[11]) + "    Hit:" + str(PlayerInfo[12])
            TempStr = TempStr + "%   Critical:" + str(PlayerInfo[13]) + "%    Durabilty: " + str(PlayerInfo[14]) + "%\nArmour: " + str(PlayerInfo[15]) + "    Defence:" + str(PlayerInfo[16]) + "    Durabilty: " + str(PlayerInfo[17])
            print(str(TempStr))
            time.sleep(10)
        elif keyboard.is_pressed("5"):
            SaveLoad()
        elif keyboard.is_pressed("6"):
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
    print("Battle")


Intialise() #Starts the game after all functions are declared