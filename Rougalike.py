#Mk 5?
BuildNumber = "0.0.2 Nov/18/11/19"
Debug = 0   #1 = true anything else = false

def BootCheck():    #Starts up and checks required modules are installed
    TMPTXT = "FILLER TEXT"
    TMPTXT = ""
    try:
         import time
    except ImportError:
        TMPTXT = " time"

    try:
        import keyboard
    except ImportError:
        TMPTXT = TMPTXT + " keyboard"
    
    try:
        import random
    except ImportError:
        TMPTXT = TMPTXT + " random"

    try:
        import os
    except ImportError:
        TMPTXT = TMPTXT + " os"

    try:
        import linecache
    except ImportError:
        TMPTXT = TMPTXT + " linecache"

    try:
        from colorama import Fore, Back, Style
    except ImportError:
        TMPTXT = TMPTXT + " colorama"

    if TMPTXT == "":
        print(" ")
    else:
        input("You are missing required modules.\nPlease use this command in comand prompt to fix this\npip install" + TMPTXT)

#Fore.__getattribute__(TxClPref) + Back.__getattribute__(TxHlPref) + Style.__getattribute__(TxBrPref) 
#This is the color prefs 

BootCheck()
import time
import keyboard
import random
import os
import linecache
from colorama import Fore, Back, Style, init
init(convert=True)  #Allows CMD and Powershell to display colors instead of the acsii code or whatever garbled text s/21A is

MapX = random.randint(-1000000,1000000)
MapY = random.randint(-1000000,1000000)  
PlayerStats = [100,100,100,100]
EnemyStats  = [10000,1000,1000,1000,3]
PlayerInventory = ["Grey Crystal"]  #grey crystal means nothing and is just for the list to initalised
PlayerInventoryAmmount = [1]
WorldText   = "The glass is half full"          #
EnemyText   = "The glass is a stupid question." # Hastag NOTFILLERTEXT
XP   = 0
Gold = 100
Resource1 = "Aircatcher"
Resource1Ammount = 1911

TmpNum = 1          #Overwriten by numbers if needed
TxHlPref = "RESET"  #Text highlighting preference
TxClPref = "RESET"  #Text Color preference
TxBrPref = "NORMAL" #Text brightness preference 

def Menu(): #Handles the mainmenu
    global BuildNumber
    global Debug

    print("Rougalike Game\n\n1) Play\n2) Exit\n\n\nCreated by TMAltair\nGet updates here: http://bit.ly/Rougalike \n\nPress the number/letter in brackets to select your options ")
    if Debug == 1:
        print("BuildNumber = " + BuildNumber)

    while TmpNum == 1:
        if keyboard.is_pressed("1"): 
            WorldGen()
        elif keyboard.is_pressed("2"):
            exit()

