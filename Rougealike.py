SystemStats = [0,"0.8","Jan/19/1/20"] # 0 - Debug  1 - BuildDate/Version
def BootCheck():    #Starts up and checks required modules are installed
    try:
        import keyboard
        from colorama import Fore, Back, Style, init
    except ImportError:
        input("You are missing the required modules\nPlease run this command to in Powershell or Command Prompt to continue.")
    
    if SystemStats[0] == 1:
        print("\nYou are in developer mode.\nScreens will not be cleared\nDO NOT SUBMIT BUG REPORTS WITH THIS ENABLED\nTo disable developer mode change SystemStats[0] to 0\n\n")

BootCheck()
import time
import keyboard
import random
import os      
import linecache
import json
import threading
from colorama import Fore, Back, Style, init    #C O L O U R
import urllib.request
import zipfile
init(convert=True)  #Allows CMD and Powershell to display colors instead of the acsii codes

#random.randint(-2147483500,2147483500)
WorldStats = [0,0,1]    #0-X coord 1- Y coord  2 - Difficulty
EnemyStats  = [50,50,50,50,3]
PlayerInventory = [""]
PlayerInventoryAmmount = [""]
PlayerGeneral = [0,0,1] # 0 - XP   1 - Gold   2 - Level
PlayerMaxStats = [50,50,50]  #0-HP 1-Attack 2-Defence
EnemyStats = [0,0,0]
SaveInfo = ["Unknown","Unknown"] #Latest Version 1- Last saved to
Resource1Ammount = 0
TurnCount        = 0
AlternateTerrain = 0
TerrainID        = 0
WorldText     = "ERROR"
EnemyText     = "ERROR"
Resource1Text = "ERROR"
Resource1     = "ERROR"
PlayerHealingItems = ["Basic Healing Potion","Advanced Healing Potion"]
PlayerHealingItemsAmmount = [0,0]
Z = 0
PlayerInventoryArmourRes = []
PlayerInventoryArmour    = []
PlayerInventoryArmourDef = []
PlayerInventoryWeapon    = []
PlayerInventoryWeaponAtk = []
PlayerInventoryWeaponRes = []
PlayerInventoryWeaponCrt = []
PlayerInventoryWeaponhit = []
PlayerPrefs              = [linecache.getline(os.path.dirname(os.path.abspath(__file__)) + "\\Data\\Prefs.ini",6),linecache.getline(os.path.dirname(os.path.abspath(__file__)) + "\\Data\\Prefs.ini",10),linecache.getline(os.path.dirname(os.path.abspath(__file__)) + "\\Data\\Prefs.ini",14)] #0 - Color  1 - Brightness 2 Autoupdate
PlayerPrefs[0] = PlayerPrefs[0].strip()
PlayerPrefs[1] = PlayerPrefs[1].strip()
PlayerPrefs[2] = PlayerPrefs[2].strip()
EquipedArmour = "Nothing"   #Name of armour
EquipedArmourDef = 0 #Defence increase
EquipedArmourRes = 0 #Durabilty
EquipedWeapon = "Hands"
EquipedWeaponhit = 100
EquipedWeaponatk = 0
EquipedWeaponcrt = 0
EquipedWeaponres = 0
SaveUI = 1  #0- Player has a chance to select a slot 1- disables UI and forces auto save
BattleLog = ["","","","","","",""]
QuestName = ["","QuestTest1","QuestTest2 -  Triple Darkness","QuestTest3","Quest test 3 - Connectivity"] # name of the quest
QuestDescription = ["","Quest test!","This is a quest to test","Beast drops?","Who is this guy?"]
QuestReq1Ammount = ["",20,5,10,5]
QuestReq1Item = ["","Iron Bar","Branches","Beast Hide","Sword of gods"]
QuestReward = ["",1000]
PlayerHP = 50
#I'm fairly Local, I've been around, I've seen the streets you're walking down

def UpdateCheck():               
    global SystemStats
    global PlayerPrefs

    print("Trying to check update servers...\n\nTired of seeing this?\nChange the autoupdater setting in Prefs.ini\nThis shouldn't take more than 30 seconds")

    if PlayerPrefs[2] == "0":
        Menu()

    try:
        urllib.request.urlretrieve("https://raw.githubusercontent.com/TMAltair/RougalikeRPG/master/metadata.txt",os.path.dirname(os.path.abspath(__file__)) + "\\Data\\meta.txt")
        LatestVer = str(linecache.getline(os.path.dirname(os.path.abspath(__file__)) + "\\Data\\meta.txt",3))
    except:
        LatestVer = "Failed"
    LatestVer = LatestVer.strip()
    
    try:
        os.remove(os.path.dirname(os.path.abspath(__file__)) + "\\Data\\meta.txt")
    except:
        time.sleep(0)
    
    os.system("cls")
    if LatestVer != SystemStats[1] and not LatestVer == "Failed": #Autoupdater code
        print("You are on version " + str(SystemStats[1]) + "\nVersion " + str(LatestVer) + " is available\n\nUpdate? (Y/N)")
        b = 1
        while b == 1:
            if keyboard.is_pressed("y"):
                print("Downloading latest version from github (1/4)")
                try:
                    os.mkdir("Rougalike " + LatestVer)
                except:
                    a = 0
                urllib.request.urlretrieve("https://raw.githubusercontent.com/TMAltair/RougalikeRPG/master/Rougalike.py",os.path.dirname(os.path.abspath(__file__)) + "\\Rougalike " + LatestVer +"\\Rougalike " + LatestVer + ".py")
                print("Downloading Latest data files (2/4)")
                urllib.request.urlretrieve("https://raw.githubusercontent.com/TMAltair/RougalikeRPG/master/Data.zip",os.path.dirname(os.path.abspath(__file__)) + "\\Rougalike " + LatestVer +"\\Data.zip")
                print("Extracting data files (3/4)")
                with zipfile.ZipFile(os.path.dirname(os.path.abspath(__file__)) + "\\Rougalike " + LatestVer + "\\Data.zip", 'r') as zip_ref:
                    zip_ref.extractall(os.path.dirname(os.path.abspath(__file__)) + "\\Rougalike " + LatestVer)
                print("Deleting Data.zip (4/4)")
                os.remove(os.path.dirname(os.path.abspath(__file__)) + "\\Rougalike " + LatestVer + "\\Data.zip")
                print("\n" + Fore.GREEN + "Complete!" + Fore.__getattribute__(PlayerPrefs[0]) + "\nTo run the latest version look for the folder called Rougalike " + LatestVer)
                input("Press enter to close\n")
                exit()
            elif keyboard.is_pressed("n"):
                Menu()
    Menu()

def Menu(): #Handles the mainmenu   
    global SystemStats
    global WorldStats

    os.system("cls")
    print("RoguelikeRPG by TMAltair\n\n1) Play\n2) Load\n3) Exit\n\nPress the number in brackets to select your options \nSupport the project at: http://bit.ly/Rougalike")
    if SystemStats[0] == 1:
        print(Fore.RED+ "YOU ARE IN DEVELOPER MODE.\nBuildNumber = " + str(SystemStats[2]) + Fore.__getattribute__(PlayerPrefs[0]))

    A = 1
    while A == 1:
        if keyboard.is_pressed("1"):
            
            if SystemStats[0] != 1:
                os.system("cls")
            else:
                WorldGen()

            print("Select your difficulty:\n1) Easy\n2) Medium\n3) Hard")
            time.sleep(1)
            B = 1
            while B == 1:
                if keyboard.is_pressed("1"):
                    WorldStats[2] = 1
                    B = 0
                elif keyboard.is_pressed("2"):
                    WorldStats[2] = 2
                    B = 0
                elif keyboard.is_pressed("3"):
                    WorldStats[2] = 3

            while B == 0:
                if SystemStats[0] != 1:
                    os.system("cls")
                
                Name = input("Name your character: ")
                B = 1
            TimerStart = time.time()
            WorldGen()

        elif keyboard.is_pressed("2"):
            Load()
        elif keyboard.is_pressed("3"):
            exit()