def WorldGen():
    global TxBrPref
    global TxClPref
    global TxHlPref
    global WorldText
    global PlayerStats
    global EnemyStats
    global MapX
    global MapY
    global EnemyText
    if Debug == 1:
        time.sleep(0)
    else:  
        os.system("cls")

    TerrainSlots = int(linecache.getline(os.path.dirname(os.path.abspath(__file__)) + "\\Data\\Slots.txt", 1))    #Gets total ammount of terrain
    TerrainID   = random.randint(1,TerrainSlots) #Line Number of Terrain
    Terrain     = linecache.getline(os.path.dirname(os.path.abspath(__file__)) + "\\Data\\Terrain\\Terrain.txt", TerrainID )       #Rolls Terrain
    TerrainBr   = linecache.getline(os.path.dirname(os.path.abspath(__file__)) + "\\Data\\Terrain\\Brightness.txt", TerrainID)     #Gets brightness
    TerrainCl   = linecache.getline(os.path.dirname(os.path.abspath(__file__)) + "\\Data\\Terrain\\Color.txt", TerrainID)          #Gets color
    TerrainIcon = linecache.getline(os.path.dirname(os.path.abspath(__file__)) + "\\Data\\Terrain\\MapIcon.txt", TerrainID)        #Gets map letter
    TerrainIcon = TerrainIcon.strip()
    TerrainIcon = TerrainIcon[0]       #Makes sure its only 1 letter
    TerrainIcon = TerrainIcon.upper()
    Terrain     = Terrain.strip()      #Removes \n
    TerrainBr   = TerrainBr.strip()    #Removes \n
    TerrainCl   = TerrainCl.strip()    #Removes \n
    TerrainText = Fore.__getattribute__(TxClPref) + Back.__getattribute__(TxHlPref) + Style.__getattribute__(TxBrPref) + "You are " + Fore.__getattribute__(TerrainCl) + Style.__getattribute__(TerrainBr) + Terrain + "." + Fore.__getattribute__(TxClPref) + Back.__getattribute__(TxHlPref) + Style.__getattribute__(TxBrPref)

    ResourceSlots = int(linecache.getline(os.path.dirname(os.path.abspath(__file__)) + "\\Data\\Slots.txt", 2))   #Gets total ammount of resource
    Resource1ID = random.randint(1,ResourceSlots) #Rolls Resource
    Resource1Ammount = random.randint(0,10)       #Rolls 
    Resource1 = linecache.getline(os.path.dirname(os.path.abspath(__file__)) + "\\Data\\Resources\\Resources.txt",Resource1ID)    #Gets resource      
    Resource1Br = linecache.getline(os.path.dirname(os.path.abspath(__file__))  + "\\Data\\Resources\\Brightness.txt",Resource1ID) #Gets brightness
    Resource1Cl = linecache.getline(os.path.dirname(os.path.abspath(__file__)) + "\\Data\\Resources\\Color.txt",Resource1ID)       #Gets color
    Resource1   = Resource1.strip()     #Removes \n
    Resource1Br = Resource1Br.strip()   #Removes \n
    Resource1Cl = Resource1Cl.strip()   #Removes \n
    Resource1Text = Fore.__getattribute__(TxClPref) + Back.__getattribute__(TxHlPref) + Style.__getattribute__(TxBrPref) + "There are " + Style.__getattribute__(Resource1Br) + Fore.__getattribute__(Resource1Cl) + str(Resource1Ammount)  + " " + Resource1 + Fore.__getattribute__(TxClPref) + Back.__getattribute__(TxHlPref) + Style.__getattribute__(TxBrPref)  + " here."
    if Resource1Ammount == 0:
        Resource1Text = ""

    EnemySlots = int(linecache.getline(os.path.dirname(os.path.abspath(__file__)) + "\\Data\\Slots.txt",3))
    EnemyID = random.randint(1,EnemySlots)
    EnemyName = linecache.getline(os.path.dirname(os.path.abspath(__file__)) + "\\Data\\Enemys.txt",EnemyID)
    EnemyName = EnemyName.strip()
    EnemyStats = [random.randint(round(PlayerStats[0]/2),PlayerStats[0]),random.randint(round(PlayerStats[1]/4),round(PlayerStats[1]/4*3)),random.randint(round(PlayerStats[2]/2),PlayerStats[2]),random.randint(round(PlayerStats[3]/2),PlayerStats[3]), random.randint(1,2)]
    #EnemyStats index = 0 - Health  1-Attack  2-Defence  3-Speed  4-Magic(1)/Physical(2)
    EnemyText = Fore.RESET + "There is a " + Fore.RED + EnemyName + Fore.RESET + " here."

    WorldText = str(TerrainText) + "\n" + str(Resource1Text) + "\n" + str(EnemyText)
    Display()

def Display():
    global WorldText
    print(WorldText)
    PlayerTurn()
 