def WorldGen(): #generates Terrain
    global WorldText
    global EnemyStats
    global WorldStats
    global EnemyText
    global Resource1
    global Resource1Ammount
    global Resource1Text
    global AlternateTerrain
    global WorldStats #0-X coord 1- Y coord  2 - Difficulty
    global TerrainID
    global EnemyText
    global Weather
    global WeatherID
    global SaveUI
    global TurnCount
    
    AlternateTerrain = random.randint(1,50)
    if AlternateTerrain <= 4:
        AlternateTerrains()

    CurrentCoords = "x" + str(WorldStats[0]) + "y" + str(WorldStats[1])
    if os.path.exists(os.path.dirname(os.path.abspath(__file__)) + "\\Data\\WorldData\\" + CurrentCoords + ".txt"): # Terrain that exists
        TerrainID    = linecache.getline(os.path.dirname(os.path.abspath(__file__)) + "\\Data\\WorldData\\" + CurrentCoords + ".txt",1)
        TerrainID    = int(TerrainID.strip())
        Terrain      = linecache.getline(os.path.dirname(os.path.abspath(__file__)) + "\\Data\\Terrain\\Terrain.txt", TerrainID)       #Rolls Terrain
        TerrainBr    = linecache.getline(os.path.dirname(os.path.abspath(__file__)) + "\\Data\\Terrain\\Brightness.txt", TerrainID)     #Gets brightness
        TerrainCl    = linecache.getline(os.path.dirname(os.path.abspath(__file__)) + "\\Data\\Terrain\\Color.txt", TerrainID)          #Gets color
        Terrain      = Terrain.strip()      #Removes \n
        TerrainBr    = TerrainBr.strip()    #Removes \n
        TerrainCl    = TerrainCl.strip()    #Removes \n
        try:    #Stops crashes
            TerrainText  = "You are " + Fore.__getattribute__(TerrainCl) + Style.__getattribute__(TerrainBr) + Terrain + "." + Fore.__getattribute__(PlayerPrefs[0]) + Back.RESET
        except AttributeError:
            WorldGen()
        TerrainText  = "You are " + Fore.__getattribute__(TerrainCl) + Style.__getattribute__(TerrainBr) + Terrain + "." + Fore.__getattribute__(PlayerPrefs[0]) + Back.RESET

        Resource1ID = int(linecache.getline(os.path.dirname(os.path.abspath(__file__)) + "\\Data\\WorldData\\" + CurrentCoords + ".txt",2)) #Rolls Resource
        if Resource1ID > 0:
            Resource1Ammount = int(linecache.getline(os.path.dirname(os.path.abspath(__file__)) + "\\Data\\WorldData\\" + CurrentCoords + ".txt",3)) 
            Resource1 = linecache.getline(os.path.dirname(os.path.abspath(__file__)) + "\\Data\\Resources\\Resources.txt",Resource1ID)    #Gets resource      
            Resource1Br = linecache.getline(os.path.dirname(os.path.abspath(__file__))  + "\\Data\\Resources\\Brightness.txt",Resource1ID) #Gets brightness
            Resource1Cl = linecache.getline(os.path.dirname(os.path.abspath(__file__)) + "\\Data\\Resources\\Color.txt",Resource1ID)       #Gets color
            Resource1   = Resource1.strip()     #Removes \n
            Resource1Br = Resource1Br.strip()   #Removes \n
            Resource1Cl = Resource1Cl.strip()   #Removes \n

            try:    #Stops crashes
                Resource1Text = "There are " + Style.__getattribute__(Resource1Br) + Fore.__getattribute__(Resource1Cl) + str(Resource1Ammount)  + " " + Resource1 +  " here."
            except AttributeError:
                WorldGen()
            Resource1Text = "There are " + Style.__getattribute__(Resource1Br) + Fore.__getattribute__(Resource1Cl) + str(Resource1Ammount)  + " " + Resource1 +  " here."
            
            if Resource1Ammount == 0:
                Resource1Text = ""
        else:
            Resource1Text = ""

        EnemySlots = int(linecache.getline(os.path.dirname(os.path.abspath(__file__)) + "\\Data\\Slots.txt",3))
        EnemyID = random.randint(1,EnemySlots)
        EnemyName = linecache.getline(os.path.dirname(os.path.abspath(__file__)) + "\\Data\\Enemys.txt",EnemyID)
        EnemyText = Fore.__getattribute__(PlayerPrefs[0]) + "There is a " + Fore.RED + str(EnemyName.strip()) + Fore.__getattribute__(PlayerPrefs[0]) + " here."

        WorldText = str(TerrainText) + "\n" + str(Resource1Text) + "\n" + str(EnemyText)
        if Resource1Text == "":
            WorldText = str(TerrainText) + "\n" + str(EnemyText)                                        
    else: #Terrain that needs to be generated
        TerrainSlots = int(linecache.getline(os.path.dirname(os.path.abspath(__file__)) + "\\Data\\Slots.txt", 1))    #Gets total ammount of terrain
        TerrainID    = random.randint(1,TerrainSlots) #Line Number of Terrain
        Terrain      = linecache.getline(os.path.dirname(os.path.abspath(__file__)) + "\\Data\\Terrain\\Terrain.txt", TerrainID)       #Rolls Terrain
        TerrainBr    = linecache.getline(os.path.dirname(os.path.abspath(__file__)) + "\\Data\\Terrain\\Brightness.txt", TerrainID)     #Gets brightness
        TerrainCl    = linecache.getline(os.path.dirname(os.path.abspath(__file__)) + "\\Data\\Terrain\\Color.txt", TerrainID)          #Gets color
        Terrain      = Terrain.strip()      #Removes \n
        TerrainBr    = TerrainBr.strip()    #Removes \n
        TerrainCl    = TerrainCl.strip()    #Removes \n
        try:    #Stops crashes
            TerrainText  = "You are " + Fore.__getattribute__(TerrainCl) + Style.__getattribute__(TerrainBr) + Terrain + "." + Fore.__getattribute__(PlayerPrefs[0]) + Back.RESET
        except AttributeError:
            WorldGen()
        TerrainText  = "You are " + Fore.__getattribute__(TerrainCl) + Style.__getattribute__(TerrainBr) + Terrain + "." + Fore.__getattribute__(PlayerPrefs[0]) + Back.RESET

        ResourceSlots = int(linecache.getline(os.path.dirname(os.path.abspath(__file__)) + "\\Data\\Slots.txt", 2))   #Gets total ammount of resource
        Resource1ID = random.randint(1,ResourceSlots) #Rolls Resource
        Resource1Ammount = random.randint(0,10)       #Rolls 
        Resource1 = linecache.getline(os.path.dirname(os.path.abspath(__file__)) + "\\Data\\Resources\\Resources.txt",Resource1ID)    #Gets resource      
        Resource1Br = linecache.getline(os.path.dirname(os.path.abspath(__file__))  + "\\Data\\Resources\\Brightness.txt",Resource1ID) #Gets brightness
        Resource1Cl = linecache.getline(os.path.dirname(os.path.abspath(__file__)) + "\\Data\\Resources\\Color.txt",Resource1ID)       #Gets color
        Resource1   = Resource1.strip()     #Removes \n
        Resource1Br = Resource1Br.strip()   #Removes \n
        Resource1Cl = Resource1Cl.strip()   #Removes \n

        try:    #Stops crashes
            Resource1Text = "There are " + Style.__getattribute__(Resource1Br) + Fore.__getattribute__(Resource1Cl) + str(Resource1Ammount)  + " " + Resource1 +  " here."
        except AttributeError:
            WorldGen()
        Resource1Text = "There are " + Style.__getattribute__(Resource1Br) + Fore.__getattribute__(Resource1Cl) + str(Resource1Ammount)  + " " + Resource1 +  " here."
        
        if Resource1Ammount == 0:
            Resource1Text = ""
            Resource1ID = 0

        if random.randint(0,2) > 0:
            EnemySlots = int(linecache.getline(os.path.dirname(os.path.abspath(__file__)) + "\\Data\\Slots.txt",3))
            EnemyID = random.randint(1,EnemySlots)
            EnemyName = linecache.getline(os.path.dirname(os.path.abspath(__file__)) + "\\Data\\Enemys.txt",EnemyID)
            EnemyText = Fore.__getattribute__(PlayerPrefs[0]) + "There is a " + Fore.RED + str(EnemyName.strip()) + Fore.__getattribute__(PlayerPrefs[0]) + " here."
        else:
            EnemyText = ""

        WorldText = str(TerrainText)

        if Resource1Text != "":
            WorldText = WorldText + "\n" + str(Resource1Text)

        if EnemyText != "":
            WorldText = WorldText + "\n" + str(EnemyText)

        WorldFile = open(os.path.dirname(os.path.abspath(__file__)) + "\\Data\\WorldData\\" + CurrentCoords + ".txt","w")
        WorldFile.write(str(TerrainID) + "\n" + str(Resource1ID) + "\n" + str(Resource1Ammount))
        WorldFile.close()

    WeatherID = random.randint(1,55)
    if WeatherID <= 5:
        Weather = linecache.getline(os.path.dirname(os.path.abspath(__file__)) + "\\Data\\Terrain\\Weather.txt",WeatherID)
        Weather = Weather.strip()
        if WeatherID == 1: # sunny weather makes res1 * 1-10
            Resource1Ammount = Resource1Ammount * random.randint(1,10)
        elif WeatherID == 2:
            Resource1Ammount = round(Resource1Ammount / 2) + 1
        elif WeatherID == 3:
            time.sleep(0)
        elif WeatherID == 4:
            time.sleep(0)
        elif WeatherID == 5:
            time.sleep(0)

    PlayerTurn()