def PlayerTurn():
    global PlayerInventory
    global PlayerInventoryAmmount
    global Resource1
    global Resource1Ammount
    print("\n\nOptions:")
    print("1) Battle     2) Move        3) Collect items  4)Inventory")
    print("5) Save/Load  6) Statistics  7) Settings       8) Quit")
    time.sleep(1)
    a = 1
    while a == 1:
        if keyboard.is_pressed("1"):
            Battle()
        elif keyboard.is_pressed("2"):
            Move()
        elif keyboard.is_pressed("3"):
            print("Collect:\n 1) " + Resource1)
            b = 1
            TmpNum = 0
            time.sleep(1)
            while b == 1:
                if keyboard.is_pressed("1"):
                    print("Collected " + str(Resource1Ammount) + " " + str(Resource1))
                    try:
                        PlayerInventory.index(Resource1)    #Checks if player has allready collected this resource
                    except ValueError:
                        TmpNum = 1
                    b = 0
            if TmpNum == 1:
                PlayerInventory = PlayerInventory.append(Resource1)
                PlayerInventoryAmmount = PlayerInventoryAmmount.append(Resource1Ammount)
            else:
                TmpNum = PlayerInventory.index(Resource1)
                PlayerInventoryAmmount[TmpNum] = PlayerInventoryAmmount[TmpNum] + Resource1Ammount
                Display()

        elif keyboard.is_pressed("4"):
            print("You currently have: " + str(PlayerInventory))
        elif keyboard.is_pressed("5"):
            a=1#link to stats
        elif keyboard.is_pressed("6"):
            a=1#link to stats/achivements
        elif keyboard.is_pressed("7"):
            a=1#link to settings
        elif keyboard.is_pressed("8"):
            a=1#quit

def Battle():
    global EnemyText
    global PlayerStats
    global EnemyStats
    global Gold
    global XP
    PlayerBattleStats = PlayerStats
    EnemyBattleStats = EnemyStats
    if Debug == 1:
        time.sleep(0.000000000000000001)
    else:  
        os.system("cls")
    
    print("Your HP: " + str(PlayerStats[0]) + "  Enemy HP: " + str(EnemyStats[0]))
    print(EnemyText + "\n1) Battle  2) Run \n")
    time.sleep(1)

    a = 1
    while a == 1:
        if keyboard.is_pressed("1"):
            a = 2
        elif keyboard.is_pressed("2"):
            BootCheck()

    BattleLoop = 1
    while BattleLoop == 1:
        print("\n1) Attack  2) Magic  3) Defend\n4) Items   5) Run    6) Inspect")
        time.sleep(1)
        AttackLoop = 1
        while AttackLoop == 1:
            if keyboard.is_pressed("1"):    #Attack Command
                AttackLoop = 0
                print("You used a melee attack")
                if EnemyBattleStats[4] == 2:
                    EnemyBattleStats[0] = EnemyBattleStats[0] - random.randint(round(PlayerBattleStats[1] / 2), round(PlayerBattleStats[1] * 2)) - EnemyBattleStats[2]
                    print("You were attacked by the enemy.")
                    PlayerBattleStats[0] = PlayerBattleStats[0] - random.randint(round(EnemyBattleStats[1] / 2), round(EnemyBattleStats[1] * 2)) - PlayerBattleStats[2]                
                else:
                    EnemyBattleStats[0] = EnemyBattleStats[0] - round(PlayerBattleStats[1] / 4)
                    print("You were attacked by the enemy.")
                    PlayerBattleStats[0] = PlayerBattleStats[0] - random.randint(round(EnemyBattleStats[1] / 2), round(EnemyBattleStats[1] * 2)) - PlayerBattleStats[2]
            elif keyboard.is_pressed("2"):  #Magic  Command
                print("You used a magic attack")
                AttackLoop = 0
                if EnemyBattleStats[4] == 1:
                    EnemyBattleStats[0] = EnemyBattleStats[0] - random.randint(round(PlayerBattleStats[1] / 2), round(PlayerBattleStats[1] * 2)) - EnemyBattleStats[2]
                    print("You were attacked by the enemy.")
                    PlayerBattleStats[0] = PlayerBattleStats[0] - random.randint(round(EnemyBattleStats[1] / 2), round(EnemyBattleStats[1] * 2)) - PlayerBattleStats[2]                
                else:
                    EnemyBattleStats[0] = EnemyBattleStats[0] - round(PlayerBattleStats[1] / 4)
                    print("You were attacked by the enemy.")
                    PlayerBattleStats[0] = PlayerBattleStats[0] - random.randint(round(EnemyBattleStats[1] / 2), round(EnemyBattleStats[1] * 2)) - PlayerBattleStats[2]
            elif keyboard.is_pressed("3"):  #Defend Command
                AttackLoop = 0
                Defence = PlayerBattleStats[2] * 1.5
                print("You were attacked by the enemy.")
                PlayerBattleStats[0] = PlayerBattleStats[0] - random.randint(round(EnemyBattleStats[1] / 2), round(EnemyBattleStats[1] * 2)) - PlayerBattleStats[2]
            elif keyboard.is_pressed("4"):
                BattleLoop = 1#put inventory here
            elif keyboard.is_pressed("5"):  #Run     Command
                Display()
            elif keyboard.is_pressed("6"):  #Inspect Command
                AttackLoop = 0
                print("\n       You: HP: " + str(PlayerStats[0]) + "   Attack: " + str(PlayerStats[1]) + "  Defence: " + str(PlayerStats[2]) + " Speed: " + str(PlayerStats[3]))
                print("     Enemy: HP: " + str(EnemyStats[0])  + "    Attack: " + str(EnemyStats[1])  + "   Defence: " + str(EnemyStats[2])  + "  Speed: " + str(EnemyStats[3]))
                print("Difference: HP: " + str(PlayerStats[0] - EnemyStats[0]) + "    Attack: " + str(PlayerStats[1] - EnemyStats[1]) + "   Defence: "+ str(PlayerStats[2] - EnemyStats[2]) + "  Speed: " + str(PlayerStats[3] - EnemyStats[3]))
                time.sleep(1)
                print("You were attacked by the enemy.")
                PlayerBattleStats[0] = PlayerBattleStats[0] - random.randint(round(EnemyBattleStats[1] / 2), round(EnemyBattleStats[1] * 2)) - PlayerBattleStats[2]

        if EnemyBattleStats[0] <= 0:
            if PlayerBattleStats[0] <= 0:
                PlayerBattleStats[0] = 1
            EnemyBattleStats[0]  = 0     
            print("Your HP: " + str(PlayerStats[0]) +  " Enemy HP: " + str(EnemyStats[0]))
            input("You won!\nPress enter to continue")
            BattleLoop = 0
        elif int(PlayerBattleStats[0]) <= 0:
            print("Your HP: " + str(PlayerStats[0]) +  " Enemy HP: " + str(EnemyStats[0]))
            input("You died.\n\nPress enter to restart")
            Menu()
        else:
            print("Your HP: " + str(PlayerStats[0]) +  " Enemy HP: " + str(EnemyStats[0]))
            AttackLoop = 1
    
    Gold = Gold + random.randint(0,1000)
    XP = XP + random.randint(100,250)
    WorldGen()

def Move():
    global MapX
    global MapY
    print("Select a direction to move\n         (1)\n        North\n(4) West     East (2)\n        South\n         (3)")
    time.sleep(1)
    a = 1
    while a == 1:
        if keyboard.is_pressed("1"):
            MapY = MapY + 1
            a = 0
        elif keyboard.is_pressed("2"):
            MapX = MapX + 1
            a = 0
        elif keyboard.is_pressed("3"):
            MapY = MapY - 1
            a = 0
        elif keyboard.is_pressed("4"):
            MapX = MapX - 1
            a = 0
    WorldGen()
    
Menu()