def PlayerTurn():
    global PlayerInventory
    global PlayerInventoryAmmount
    global Resource1
    global Resource1Ammount
    global TurnCount
    global WorldText
    global EquipedArmour
    global EquipedArmourDef
    global EquipedArmourRes
    global EquipedWeapon
    global EquipedWeaponatk
    global EquipedWeaponres
    global EquipedWeaponcrt
    global EquipedWeaponhit
    global BattleLog
    global PlayerPrefs
    global WeatherID
    global Weather
    global PlayerHP
    global PlayerMaxStats
    global SaveUI

    if PlayerHP < 0:
        PlayerHP = 1

    if SystemStats != 1:
        os.system("cls")
    
    if SaveUI == 1:
        Save()
    else:
        SaveUI = 1

    BattleLog[0] = BattleLog[1] 
    BattleLog[1] = BattleLog[2]
    BattleLog[2] = BattleLog[3]
    BattleLog[3] = BattleLog[4]
    BattleLog[4] = BattleLog[5]
    BattleLog[5] = ""

    print(str(BattleLog[0]) + "\n" + str(BattleLog[1]) + "\n" + str(BattleLog[2]) + "\n" + str(BattleLog[3]) + "\n" + str(BattleLog[4]) + "\n" + str(BattleLog[5]))

    TurnCount = TurnCount + 1
    print(Style.__getattribute__(PlayerPrefs[1]) + Fore.__getattribute__(PlayerPrefs[0]) + "Turn: " + str(TurnCount))
    if PlayerHP < PlayerMaxStats[0]:
        print("HP: " + str(round(PlayerHP / PlayerMaxStats[0] * 100)) + "%")

    print("\n" + WorldText + Fore.__getattribute__(PlayerPrefs[0]) + Style.__getattribute__(PlayerPrefs[1]) + "\n\n\nOptions:\n1) Battle     2) Move  3) Collect items  4) Inventory\n5) Save/Load  6) Map   7) Quest log      8) Quit")
  
    if WeatherID <= 5:
        print(Fore.YELLOW + "Weather Warning: Very " + Weather + "!" + Fore.__getattribute__(PlayerPrefs[0]))

    time.sleep(1)
    a = 1
    while a == 1:
        if keyboard.is_pressed("1"):
            Battle()
        
        elif keyboard.is_pressed("2"):
            Move()
        
        elif keyboard.is_pressed("3"):
            Collect()
        
        elif keyboard.is_pressed("4"):
            if SystemStats != 1:
                 os.system("cls")
            print("Select a catagory to display:\n\n1) Items    3) Armor\n2) Potions  4) Weapons")
            c = 1
            time.sleep(1)
            while c == 1:
                if keyboard.is_pressed("1"):
                    a = len(PlayerInventory)
                    b = 0
                    c = 0
                    while b < a:
                        print(PlayerInventory[b] + " (" + str(PlayerInventoryAmmount[b]) + ")")
                        b = b + 1
                    input("Press Enter to continue")
                    PlayerTurn()
                elif keyboard.is_pressed("2"):
                    a = len(PlayerHealingItems)
                    b = 0
                    c = 0
                    while b < a:
                        print(PlayerHealingItems[b] + " (" + str(PlayerHealingItemsAmmount[b]) + ")")
                        b = b + 1
                    input("Press Enter to continue")
                    PlayerTurn()
                elif keyboard.is_pressed("3"):
                    d = 1
                    while d == 1:
                        if SystemStats != 1:
                            os.system("cls")
                        a = len(PlayerInventoryArmour)
                        b = 0
                        c = 0
                        while b < a:
                            print(PlayerInventoryArmour[b] + "  Defence: " + str(PlayerInventoryArmourDef[b]) + "  Durability: " + str(PlayerInventoryArmourRes[b]) + "  ID: " + str(b))
                            b = b + 1                    
                        print("You have curently equiped: " + EquipedArmour + "  Defence: " + str(EquipedArmourDef) + "  Durability: " + str(EquipedArmourRes))
                        armourSelect = input("Type the id of an armor to equip it (or type leave with no capitals to leave)\n")
                        err = 0
                        if armourSelect == "leave":
                            PlayerTurn()

                        try:
                            armourSelect = int(armourSelect)
                        except:
                            err = 1
                        else:
                            err = 0
                            int(armourSelect)

                        if err == 0 and len(PlayerInventoryArmour) >= armourSelect:
                            PlayerInventoryArmour.append(EquipedArmour)
                            PlayerInventoryArmourDef.append(EquipedArmourDef)
                            PlayerInventoryArmourRes.append(EquipedArmourRes)

                            EquipedArmour = PlayerInventoryArmour[armourSelect]
                            EquipedArmourDef = PlayerInventoryArmourDef[armourSelect]
                            EquipedArmourRes = PlayerInventoryArmourRes[armourSelect]

                            PlayerInventoryArmour.pop(armourSelect)
                            PlayerInventoryArmourDef.pop(armourSelect)
                            PlayerInventoryArmourRes.pop(armourSelect)
                        else:
                            print("an error occured while processing your ID, please use numbers only for IDs and your ID exists.")
                
                elif keyboard.is_pressed("4"):
                    d = 1
                    while d == 1:
                        if SystemStats != 1:
                            os.system("cls")
                        a = len(PlayerInventoryWeapon)
                        b = 0
                        c = 0
                        while b < a:
                            print(str(PlayerInventoryWeapon[b]) + "  Attack: " + str(PlayerInventoryWeaponAtk[b]) + "  Durability: " + str(PlayerInventoryWeaponRes[b]) + "  Critical Rate: " + str(PlayerInventoryWeaponCrt[b]) + "%   Hit Rate: " + str(PlayerInventoryWeaponhit[b]) +   "%   ID: " + str(b))
                            b = b + 1                    
                        print("You have curently equiped: " + EquipedWeapon + "  Attack: " + str(EquipedWeaponres) + "  Durability: " + str(EquipedWeaponres) + "  Critical Rate: " + str(EquipedWeaponcrt) + "%  Hit Rate: " + str(EquipedWeaponhit) + "%")
                        WeaponSelect = input("Type the id of an armour to equip it (or type leave with no capitals to leave)\n")
                        err = 0
                        if WeaponSelect == "leave":
                            PlayerTurn()

                        try:
                            WeaponSelect = int(WeaponSelect)
                        except:
                            err = 1
                        else:
                            err = 0
                            int(WeaponSelect)

                        if err == 0 and len(PlayerInventoryWeapon) >= WeaponSelect:
                            PlayerInventoryWeapon.append(EquipedWeapon)
                            PlayerInventoryWeaponAtk.append(EquipedWeaponatk)
                            PlayerInventoryWeaponRes.append(EquipedWeaponres)
                            PlayerInventoryWeaponhit.append(EquipedWeaponhit)
                            PlayerInventoryWeaponCrt.append(EquipedWeaponcrt)

                            EquipedWeapon = PlayerInventoryWeapon[WeaponSelect]
                            EquipedWeaponatk = PlayerInventoryWeaponAtk[WeaponSelect]
                            EquipedWeaponres = PlayerInventoryWeaponRes[WeaponSelect]
                            EquipedWeaponcrt = PlayerInventoryWeaponCrt[WeaponSelect]
                            EquipedWeaponhit = PlayerInventoryWeaponhit[WeaponSelect]              

                            PlayerInventoryWeapon.pop(WeaponSelect)
                            PlayerInventoryWeaponAtk.pop(WeaponSelect)
                            PlayerInventoryWeaponRes.pop(WeaponSelect)
                            PlayerInventoryWeaponCrt.pop(WeaponSelect)
                            PlayerInventoryWeaponhit.pop(WeaponSelect)
                        else:
                            print("an error occured while processing your ID, please use numbers only for IDs and your ID exists.")
        
        elif keyboard.is_pressed("5"):
            A = 0
            print("\n1) Save\n2) Load\n3) Go Back")
            while A == 0:
                if keyboard.is_pressed("1"):
                    Save()
                elif keyboard.is_pressed("2"):
                    Load()
                elif keyboard.is_pressed("3"):
                    PlayerTurn
        
        elif keyboard.is_pressed("6"): 
            global WorldStats
            upleft = "x" + str(int(WorldStats[0] - 1)) + "y" + str(int(WorldStats[1] + 1))
            upmid  = "x" + str(int(WorldStats[0])) + "y" + str(int(WorldStats[1] + 1))
            uprig = "x" + str(int(WorldStats[0] + 1)) + "y" + str(int(WorldStats[1] + 1))
            midlef = "x" + str(int(WorldStats[0] - 1)) + "y" + str(int(WorldStats[1]))
            midmid =  "x" + str(int(WorldStats[0])) + "y" + str(int(WorldStats[1]))
            midrig = "x" + str(int(WorldStats[0] + 1)) + "y" + str(int(WorldStats[1]))
            lowlef = "x" + str(int(WorldStats[0] - 1)) + "y" + str(int(WorldStats[1] - 1))
            lowmid = "x" + str(int(WorldStats[0])) + "y" + str(int(WorldStats[1] - 1))
            lowrig = "x" + str(int(WorldStats[0] + 1)) + "y" + str(int(WorldStats[1] - 1))

            uprow  = " "
            midrow = " "
            lowrow = " "

            if os.path.exists(os.path.dirname(os.path.abspath(__file__)) + "\\Data\\WorldData\\" + upleft + ".txt"):
                temp1 = int(linecache.getline(os.path.dirname(os.path.abspath(__file__)) + "\\Data\\WorldData\\" + upleft + ".txt",1))  #Terrainid
                temp2 = linecache.getline(os.path.dirname(os.path.abspath(__file__)) + "\\Data\\Terrain\\Terrain.txt", temp1)       #Rolls Terrain
                uprow = uprow + Fore.__getattribute__(linecache.getline(os.path.dirname(os.path.abspath(__file__)) + "\\Data\\Terrain\\Color.txt",temp1).strip()) + temp2[0] + " "
            else:
                uprow = uprow + Fore.__getattribute__(PlayerPrefs[0]) + "?" + " "

            if os.path.exists(os.path.dirname(os.path.abspath(__file__)) + "\\Data\\WorldData\\" + upmid + ".txt"):
                temp1 = int(linecache.getline(os.path.dirname(os.path.abspath(__file__)) + "\\Data\\WorldData\\" + upmid + ".txt",1))  #Terrainid
                temp2 = linecache.getline(os.path.dirname(os.path.abspath(__file__)) + "\\Data\\Terrain\\Terrain.txt", temp1)       #Rolls Terrain
                uprow = uprow + Fore.__getattribute__(linecache.getline(os.path.dirname(os.path.abspath(__file__)) + "\\Data\\Terrain\\Color.txt",temp1).strip()) + temp2[0] + " "
            else:
                uprow = uprow + Fore.__getattribute__(PlayerPrefs[0]) + "?" + " "

            if os.path.exists(os.path.dirname(os.path.abspath(__file__)) + "\\Data\\WorldData\\" + uprig + ".txt"):
                temp1 = int(linecache.getline(os.path.dirname(os.path.abspath(__file__)) + "\\Data\\WorldData\\" + uprig + ".txt",1))  #Terrainid
                temp2 = linecache.getline(os.path.dirname(os.path.abspath(__file__)) + "\\Data\\Terrain\\Terrain.txt", temp1)       #Rolls Terrain
                uprow = uprow + Fore.__getattribute__(linecache.getline(os.path.dirname(os.path.abspath(__file__)) + "\\Data\\Terrain\\Color.txt",temp1).strip()) + temp2[0] + " "
            else:
                uprow = uprow + Fore.__getattribute__(PlayerPrefs[0]) + "?" + " " 

            if os.path.exists(os.path.dirname(os.path.abspath(__file__)) + "\\Data\\WorldData\\" + midlef + ".txt"):
                temp1 = int(linecache.getline(os.path.dirname(os.path.abspath(__file__)) + "\\Data\\WorldData\\" + midlef + ".txt",1))  #Terrainid
                temp2 = linecache.getline(os.path.dirname(os.path.abspath(__file__)) + "\\Data\\Terrain\\Terrain.txt", temp1)       #Rolls Terrain
                midrow = midrow + Fore.__getattribute__(linecache.getline(os.path.dirname(os.path.abspath(__file__)) + "\\Data\\Terrain\\Color.txt",temp1).strip()) + temp2[0] + " "
            else:
                midrow = midrow + Fore.__getattribute__(PlayerPrefs[0]) + "?" + " " 

            if os.path.exists(os.path.dirname(os.path.abspath(__file__)) + "\\Data\\WorldData\\" + midmid + ".txt"):
                temp1 = int(linecache.getline(os.path.dirname(os.path.abspath(__file__)) + "\\Data\\WorldData\\" + midmid + ".txt",1))  #Terrainid
                temp2 = linecache.getline(os.path.dirname(os.path.abspath(__file__)) + "\\Data\\Terrain\\Terrain.txt", temp1)       #Rolls Terrain
                midrow = midrow + Fore.__getattribute__(linecache.getline(os.path.dirname(os.path.abspath(__file__)) + "\\Data\\Terrain\\Color.txt",temp1).strip()) + temp2[0] + " "
            else:
                midrow = midrow + Fore.__getattribute__(PlayerPrefs[0]) + "?" + " " 

            if os.path.exists(os.path.dirname(os.path.abspath(__file__)) + "\\Data\\WorldData\\" + midrig + ".txt"):
                temp1 = int(linecache.getline(os.path.dirname(os.path.abspath(__file__)) + "\\Data\\WorldData\\" + midrig + ".txt",1))  #Terrainid
                temp2 = linecache.getline(os.path.dirname(os.path.abspath(__file__)) + "\\Data\\Terrain\\Terrain.txt", temp1)       #Rolls Terrain
                midrow = midrow + Fore.__getattribute__(linecache.getline(os.path.dirname(os.path.abspath(__file__)) + "\\Data\\Terrain\\Color.txt",temp1).strip()) + temp2[0] + " "
            else:
                midrow = midrow + Fore.__getattribute__(PlayerPrefs[0]) + "?" + " " 

            if os.path.exists(os.path.dirname(os.path.abspath(__file__)) + "\\Data\\WorldData\\" + lowlef + ".txt"):
                temp1 = int(linecache.getline(os.path.dirname(os.path.abspath(__file__)) + "\\Data\\WorldData\\" + lowlef + ".txt",1))  #Terrainid
                temp2 = linecache.getline(os.path.dirname(os.path.abspath(__file__)) + "\\Data\\Terrain\\Terrain.txt", temp1)       #Rolls Terrain
                lowrow = lowrow + Fore.__getattribute__(linecache.getline(os.path.dirname(os.path.abspath(__file__)) + "\\Data\\Terrain\\Color.txt",temp1).strip()) + temp2[0] + " "
            else:
                lowrow = lowrow + Fore.__getattribute__(PlayerPrefs[0]) + "?" + " " 

            if os.path.exists(os.path.dirname(os.path.abspath(__file__)) + "\\Data\\WorldData\\" + lowmid + ".txt"):
                temp1 = int(linecache.getline(os.path.dirname(os.path.abspath(__file__)) + "\\Data\\WorldData\\" + lowmid + ".txt",1))  #Terrainid
                temp2 = linecache.getline(os.path.dirname(os.path.abspath(__file__)) + "\\Data\\Terrain\\Terrain.txt", temp1)       #Rolls Terrain
                lowrow = lowrow + Fore.__getattribute__(linecache.getline(os.path.dirname(os.path.abspath(__file__)) + "\\Data\\Terrain\\Color.txt",temp1).strip()) + temp2[0] + " "
            else:
                lowrow = lowrow + Fore.__getattribute__(PlayerPrefs[0]) + "?" + " " 

            if os.path.exists(os.path.dirname(os.path.abspath(__file__)) + "\\Data\\WorldData\\" + lowrig + ".txt"):
                temp1 = int(linecache.getline(os.path.dirname(os.path.abspath(__file__)) + "\\Data\\WorldData\\" + lowrig + ".txt",1))  #Terrainid
                temp2 = linecache.getline(os.path.dirname(os.path.abspath(__file__)) + "\\Data\\Terrain\\Terrain.txt", temp1)       #Rolls Terrain
                lowrow = lowrow + Fore.__getattribute__(linecache.getline(os.path.dirname(os.path.abspath(__file__)) + "\\Data\\Terrain\\Color.txt",temp1).strip()) + temp2[0] + " "
            else:
                lowrow = lowrow + Fore.__getattribute__(PlayerPrefs[0]) + "?" + " " 

            print("\n\n" + uprow + Fore.__getattribute__(PlayerPrefs[0]) + "Current X Position: " + str(WorldStats[0]) + "\n" + midrow + Fore.__getattribute__(PlayerPrefs[0]) +"Current Y Position: " + str(WorldStats[1]) + "\n" + lowrow + Fore.__getattribute__(PlayerPrefs[0]) )
            TurnCount = TurnCount - 1
            input("Press enter to go back...")
            PlayerTurn()

        elif keyboard.is_pressed("7"):
            Quests()
        elif keyboard.is_pressed("8"):
            print(Fore.RED + "Unless you have saved all data will be lost." + Fore.__getattribute__(PlayerPrefs[0]) + "\nAre you sure? (Y/N)")
            B = 1
            while B == 1:
                if keyboard.is_pressed("Y"):
                    exit()
                elif keyboard.is_pressed("N"):
                    PlayerTurn()

def AlternateTerrains():
    global AlternateTerrain
    global PlayerMaxStats
    global PlayerInventory
    global PlayerInventoryAmmount
    global EnemyStats
    global PlayerGeneral
    global PlayerHealingItems
    global PlayerHealingItemsAmmount
    global Z
    global PlayerInventoryArmourRes
    global PlayerInventoryArmour
    global PlayerInventoryArmourDef
    global BattleLog
    global PlayerPrefs
    Loop = 1

    if SystemStats != 1:
        os.system("cls")

    if AlternateTerrain == 1:   #Monolith
        TerrainMonolith = random.randint(1,50)         #Stat increase
        TerrainMonolithType = random.randint(1,110)  #Abilitys of monolith
        print(Fore.__getattribute__(PlayerPrefs[0]) + "You are at a monolith.\n1) Read the monolith")
        BattleLog[5] = "You visted a monolith"
        if PlayerGeneral[2] >= 25:
            print(Fore.__getattribute__(PlayerPrefs[0]) + "You feel you could unlock the power of the monolith.\n2) Unlock the monothlith")
        
        time.sleep(1)

        A = 1
        while A == 1:
            if keyboard.is_pressed("1"):
                PlayerMaxStats[0] = PlayerMaxStats[0] + random.randint(1,20)
                PlayerMaxStats[1] = PlayerMaxStats[1] + random.randint(1,20)
                PlayerMaxStats[2] = PlayerMaxStats[2] + random.randint(1,20)
                print("Your stats have improved.")
                input("Press enter to continue...")
                WorldGen()
            elif keyboard.is_pressed("2") and PlayerGeneral[2] >= 25:
                Z = 1
                EnemyStats = [10000,750,750]
                print("You are about fight a really strong foe\nAre you sure\n1) Yes\n2) No")
                a = 1
                while a == 1:
                    if keyboard.is_pressed("1"):
                        a = 0
                    elif keyboard.is_pressed("2"):
                        Z = 0
                        WorldGen()
                Battle()
    #0-HP 1-Attack 2-Defence
    elif AlternateTerrain == 2: #Caves
        Risk = 0
        RskTxt = "None"
        LayersDeep = 0
        BattleLog[5] = "You explored a cave"
        while Loop == 1:
            CaveResources = [int(linecache.getline(os.path.dirname(os.path.abspath(__file__)) + "\Data\Terrain\AlternateTerrains\Caves\Resources.txt",1))]
            CaveResources.append(linecache.getline(os.path.dirname(os.path.abspath(__file__)) + "\Data\Terrain\AlternateTerrains\Caves\Resources.txt",random.randint(2,CaveResources[0])))
            CaveResources.append(linecache.getline(os.path.dirname(os.path.abspath(__file__)) + "\Data\Terrain\AlternateTerrains\Caves\Resources.txt",random.randint(2,CaveResources[0])))
            CaveResources.append(linecache.getline(os.path.dirname(os.path.abspath(__file__)) + "\Data\Terrain\AlternateTerrains\Caves\Resources.txt",random.randint(2,CaveResources[0])))
            CaveResources.append(linecache.getline(os.path.dirname(os.path.abspath(__file__)) + "\Data\Terrain\AlternateTerrains\Caves\Resources.txt",random.randint(2,CaveResources[0])))
            CaveResources.append(linecache.getline(os.path.dirname(os.path.abspath(__file__)) + "\Data\Terrain\AlternateTerrains\Caves\Resources.txt",random.randint(2,CaveResources[0])))  
            CaveResources.append(linecache.getline(os.path.dirname(os.path.abspath(__file__)) + "\Data\Terrain\AlternateTerrains\Caves\Resources.txt",random.randint(2,CaveResources[0])))  
            CaveResources[1] = CaveResources[1].strip()
            CaveResources[2] = CaveResources[2].strip()
            CaveResources[3] = CaveResources[3].strip()
            CaveResources[4] = CaveResources[4].strip()
            CaveResources[5] = CaveResources[5].strip()
            CaveResourcesAmmount = [random.randint(1,random.randint(1,5 + LayersDeep)),random.randint(1,random.randint(1,5 + LayersDeep)),random.randint(1,random.randint(1,5 + LayersDeep)),random.randint(1,random.randint(1,5 + LayersDeep)),random.randint(1,random.randint(1,5 + LayersDeep)),random.randint(1,random.randint(1,5 + LayersDeep)),random.randint(1,random.randint(1,5 + LayersDeep))]
            #CaveRes    = 0-Works like Slots.txt, 1-5 Resources
            #CaveResAmm = 0 - blank number ,      1-5 ammounts
            if Risk >= 90:
                RskTxt = Fore.RED + "COLASPE IMMINENT." + Fore.__getattribute__(PlayerPrefs[0])
            elif Risk >= 75:
                RskTxt ="Risk: " + Fore.RED + "High" + Fore.__getattribute__(PlayerPrefs[0])
            elif Risk >= 50:
                RskTxt ="Risk: " + Fore.YELLOW + "Medium" + Fore.__getattribute__(PlayerPrefs[0])
            elif Risk >= 25:
                RskTxt ="Risk: " + Fore.BLUE + "Low" + Fore.__getattribute__(PlayerPrefs[0])
            elif Risk >= 0: 
                RskTxt ="Risk: " + Fore.CYAN + "None" + Fore.__getattribute__(PlayerPrefs[0])
            print(Fore.__getattribute__(PlayerPrefs[0]) + "\nYou are in a cave\n\nThere are: \n" + str(CaveResourcesAmmount[1]) + " KG of " + CaveResources[1] + "\n" + str(CaveResourcesAmmount[2]) + " KG of " + CaveResources[2] + "\n" + str(CaveResourcesAmmount[3]) + " KG of " + CaveResources[3] + "\n" + str(CaveResourcesAmmount[4]) + " KG of " + CaveResources[4] + "\n" + str(CaveResourcesAmmount[5]) + " KG of " + CaveResources[5] + "\n" + RskTxt + "\n\nOptions:\n1) Collect\n2) Explore deeper\n3) Leave\n4) Guide")
            time.sleep(1)
            TurnLoop = 1 
            while TurnLoop == 1:
                if keyboard.is_pressed("1"):    #Collects items
                    Risk = Risk + random.randint(5,10)
                    if Risk >= 100:
                        input("The cave collasped.\nPress enter to continue ")
                        WorldGen()
                    elif Risk < 0:
                        Risk = 0

                    if CaveResources[1] in PlayerInventory: #Collects Item #1
                        PlayerInventoryAmmount[PlayerInventory.index(CaveResources[1])] = PlayerInventoryAmmount[PlayerInventory.index(CaveResources[1])] + CaveResourcesAmmount[1]
                    else:
                        PlayerInventoryAmmount.append(CaveResourcesAmmount[1]) 
                        PlayerInventory.append(CaveResources[1])

                    if CaveResources[2] in PlayerInventory: #Collects Item #2
                        PlayerInventoryAmmount[PlayerInventory.index(CaveResources[2])] = PlayerInventoryAmmount[PlayerInventory.index(CaveResources[2])] + CaveResourcesAmmount[2]
                    else:
                        PlayerInventoryAmmount.append(CaveResourcesAmmount[2]) 
                        PlayerInventory.append(CaveResources[2])

                    if CaveResources[3] in PlayerInventory: #Collects Item #3
                        PlayerInventoryAmmount[PlayerInventory.index(CaveResources[3])] = PlayerInventoryAmmount[PlayerInventory.index(CaveResources[3])] + CaveResourcesAmmount[3]
                    else:
                        PlayerInventoryAmmount.append(CaveResourcesAmmount[3]) 
                        PlayerInventory.append(CaveResources[3])

                    if CaveResources[4] in PlayerInventory: #Collects Item #4
                        PlayerInventoryAmmount[PlayerInventory.index(CaveResources[4])] = PlayerInventoryAmmount[PlayerInventory.index(CaveResources[4])] + CaveResourcesAmmount[4]
                    else:
                        PlayerInventoryAmmount.append(CaveResourcesAmmount[4]) 
                        PlayerInventory.append(CaveResources[4])

                    if CaveResources[5] in PlayerInventory: #Collects Item #5
                        PlayerInventoryAmmount[PlayerInventory.index(CaveResources[5])] = PlayerInventoryAmmount[PlayerInventory.index(CaveResources[5])] + CaveResourcesAmmount[5]
                    else:
                        PlayerInventoryAmmount.append(CaveResourcesAmmount[5]) 
                        PlayerInventory.append(CaveResources[5])

                    print("Collected items.")
                    CaveResources[1] = "There is nothing here"
                    CaveResources[2] = " "
                    CaveResources[3] = " "
                    CaveResources[4] = " "
                    CaveResources[5] = " "
                    CaveResourcesAmmount[1] = " "
                    CaveResourcesAmmount[2] = " "
                    CaveResourcesAmmount[3] = " "
                    CaveResourcesAmmount[4] = " "
                    CaveResourcesAmmount[5] = " "                                        
                    TurnLoop = 0
                    
                elif keyboard.is_pressed("2"): 
                    Risk = Risk - random.randint(-50,5)
                    LayersDeep = LayersDeep + 1
                    
                    if Risk >= 100:
                        if LayersDeep >= 10:
                            if random.randint(LayersDeep,100) >= 10:
                                input("The cave colasped and you didn't make it out in time.\n You died, Press enter to restart.")
                                Menu()
                            else:
                               TurnLoop = 0
                    else:
                        TurnLoop = 0

                elif keyboard.is_pressed("3"):
                    WorldGen()
                
                elif keyboard.is_pressed("4"):
                    print("Collect as many resources as you can!\nBy going deeper you can find way more resources however it may be dangerous.")
                    TurnLoop = 0

    elif AlternateTerrain == 3: #AstralProjection
        # Crafting modes 0 -  just add to inventory 1 - Mark as equipable weapon (adds to playerInventoryWeapons) 2- Mark as equipable Armour (PlayerInventoryArmour)
        if SystemStats[0] != 1:
            os.system("cls")
        print(Fore.__getattribute__(PlayerPrefs[0]) + "You are at a village\n1) Use Workbench\n2) Shop\n3) leave")
        BattleLog[5] = "You visted a Village"        
        tm = 1
        time.sleep(1)
        while tm == 1:
            if keyboard.is_pressed("1"):    #Workbench code
                A = 1
                time.sleep(1)
                while A == 1: 
                    if SystemStats[0] != 1:
                        os.system("cls")
                    print("What do you want to craft\n1) Items\n2) Armor\n3) Weapons\n")
                    B = 1
                    time.sleep(1)
                    while B == 1:   #Gets crafting group
                        if keyboard.is_pressed("1"): #Sets opperating mode to 0
                            C = 1
                            print("\nCraft:\n1) Metal\n2) Gem\n")
                            time.sleep(1)
                            while C == 1:
                                if keyboard.is_pressed("1"):
                                    Craft = "Metal"
                                    CraftMode = 0
                                    CraftSlotLine = 3
                                    C = 0
                                    B = 0 
                                elif keyboard.is_pressed("2"):
                                    Craft  = "Gem"
                                    CraftMode = 0
                                    CraftSlotLine = 6
                                    C = 0
                                    B = 0
                        elif keyboard.is_pressed("2"): #Sets Opperating mode to 1
                            C = 0
                            B = 0
                            Craft = "Armour"
                            CraftMode = 1
                            CraftSlotLine = 9
                        elif keyboard.is_pressed("3"): #Sets Opperating mode to 1
                            C = 1
                            print("\nCraft:\n1) Axe\n2) Sword\n3) Lance\n4) Bow\n5) Mace")
                            time.sleep(1)
                            while C == 1:
                                if keyboard.is_pressed("1"):
                                    Craft = "Weapon\\Axe"
                                    CraftMode = 2
                                    CraftSlotLine = 13
                                    WeaponType = 1
                                    C = 0
                                    B = 0 
                                elif keyboard.is_pressed("2"):
                                    Craft  = "Weapon\\Sword"
                                    CraftMode = 2
                                    WeaponType = 2
                                    CraftSlotLine = 16
                                    C = 0
                                    B = 0
                                elif keyboard.is_pressed("3"):
                                    Craft  = "Weapon\\Lance"
                                    CraftMode = 2
                                    WeaponType = 2
                                    CraftSlotLine = 19
                                    C = 0
                                    B = 0
                                elif keyboard.is_pressed("4"):
                                    Craft  = "Weapon\\Bow"
                                    CraftMode = 2
                                    WeaponType = 2
                                    CraftSlotLine = 22
                                    C = 0
                                    B = 0
                                elif keyboard.is_pressed("5"):
                                    Craft  = "Weapon\\Mace"
                                    CraftMode = 2
                                    WeaponType = 2
                                    CraftSlotLine = 25
                                    C = 0
                                    B = 0

                    G = 1
                    while G == 1:
                        Temp = 1 # What line number to start from (Don't change)
                        CraftingSlots = int(linecache.getline(os.path.dirname(os.path.abspath(__file__)) + "\\Data\\Terrain\\AlternateTerrains\\Villages\\Slots.txt",int(CraftSlotLine)))
                        while Temp <= CraftingSlots:    #Gets data
                            if Temp == 1:
                                ReqResource = [""] #What Resource Required
                                Product     = [""]     #What will be given to the player
                                ReqAmmount  = [""]  #How much of ReqResource is needed
                                RedText   = []   #Items that cannot be crafted (Internal)
                                GreenProd = [""] #Items that can be crafted    (Internal)
                                GreenAmmount  = [""]
                                GreenResource = [""]
                                RedTxt   = "" # Text shown to player   (Things that the player has enough of)
                                Greentxt = "" # Text shown to player (Things that the player has some of)
                                Redtxt   = "" # Text show to player    (Things that the player has none of)

                            ReqResource.append(linecache.getline(os.path.dirname(os.path.abspath(__file__)) + "\\Data\\Terrain\\AlternateTerrains\\Villages\\WorkBench\\" + Craft + "\\Material.txt",int(Temp)))
                            ReqAmmount.append(linecache.getline(os.path.dirname(os.path.abspath(__file__)) + "\\Data\\Terrain\\AlternateTerrains\\Villages\\WorkBench\\" + Craft + "\\Ammount.txt",int(Temp)))
                            Product.append(linecache.getline(os.path.dirname(os.path.abspath(__file__)) + "\\Data\\Terrain\\AlternateTerrains\\Villages\\WorkBench\\" + Craft + "\\Product.txt",int(Temp)))

                            ReqAmmount[Temp] = int(ReqAmmount[Temp].strip()) #Removes \n (Newline character) 
                            ReqResource[Temp] = ReqResource[Temp].strip() #Removes \n (Newline character)
                            Product[Temp] = Product[Temp].strip() #Removes \n (Newline character)

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
                        
                        print(str(Fore.GREEN + Greentxt + Fore.RED + RedTxt + Redtxt + Fore.__getattribute__(PlayerPrefs[0]))) # Displays items in order of craftibilty
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
                                except: #If not in list then loop
                                    print("That number isn't valid, make sure it's a number in the brackets.")
                                else:
                                    E = 2
                        
                        if Select == 0:
                            AlternateTerrains()

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
                            PlayerInventoryArmourRes.append(random.randint(Product.index(GreenProd[Select]) * 10,Product.index(GreenProd[Select]) * 100))
                            print("Crafted 1 x " + str(GreenProd[Select]) + " - Def: " + str(PlayerInventoryArmourDef[len(PlayerInventoryArmourDef) - 1]) + " Durabilty: " + str(PlayerInventoryArmourDef[len(PlayerInventoryArmourRes) - 1]))
                        elif CraftMode == 2:    #For weapons
                            PlayerInventoryWeapon.append(GreenProd[Select])
                            PlayerInventoryWeaponAtk.append(random.randint(Product.index(GreenProd[Select]) * 10,Product.index(GreenProd[Select]) * 100))
                            PlayerInventoryWeaponhit.append(random.randint(random.randint(1,50),random.randint(50,100)))
                            PlayerInventoryWeaponCrt.append(random.randint(random.randint(0,25),random.randint(25,50)))
                            PlayerInventoryWeaponRes.append(random.randint(Product.index(GreenProd[Select]) * 10,Product.index(GreenProd[Select]) * 100))
                            print("Crafted 1 x " + str(GreenProd[Select]) + " - Atk: " + str(PlayerInventoryWeaponAtk[len(PlayerInventoryWeaponAtk) - 1]) + " Durabilty: " + str(PlayerInventoryWeaponRes[len(PlayerInventoryWeaponRes) - 1]) + " Hit: " + str(PlayerInventoryWeaponhit[len(PlayerInventoryWeaponhit) - 1]) + "% Critical: " + str(PlayerInventoryWeaponCrt[len(PlayerInventoryWeaponCrt) - 1])) 

            elif keyboard.is_pressed("3"):
                WorldGen()

    elif AlternateTerrain == 4: #Traders
        C = 0
        while C == 0:
            if SystemStats[0] != 1:
                os.system("cls")
        
            print(Fore.__getattribute__(PlayerPrefs[0]) + "There is a trader here, you can probably buy somthing here.\n1) Buy\n")
            if PlayerGeneral[1] >= 100:
                print(Fore.GREEN + "1) Basic Healing Potion - 100\nHeals 50 HP\n" + Fore.__getattribute__(PlayerPrefs[0]))
            else:
                print(Fore.RED + "1) Basic Healing Potion - 100\nHeals 50 HP\n" + Fore.__getattribute__(PlayerPrefs[0]))

            if PlayerGeneral[1] >= 250:
                print(Fore.GREEN + "2) Advanced Healing Potion - 500\nHeals 250 HP\n" + Fore.__getattribute__(PlayerPrefs[0]))
            else:
                print(Fore.RED + "2) Advanced Healing Potion - 500\nHeals 250 HP\n" + Fore.__getattribute__(PlayerPrefs[0]))

            print("3) Leave")
            time.sleep(1)

            A = 1
            while A == 1:
                if keyboard.is_pressed("1") and PlayerGeneral[1] >= 100:
                    PlayerHealingItemsAmmount[0] = PlayerHealingItemsAmmount[0] + 1
                    PlayerGeneral[1] = PlayerGeneral[1] - 100
                    A = 0
                elif keyboard.is_pressed("1") and PlayerGeneral[1] < 100:
                    print("You don't have enough gold.")
                    A = 0
                elif keyboard.is_pressed("2") and PlayerGeneral[1] >= 250:
                    PlayerHealingItemsAmmount[1] = PlayerHealingItemsAmmount[1] + 1
                    PlayerGeneral[1] = PlayerGeneral[1] - 250
                    A = 0
                elif keyboard.is_pressed("2") and PlayerGeneral[1] < 250:
                    print("You don't have enough gold.")
                    A = 0
                elif keyboard.is_pressed("3"):
                    WorldGen()

def Save():
    global PlayerInventory
    global PlayerInventoryAmmount
    global PlayerMaxStats
    global SaveInfo
    global WorldStats
    global PlayerGeneral
    global SaveInfo
    global TurnCount
    global PlayerHealingItems
    global PlayerHealingItemsAmmount
    global PlayerInventoryArmourRes
    global PlayerInventoryArmour
    global PlayerInventoryArmourDef
    global PlayerInventoryWeapon
    global PlayerInventoryWeaponAtk
    global PlayerInventoryWeaponRes
    global PlayerInventoryWeaponCrt
    global PlayerInventoryWeaponhit
    global EquipedArmour
    global EquipedArmourDef
    global EquipedArmourRes
    global EquipedWeapon
    global EquipedWeaponhit
    global EquipedWeaponatk
    global EquipedWeaponcrt
    global EquipedWeaponres
    global BattleLog
    global SaveUI

    #Panic!
    if SaveUI == 1:
        SaveUI = 0
        SlotNo = "Auto"
    else:
        SaveUI = 0 
        SaveInfo = [SystemStats[1],"Unknown"]
        print("Select a slot to save to (1-5)")
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

    destination = os.path.dirname(os.path.abspath(__file__)) + "\\Data\\PlayerData\\" + SlotNo + "\\PlayerInventory.json"
    with open(destination, "w") as file:
        json.dump(PlayerInventory, file)

    destination = os.path.dirname(os.path.abspath(__file__)) + "\\Data\\PlayerData\\" + SlotNo + "\\PlayerInventoryAmmount.json"
    with open(destination, "w") as file:
        json.dump(PlayerInventoryAmmount, file)

    destination = os.path.dirname(os.path.abspath(__file__)) + "\\Data\\PlayerData\\" + SlotNo + "\\PlayerMaxStats.json"
    with open(destination, "w") as file:
        json.dump(PlayerMaxStats, file)

    destination = os.path.dirname(os.path.abspath(__file__)) + "\\Data\\PlayerData\\" + SlotNo + "\\WorldStats.json"
    with open(destination, "w") as file:
        json.dump(WorldStats, file)

    destination = os.path.dirname(os.path.abspath(__file__)) + "\\Data\\PlayerData\\" + SlotNo + "\\PlayerGeneral.json"
    with open(destination, "w") as file:
        json.dump(PlayerGeneral, file)

    destination = os.path.dirname(os.path.abspath(__file__)) + "\\Data\\PlayerData\\" + SlotNo + "\\SaveInfo.json"
    with open(destination, "w") as file:
        json.dump(SaveInfo, file)

    destination = os.path.dirname(os.path.abspath(__file__)) + "\\Data\\PlayerData\\" + SlotNo + "\\TurnCount.json"
    with open(destination, "w") as file:
        json.dump(TurnCount, file)

    destination = os.path.dirname(os.path.abspath(__file__)) + "\\Data\\PlayerData\\" + SlotNo + "\\PlayerHealingItems.json"
    with open(destination, "w") as file:
        json.dump(PlayerHealingItems, file)
    
    destination = os.path.dirname(os.path.abspath(__file__)) + "\\Data\\PlayerData\\" + SlotNo + "\\PlayerHealingItemsAmmount.json"
    with open(destination, "w") as file:
        json.dump(PlayerHealingItemsAmmount, file)

    destination = os.path.dirname(os.path.abspath(__file__)) + "\\Data\\PlayerData\\" + SlotNo + "\\PlayerInventoryArmourRes.json"
    with open(destination, "w") as file:
        json.dump(PlayerInventoryArmourRes, file)

    destination = os.path.dirname(os.path.abspath(__file__)) + "\\Data\\PlayerData\\" + SlotNo + "\\PlayerInventoryArmour.json"
    with open(destination, "w") as file:
        json.dump(PlayerInventoryArmour, file)

    destination = os.path.dirname(os.path.abspath(__file__)) + "\\Data\\PlayerData\\" + SlotNo + "\\PlayerInventoryArmourDef.json"
    with open(destination, "w") as file:
        json.dump(PlayerInventoryArmourDef, file)

    destination = os.path.dirname(os.path.abspath(__file__)) + "\\Data\\PlayerData\\" + SlotNo + "\\PlayerInventoryWeapon.json"
    with open(destination, "w") as file:
        json.dump(PlayerInventoryWeapon, file)

    destination = os.path.dirname(os.path.abspath(__file__)) + "\\Data\\PlayerData\\" + SlotNo + "\\PlayerInventoryWeaponAtk.json"
    with open(destination, "w") as file:
        json.dump(PlayerInventoryWeaponAtk, file)

    destination = os.path.dirname(os.path.abspath(__file__)) + "\\Data\\PlayerData\\" + SlotNo + "\\PlayerInventoryWeaponRes.json"
    with open(destination, "w") as file:
        json.dump(PlayerInventoryWeaponRes, file)

    destination = os.path.dirname(os.path.abspath(__file__)) + "\\Data\\PlayerData\\" + SlotNo + "\\PlayerInventoryWeaponCrt.json"
    with open(destination, "w") as file:
        json.dump(PlayerInventoryWeaponCrt, file)

    destination = os.path.dirname(os.path.abspath(__file__)) + "\\Data\\PlayerData\\" + SlotNo + "\\PlayerInventoryWeaponhit.json"
    with open(destination, "w") as file:
        json.dump(PlayerInventoryWeaponhit, file)

    destination = os.path.dirname(os.path.abspath(__file__)) + "\\Data\\PlayerData\\" + SlotNo + "\\EquipedArmour.json"
    with open(destination, "w") as file:
        json.dump(EquipedArmour, file)

    destination = os.path.dirname(os.path.abspath(__file__)) + "\\Data\\PlayerData\\" + SlotNo + "\\EquipedArmourDef.json"
    with open(destination, "w") as file:
        json.dump(EquipedArmourDef, file)

    destination = os.path.dirname(os.path.abspath(__file__)) + "\\Data\\PlayerData\\" + SlotNo + "\\EquipedArmourRes.json"
    with open(destination, "w") as file:
        json.dump(EquipedArmourRes, file)

    destination = os.path.dirname(os.path.abspath(__file__)) + "\\Data\\PlayerData\\" + SlotNo + "\\EquipedWeapon.json"
    with open(destination, "w") as file:
        json.dump(EquipedWeapon, file)

    destination = os.path.dirname(os.path.abspath(__file__)) + "\\Data\\PlayerData\\" + SlotNo + "\\EquipedWeaponhit.json"
    with open(destination, "w") as file:
        json.dump(EquipedWeaponhit, file)

    destination = os.path.dirname(os.path.abspath(__file__)) + "\\Data\\PlayerData\\" + SlotNo + "\\EquipedWeaponatk.json"
    with open(destination, "w") as file:
        json.dump(EquipedWeaponatk, file)

    destination = os.path.dirname(os.path.abspath(__file__)) + "\\Data\\PlayerData\\" + SlotNo + "\\EquipedWeaponcrt.json"
    with open(destination, "w") as file:
        json.dump(EquipedWeaponcrt, file)

    destination = os.path.dirname(os.path.abspath(__file__)) + "\\Data\\PlayerData\\" + SlotNo + "\\EquipedWeaponres.json"
    with open(destination, "w") as file:
        json.dump(EquipedWeaponres, file)

    destination = os.path.dirname(os.path.abspath(__file__)) + "\\Data\\PlayerData\\" + SlotNo + "\\BattleLog.json"
    with open(destination, "w") as file:
        json.dump(BattleLog, file)

    print("Saved!\n\n")
    WorldGen()

def Load():
    global PlayerInventory
    global PlayerInventoryAmmount
    global PlayerMaxStats
    global SaveInfo
    global WorldStats
    global PlayerGeneral
    global SaveInfo
    global TurnCount
    global PlayerHealingItems
    global PlayerHealingItemsAmmount
    global PlayerInventoryArmourRes
    global PlayerInventoryArmour
    global PlayerInventoryArmourDef
    global PlayerInventoryWeapon
    global PlayerInventoryWeaponAtk
    global PlayerInventoryWeaponRes
    global PlayerInventoryWeaponCrt
    global PlayerInventoryWeaponhit
    global EquipedArmour
    global EquipedArmourDef
    global EquipedArmourRes
    global EquipedWeapon
    global EquipedWeaponhit
    global EquipedWeaponatk
    global EquipedWeaponcrt
    global EquipedWeaponres
    global BattleLog

    print("Select a slot to load (1 - 5) or press a to load the latest AutoSave:")
    time.sleep(1)
    A = 1
    while A == 1:
        if keyboard.is_pressed("1"):
            SlotNo = "Slot1"
            A=0
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
        elif keyboard.is_pressed("a"):
            SlotNo = "Auto"
            A = 0

    C = 1
    while C == 1:
        if os.path.exists(os.path.dirname(os.path.abspath(__file__)) + "\\Data\\PlayerData\\" + SlotNo + "\\SaveInfo.json"):
            destination = os.path.dirname(os.path.abspath(__file__)) + "\\Data\\PlayerData\\" + SlotNo + "\\SaveInfo.json"
            with open(destination) as file:
                SaveInfo = json.load(file)
        else:
            SaveInfo = ["Unknown","Unknown"]
                
        print("This save was last accessed/modifyed on: " + str(time.ctime(os.path.getmtime(os.path.dirname(os.path.abspath(__file__)) + "\\Data\\PlayerData\\" + SlotNo + "\\SaveInfo.json"))) + "\nLast version used: " + str(SaveInfo[0]) + "\nLoad? (Y/N)\n")
        B=1
        while B == 1:
            if keyboard.is_pressed("n"):
                Load()
            elif keyboard.is_pressed("y"):
                B = 0
                C = 0

    destination = os.path.dirname(os.path.abspath(__file__)) + "\\Data\\PlayerData\\" + str(SlotNo) + "\\PlayerInventory.json"
    with open(destination) as file:
        PlayerInventory = json.load(file)

    destination = os.path.dirname(os.path.abspath(__file__)) + "\\Data\\PlayerData\\" + str(SlotNo) + "\\PlayerInventoryAmmount.json"
    with open(destination) as file:
        PlayerInventoryAmmount = json.load(file)

    destination = os.path.dirname(os.path.abspath(__file__)) + "\\Data\\PlayerData\\" + str(SlotNo) + "\\PlayerMaxStats.json"
    with open(destination) as file:
        PlayerMaxStats = json.load(file)

    destination = os.path.dirname(os.path.abspath(__file__)) + "\\Data\\PlayerData\\" + str(SlotNo) + "\\WorldStats.json"
    with open(destination) as file:
        WorldStats = json.load(file)

    destination = os.path.dirname(os.path.abspath(__file__)) + "\\Data\\PlayerData\\" + str(SlotNo) + "\\PlayerGeneral.json"
    with open(destination) as file:
            PlayerGeneral = json.load(file)

    destination = os.path.dirname(os.path.abspath(__file__)) + "\\Data\\PlayerData\\" + str(SlotNo) + "\\SaveInfo.json"
    with open(destination) as file:
        SaveInfo = json.load(file)

    destination = os.path.dirname(os.path.abspath(__file__)) + "\\Data\\PlayerData\\" + str(SlotNo) + "\\TurnCount.json"
    with open(destination) as file:
        TurnCount = json.load(file)

    destination = os.path.dirname(os.path.abspath(__file__)) + "\\Data\\PlayerData\\" + str(SlotNo) + "\\PlayerHealingItems.json"
    with open(destination) as file:
        PlayerHealingItems = json.load(file)

    destination = os.path.dirname(os.path.abspath(__file__)) + "\\Data\\PlayerData\\" + str(SlotNo) + "\\PlayerHealingItemsAmmount.json"
    with open(destination) as file:
        PlayerHealingItemsAmmount = json.load(file)

    destination = os.path.dirname(os.path.abspath(__file__)) + "\\Data\\PlayerData\\" + str(SlotNo) + "\\PlayerInventoryArmourRes.json"
    with open(destination) as file:
        PlayerInventoryArmourRes = json.load(file)

    destination = os.path.dirname(os.path.abspath(__file__)) + "\\Data\\PlayerData\\" + str(SlotNo) + "\\PlayerInventoryArmour.json"
    with open(destination) as file:
        PlayerInventoryArmour = json.load(file)

    destination = os.path.dirname(os.path.abspath(__file__)) + "\\Data\\PlayerData\\" + str(SlotNo) + "\\PlayerInventoryArmourDef.json"
    with open(destination) as file:
        PlayerInventoryArmourDef = json.load(file)

    destination = os.path.dirname(os.path.abspath(__file__)) + "\\Data\\PlayerData\\" + str(SlotNo) + "\\PlayerInventoryWeapon.json"
    with open(destination) as file:
        PlayerInventoryWeapon = json.load(file)

    destination = os.path.dirname(os.path.abspath(__file__)) + "\\Data\\PlayerData\\" + str(SlotNo) + "\\PlayerInventoryWeaponAtk.json"
    with open(destination) as file:
        PlayerInventoryWeaponAtk = json.load(file)

    destination = os.path.dirname(os.path.abspath(__file__)) + "\\Data\\PlayerData\\" + str(SlotNo) + "\\PlayerInventoryWeaponRes.json"
    with open(destination) as file:
        PlayerInventoryWeaponRes = json.load(file)

    destination = os.path.dirname(os.path.abspath(__file__)) + "\\Data\\PlayerData\\" + str(SlotNo) + "\\PlayerInventoryWeaponCrt.json"
    with open(destination) as file:
        PlayerInventoryWeaponCrt = json.load(file)

    destination = os.path.dirname(os.path.abspath(__file__)) + "\\Data\\PlayerData\\" + str(SlotNo) + "\\PlayerInventoryWeaponhit.json"
    with open(destination) as file:
        PlayerInventoryWeaponhit = json.load(file)

    destination = os.path.dirname(os.path.abspath(__file__)) + "\\Data\\PlayerData\\" + str(SlotNo) + "\\EquipedArmour.json"
    with open(destination) as file:
        EquipedArmour = json.load(file)

    destination = os.path.dirname(os.path.abspath(__file__)) + "\\Data\\PlayerData\\" + str(SlotNo) + "\\EquipedArmourDef.json"
    with open(destination) as file:
        EquipedArmourDef = json.load(file)

    destination = os.path.dirname(os.path.abspath(__file__)) + "\\Data\\PlayerData\\" + str(SlotNo) + "\\EquipedArmourRes.json"
    with open(destination) as file:
        EquipedArmourRes = json.load(file)

    destination = os.path.dirname(os.path.abspath(__file__)) + "\\Data\\PlayerData\\" + str(SlotNo) + "\\EquipedWeapon.json"
    with open(destination) as file:
        EquipedWeapon = json.load(file)

    destination = os.path.dirname(os.path.abspath(__file__)) + "\\Data\\PlayerData\\" + str(SlotNo) + "\\EquipedWeaponhit.json"
    with open(destination) as file:
        EquipedWeaponhit = json.load(file)

    destination = os.path.dirname(os.path.abspath(__file__)) + "\\Data\\PlayerData\\" + str(SlotNo) + "\\EquipedWeaponatk.json"
    with open(destination) as file:
        EquipedWeaponatk = json.load(file)

    destination = os.path.dirname(os.path.abspath(__file__)) + "\\Data\\PlayerData\\" + str(SlotNo) + "\\EquipedWeaponcrt.json"
    with open(destination) as file:
        EquipedWeaponcrt = json.load(file)

    destination = os.path.dirname(os.path.abspath(__file__)) + "\\Data\\PlayerData\\" + str(SlotNo) + "\\EquipedWeaponres.json"
    with open(destination) as file:
        EquipedWeaponres = json.load(file)

    destination = os.path.dirname(os.path.abspath(__file__)) + "\\Data\\PlayerData\\" + str(SlotNo) + "\\EquipedWeaponres.json"
    with open(destination) as file:
        EquipedWeaponres = json.load(file)

    destination = os.path.dirname(os.path.abspath(__file__)) + "\\Data\\PlayerData\\" + str(SlotNo) + "\\BattleLog.json"
    with open(destination) as file:
        BattleLog = json.load(file)

    print("Loaded " + str(SlotNo) +"\n\n")
    WorldGen()    

def Battle():
    global PlayerMaxStats
    global WorldStats
    global PlayerGeneral
    global Z
    global EnemyStats
    global PlayerHealingItems
    global PlayerHealingItemsAmmount
    global EquipedArmourDef
    global EquipedWeapon
    global EquipedWeaponatk
    global EquipedWeaponcrt
    global EquipedWeaponhit
    global EquipedWeaponres 
    global EquipedArmour
    global EquipedArmourDef
    global EquipedArmourRes
    global EnemyText
    global BattleLog
    global PlayerHP
    global WeatherID

    if EnemyText == "":
        print("There is no enemy to battle.\n")
        time.sleep(2.5)
        PlayerTurn()

    if SystemStats != 1:
        os.system("cls")

    PlayerAttack = PlayerMaxStats[1]
    PlayerDefence = PlayerMaxStats[2]
    if Z != 1:
        EnemyStats = [random.randint(round(PlayerMaxStats[0]/2),PlayerMaxStats[0] * 2),random.randint(round(PlayerMaxStats[1]/2),PlayerMaxStats[1] * 2),random.randint(round(PlayerMaxStats[2]/2),PlayerMaxStats[2] * 2)]    
    #0-HP 1-Attack 2-Defence
    A = 1
    while A == 1:
        print("Your HP: " + str(PlayerHP) + "  Enemy HP: " + str(EnemyStats[0]) + "\n1) Attack  2) Defend\n3) Items   4) Run\n")
        B = 1
        time.sleep(1)
        while B == 1:
            Attack = 0
            Defence = 0
            F = 0
            if keyboard.is_pressed("1"): # attack
                Attack = PlayerAttack + EquipedWeaponatk
                if random.randint(0,100) > EquipedWeaponhit:
                    Attack = 0
                    B = 0
                    print("You missed!")
                if random.randint(0,100) <= EquipedWeaponcrt:
                    Attack = round(Attack * 2)
                if EquipedWeapon != "Hands":
                    EquipedWeaponres = EquipedWeaponres - 1
                    if EquipedWeaponres <= 0: 
                        print(EquipedWeapon + " broke.")
                        EquipedWeapon = "Hands"
                        EquipedWeaponatk = 0
                        EquipedWeaponcrt = 0
                        EquipedWeaponhit = 100
                        EquipedWeaponres = 0 

                Defence = PlayerDefence
                if EquipedArmour != "Nothing":
                    EquipedArmourRes = EquipedArmourRes - 1
                    if EquipedArmourRes <= 0:
                        print(EquipedArmour + " broke.")
                        EquipedArmour = "Nothing"
                        EquipedArmourDef = 0
                        EquipedArmourRes = 0
                B = 0
                Defence = random.randint(Defence,Defence * 2)
            elif keyboard.is_pressed("2"):  #defence
                Defence = PlayerDefence * 2
                B = 0
            elif keyboard.is_pressed("3"):
                print("1) Basic Healing Potion (+ 50HP) You have: " + str(PlayerHealingItemsAmmount[0]) + "\n2) Advanced Healing Potion (+ 250HP) You have: " + str(PlayerHealingItemsAmmount[1]) + "\n3) Go back")
                C = 1
                time.sleep(1)
                while C == 1:
                    if keyboard.is_pressed("1"):
                        C = 0
                        B = 0
                        if PlayerHealingItemsAmmount[0] > 0:
                            PlayerHP = PlayerHP + 50
                            PlayerHealingItemsAmmount[0] = PlayerInventoryAmmount[0] - 1
                        else:
                            print("You don't have enough potions")

                    if keyboard.is_pressed("2"):
                        C = 0
                        B = 0
                        if PlayerHealingItemsAmmount[1] > 0:
                            PlayerHP = PlayerHP + 250
                            PlayerHealingItemsAmmount[1] = PlayerInventoryAmmount[1] - 1
                        else:
                            print("You don't have enough potions")
                            
                    if keyboard.is_pressed("3"):
                        C = 0
                        B = 0
                        EnAttack = 0
                        F = 1

            elif keyboard.is_pressed("4"):
                if WeatherID == 4 and random.randint(1,2) == 1: # Wind 
                    BattleLog[5] = "Got blown away by the wind from X:" + str(WorldStats[0]) + " Y:" + str(WorldStats[1])
                    WorldStats[0] = random.randint(-2147483500,2147483500)
                    WorldStats[1] = random.randint(-2147483500,2147483500)
                    BattleLog[5] = BattleLog[5] + " To X:" + str(WorldStats[0]) + " Y:" + str(WorldStats[1])
                    WorldGen()
                if random.randint(0,1) == 0:
                    WorldGen()
                else:
                    print("Couldn't run!")
                    B = 0
        
        atkmult = WorldStats[2] * 10
        EnAttack = EnemyStats[1] + atkmult - random.randint(round(Defence/2),Defence)
        
        Attack = Attack - EnemyStats[2] + atkmult
        if EnAttack <= 0:
            EnAttack = 0
        if Attack <= 0:
            Attack = 0
        
        if F == 1:
            EnAttack = 0
        
        EnemyStats[0] = EnemyStats[0] - random.randint(Attack,round(Attack * 1.5))
        PlayerHP = PlayerHP - EnAttack
        print("\nYour attack did: " + str(Attack) + "\nEnemy Attack did: " + str(EnAttack))

        if WeatherID == 3 and EquipedArmour != "Nothing":
            print("You also took " + str(round(PlayerMaxStats[0] / 5)) + " from the hot weather!")
            PlayerHP = PlayerHP - round(PlayerMaxStats[0] / 5)

        if WeatherID == 5 and EquipedArmour == "Nothing":
            print("You also took " + str(round(PlayerMaxStats[0] / 5)) + " from the cold weather!")
            PlayerHP = PlayerHP - round(PlayerMaxStats[0] / 5)

        if EnemyStats[0] <= 0:
            BattleLog[5] = "Won a battle" 
            if PlayerGeneral[0] >= PlayerGeneral[2] * 1000:
                print("You leveled up!")
                LevelUpBonu13s = random.randint(1,50)
                PlayerMaxStats[0] = PlayerMaxStats[0] + LevelUpBonus
                PlayerHP = PlayerMaxStats[0]
                print("HP Increased by " + str(LevelUpBonus))
                LevelUpBonus = random.randint(1,50)
                PlayerAttack = PlayerAttack + LevelUpBonus
                print("Attack Increased by" + str(LevelUpBonus))
                LevelUpBonus = random.randint(1,50)
                PlayerDefence = PlayerDefence + LevelUpBonus
                print("Defence Increased by" + str(LevelUpBonus))
                PlayerGeneral[2] + 1
                input("Press enter to continue...")
                PlayerTurn()
            else:
                input("Press enter to continue...")
                PlayerTurn()
        elif PlayerHP <= 0:
            input("You died.\nPress enter to restart")
            Menu()

def Collect():
    global PlayerInventory
    global PlayerInventoryAmmount
    global Resource1
    global Resource1Ammount
    global Resource1Text
    global WorldStats
    global BattleLog

    CurrentCoords = "x" + str(WorldStats[0]) + "y" + str(WorldStats[1])

    if Resource1Text == "":
        print("Theres nothing here to collect!\n")
        PlayerTurn()

    BattleLog[5] = "Collected " + str(Resource1Ammount) + " " + str(Resource1)

    if Resource1 in PlayerInventory:
        PlayerInventoryAmmount[PlayerInventory.index(Resource1)] = PlayerInventoryAmmount[PlayerInventory.index(Resource1)] + Resource1Ammount
    else:
        PlayerInventoryAmmount.append(Resource1Ammount)
        PlayerInventory.append(Resource1)

    WorldFile = open(os.path.dirname(os.path.abspath(__file__)) + "\\Data\\WorldData\\" + CurrentCoords + ".txt","w")
    WorldFile.write(str(TerrainID) + "\n0\n0")
    WorldFile.close()

    WorldGen()

def Move():
    global WorldStats

    print("\nSelect a direction to move\n         (1)\n        North\n(4) West     East (2)\n        South\n         (3)")
    time.sleep(1)
    a = 1
    while a == 1:
        if random.randint(1,10) == 1:
            os.system("cls")
            print("You were ambushed!")
            BattleLog[5] = "You tryed to move but you were ambushed!"
            time.sleep(1)
            Battle()

        if keyboard.is_pressed("1"):
            WorldStats[1] = WorldStats[1] + 1
            a = 0
            BattleLog[5] = "Moved North"
        elif keyboard.is_pressed("2"):
            WorldStats[0] = WorldStats[0] + 1
            a = 0
            BattleLog[5] = "Moved East"
        elif keyboard.is_pressed("3"):
            WorldStats[1] = WorldStats[1] - 1
            a = 0
            BattleLog[5] = "Moved South"
        elif keyboard.is_pressed("4"):
            WorldStats[0] = WorldStats[0] - 1
            a = 0
            BattleLog[5] = "Moved West"
    
    
    WorldGen()

def Quests(): # Unused for now
    global QuestName
    global QuestDescription
    global QuestType
    global QuestReq1Ammount
    global QuestReq1Item
    global QuestReward
    global PlayerInventory
    global PlayerInventoryAmmount

    if len(QuestName) == 0:
        input("You have no quests...\nPress enter to continue\n")
        PlayerTurn()

    A = 1
    QuestDisp = ""
    while A <= len(QuestName) - 1:
        B = 1 
        QuestDisp = QuestDisp + "\n\nQuest ID: " + str(A) + "\n" + QuestName[A] + "\n" + QuestDescription[A] + "\nRequirements:"
        if QuestReq1Item[A] in PlayerInventory: 
            if QuestReq1Ammount[A] >= PlayerInventoryAmmount[PlayerInventory.index(QuestReq1Item[A])]:
                QuestDisp = QuestDisp + Fore.GREEN + "\n" + str(PlayerInventoryAmmount[PlayerInventory.index(QuestReq1Item[A])]) + "/" + str(QuestReq1Ammount[A])  + " - " +  str(QuestReq1Item[A]) + Fore.__getattribute__(PlayerPrefs[0])
            else:
                QuestDisp = QuestDisp + Fore.RED + "\n" + PlayerInventoryAmmount[PlayerInventory.index(QuestReq1Item[A])] + "/" + QuestReq1Ammount[A]  + " - " + QuestReq1Item[A] + Fore.__getattribute__(PlayerPrefs[0])
        else:
            QuestDisp = QuestDisp + Fore.RED + "\n0/" + str(QuestReq1Ammount[A])  + " - " + QuestReq1Item[A] + Fore.__getattribute__(PlayerPrefs[0])
    
        A = A + 1
    print(QuestDisp)
    input("Press enter to continue")
    PlayerTurn()

UpdateCheck()