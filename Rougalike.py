BuildNumber = "0.5.1 Nov/23/11/19"
Debug = 1   #1 = true anything else = false

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
        from colorama import Fore, Back, Style
    except ImportError:
        TMPTXT = TMPTXT + " colorama"

    if TMPTXT == "":
        print("")
    else:
        input("You are missing required modules.\nPlease use this command in comand prompt to fix this\npip install" + TMPTXT)

#Fore.__getattribute__(TxClPref) + Back.__getattribute__(TxHlPref) + Style.__getattribute__(TxBrPref) 
#This is the color prefs 

BootCheck()
import time         #allows delays
import keyboard     #Key reading
import random       #random number gen
import os           #eh idk
import linecache    #quick file reading
import json         #allows saves
from colorama import Fore, Back, Style, init    #C O L O U R
from tkinter import filedialog                  #U S E L E S S
init(convert=True)  #Allows CMD and Powershell to display colors instead of the acsii code or whatever garbled text s/21A is

MapX = random.randint(-1000000,1000000)
MapY = random.randint(-1000000,1000000)  
PlayerStats = [50,50,50,50]
EnemyStats  = [10000,1000,1000,1000,3]
PlayerInventory = ["Grey Crystal"]  #grey crystal means nothing and is just for the list to initalised
PlayerInventoryAmmount = [1]
WorldText   = "The glass is half full"          #
EnemyText   = "The glass is a stupid question." # Hastag NOTFILLERTEXT
XP   = 0
Gold = 100
level = 1
Resource1 = "Aircatcher"    # My parachutes forgot me
Resource1Ammount = 1911
TurnCount = 0
Resource1Text = "Creative expression"
TerrainMonolith = 0
TerrainMonolithType = 0

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
    global Resource1
    global Resource1Ammount
    global Resource1Text
    global TerrainMonolithType
    global TerrainMonolith
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
    TerrainMonolith = 0
    TerrainText = Fore.__getattribute__(TxClPref) + Back.__getattribute__(TxHlPref) + Style.__getattribute__(TxBrPref) + "You are " + Fore.__getattribute__(TerrainCl) + Style.__getattribute__(TerrainBr) + Terrain + "." + Fore.__getattribute__(TxClPref) + Back.__getattribute__(TxHlPref) + Style.__getattribute__(TxBrPref)


    if random.randint(1,20) == 20:
        TerrainMonolith = random.randint(1,100)     #Stat increase
        TerrainMonolithType = random.randint(1,10)  #Abilitys of monolith
        Monolith()

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
    EnemyStats = [random.randint(round(PlayerStats[0]/4*3),PlayerStats[0]*2),random.randint(round(PlayerStats[1]/4*3),round(PlayerStats[1]/4*3)),random.randint(round(PlayerStats[2]/4*3),PlayerStats[2]*2),random.randint(round(PlayerStats[3]/4*3),PlayerStats[3]*2), random.randint(1,2)*2]
    #EnemyStats index = 0 - Health  1-Attack  2-Defence  3-Speed  4-Magic(1)/Physical(2)
    EnemyText = Fore.RESET + "There is a " + Fore.RED + EnemyName + Fore.RESET + " here."

    WorldText = str(TerrainText) + "\n" + str(Resource1Text) + "\n" + str(EnemyText)
    Display()

def Display():
    global WorldText
    print(WorldText)
    PlayerTurn()

def Monolith():
    global TerrainMonolith
    global TerrainMonolithType
    global PlayerStats
    print("TerrainMonolithType: " + str(TerrainMonolithType) + "\nYou are at a monolith.\nYou feel like you could use some of the monoliths power to:")
    time.sleep(1)
    if TerrainMonolithType >= 1:
        print("1) Improve a stat")
    if TerrainMonolithType >= 5:
        print("2) Level up")
    if TerrainMonolithType >= 10:
        print("3) Unlock the power of the monolith")
    
    a = 1
    while a == 1:
        if keyboard.is_pressed("1") and TerrainMonolithType >= 1:
            print("Improve which stat?\n1)HP\n2)Attack\n3)Defence\n4)Speed")
            time.sleep(1)
            while a == 1:
                if keyboard.is_pressed("1"):
                    PlayerStats[0] = PlayerStats[0] + TerrainMonolith
                    print("Improved HP by " + str(TerrainMonolith) + " points.\nOld " + str(PlayerStats[0] - TerrainMonolith) + "   New: " + str(PlayerStats[0]))
                    input("Press enter to continue")                    
                    WorldGen()
                elif keyboard.is_pressed("2"):
                    PlayerStats[1] = PlayerStats[1] + TerrainMonolith
                    print("Improved Attack by " + str(TerrainMonolith) + " points.\nOld " + str(PlayerStats[1] - TerrainMonolith) + "   New: " + str(PlayerStats[1]))
                    input("Press enter to continue")                    
                    WorldGen()
                elif keyboard.is_pressed("3"):
                    PlayerStats[2] = PlayerStats[2] + TerrainMonolith
                    print("Improved Defence by " + str(TerrainMonolith) + " points.\nOld " + str(PlayerStats[2] - TerrainMonolith) + "   New: " + str(PlayerStats[2]))
                    input("Press enter to continue")                    
                    WorldGen()
                if keyboard.is_pressed("4"):
                    PlayerStats[3] = PlayerStats[3] + TerrainMonolith
                    print("Improved Speed by " + str(TerrainMonolith) + " points.\nOld " + str(PlayerStats[3] - TerrainMonolith) + "   New: " + str(PlayerStats[3]))
                    input("Press enter to continue")
                    WorldGen()
        elif keyboard.is_pressed("2") and TerrainMonolithType >= 5:
            global XP
            global level
            print("\nYou leveled up!\nYour stats have improved!\n")
            print("Old Stats: HP: " + str(PlayerStats[0]) + "   Attack: " + str(PlayerStats[1]) + "  Defence: " + str(PlayerStats[2]) + " Speed: " + str(PlayerStats[3]))
            PlayerStats[0] = PlayerStats[0] + random.randint(5,50)
            PlayerStats[1] = PlayerStats[1] + random.randint(5,50)
            PlayerStats[2] = PlayerStats[2] + random.randint(5,50)
            PlayerStats[3] = PlayerStats[3] + random.randint(5,50)
            print("New Stats: HP: " + str(PlayerStats[0]) + "   Attack: " + str(PlayerStats[1]) + "  Defence: " + str(PlayerStats[2]) + " Speed: " + str(PlayerStats[3]))
            level = level + 1
            XP = 0
            input("Press enter to continue")
            WorldGen()
        elif keyboard.is_pressed("3") and TerrainMonolithType >= 10:
            if level >= 10:
                print("The monolith aknowledges your power.\nHowever this isn't implemented yet.\nWell take a 10K increase in all your stats +  1 million gold")
                PlayerStats[0] + 10000
                PlayerStats[1] + 10000
                PlayerStats[2] + 10000
                PlayerStats[3] + 10000
                global Gold
                Gold = Gold + 1000000
                XP = -10000
                input("Press enter to continue")
                WorldGen()            
            else:
                print("The monolith does not recognise your power.")
                input("Press enter to continue")
                WorldGen()

def PlayerTurn():
    global PlayerInventory
    global PlayerInventoryAmmount
    global Resource1
    global Resource1Ammount
    global TurnCount
    TurnCount = TurnCount + 1
    print("Turn: " + str(TurnCount) + "\n\nOptions:\n1) Battle     2) Move        3) Collect items  4) Inventory\n5) Save/Load  6) Statistics  7) Settings       8) Quit")
  
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
            print("You currently have: " + str(PlayerInventory) + "\nAmmounts: " + str(PlayerInventoryAmmount))
            time.sleep(1)
            PlayerTurn()
        elif keyboard.is_pressed("5"):
            SaveLoad()
        elif keyboard.is_pressed("6"):
            a=1#link to stats/achivements
        elif keyboard.is_pressed("7"):
            a=1#link to settings
        elif keyboard.is_pressed("8"):
            a=1#quit

def SaveLoad(): #No clue how this works just copy and paste 
    #Do not try and change code here
    global PlayerInventory
    global PlayerInventoryAmmount
    print("\n1) Save\n2) Load")
    a = 1
    while a == 1:
        if keyboard.is_pressed("1"):
            destination = os.path.dirname(os.path.abspath(__file__)) + "\\Data\\PlayerData\\Slot1\\PlayerInventory.json"
            with open(destination, "w") as file:
                json.dump(PlayerInventory, file)

            destination = os.path.dirname(os.path.abspath(__file__)) + "\\Data\\PlayerData\\Slot1\\PlayerInventoryAmmount.json"
            with open(destination, "w") as file:
                json.dump(PlayerInventoryAmmount, file)
            
            print("Saved to Slot 1\n\n")
            Display()

        elif keyboard.is_pressed("2"):
            destination = os.path.dirname(os.path.abspath(__file__)) + "\\Data\\PlayerData\\Slot1\\PlayerInventory.json"
            with open(destination) as file:
                PlayerInventory = json.load(file)

            destination = os.path.dirname(os.path.abspath(__file__)) + "\\Data\\PlayerData\\Slot1\\PlayerInventoryAmmount.json"
            with open(destination) as file:
                PlayerInventoryAmmount = json.load(file)

            print("Loaded Slot 1\n\n")
            WorldGen()
            
def Battle():
    global EnemyText
    global PlayerStats
    global EnemyStats
    global Gold
    global XP
    global level
    PlayerBattleStats = PlayerStats
    EnemyBattleStats = EnemyStats
    if Debug == 1:
        time.sleep(0.000000000000000001)
    else:  
        os.system("cls")
    
    print("Your HP: " + str(PlayerStats[0]) + "  Enemy HP: " + str(EnemyStats[0]))

    BattleLoop = 1
    while BattleLoop == 1:
        print("\n1) Attack  2) Magic  3) Defend\n4) Items   5) Run    6) Inspect\n")
        time.sleep(1)
        AttackLoop = 1
        while AttackLoop == 1:
            if keyboard.is_pressed("1"):    #Attack Command
                AttackLoop = 0
                print("You used a melee attack")
                if EnemyBattleStats[4] == 2:
                    EnemyBattleStats[0] = EnemyBattleStats[0] - random.randint(round(EnemyBattleStats[1] / 4), EnemyBattleStats[1]) - EnemyBattleStats[2]
                else:
                    EnemyBattleStats[0] = EnemyBattleStats[0] - round(PlayerBattleStats[1] / 8)
                    print("You were attacked by the enemy.")
            elif keyboard.is_pressed("2"):  #Magic  Command
                AttackLoop = 0
                if EnemyBattleStats[4] == 1:
                    EnemyBattleStats[0] = EnemyBattleStats[0] - random.randint(round(EnemyBattleStats[1] / 4), EnemyBattleStats[1]) - EnemyBattleStats[2]
                else:
                    EnemyBattleStats[0] = EnemyBattleStats[0] - round(PlayerBattleStats[1] / 4)
            elif keyboard.is_pressed("3"):  #Defend Command
                AttackLoop = 0
                Defence = PlayerBattleStats[2] * 1.5
            elif keyboard.is_pressed("4"):
                BattleLoop = 1#put inventory here
            elif keyboard.is_pressed("5"):  #Run Command
                Display()
            elif keyboard.is_pressed("6"):  #Inspect Command
                AttackLoop = 0
                print("\n       You: HP: " + str(PlayerStats[0]) + "   Attack: " + str(PlayerStats[1]) + "  Defence: " + str(PlayerStats[2]) + " Speed: " + str(PlayerStats[3]))
                print("     Enemy: HP: " + str(EnemyStats[0])  + "    Attack: " + str(EnemyStats[1])  + "   Defence: " + str(EnemyStats[2])  + "  Speed: " + str(EnemyStats[3]))
                print("Difference: HP: " + str(PlayerStats[0] - EnemyStats[0]) + "    Attack: " + str(PlayerStats[1] - EnemyStats[1]) + "   Defence: "+ str(PlayerStats[2] - EnemyStats[2]) + "  Speed: " + str(PlayerStats[3] - EnemyStats[3]))
                time.sleep(1)

        if EnemyBattleStats[0] <= 0:
            if PlayerBattleStats[0] <= 0:
                PlayerBattleStats[0] = 1
            EnemyBattleStats[0]  = 0     
            print("Your HP: " + str(PlayerStats[0]) +  " Enemy HP: " + str(EnemyStats[0]))
            print("You won!")
            BattleLoop = 0
        elif int(PlayerBattleStats[0]) <= 0:
            print("Your HP: " + str(PlayerStats[0]) +  " Enemy HP: " + str(EnemyStats[0]))
            input("You died.\n\nPress enter to restart")
            BootCheck()
        else:
            EmAttack = random.randint(round(EnemyBattleStats[1] / 2), EnemyBattleStats[1]) - random.randint(round(PlayerBattleStats[2]/2),PlayerBattleStats[2]) 
            if EmAttack <= 0:
                print("Enemy Attack did no damage")
            else:
                PlayerBattleStats[0] = PlayerBattleStats[0] - EmAttack
                print("Enemy attack did " + str(EmAttack) + " Damage")
            print("Your HP: " + str(PlayerStats[0]) +  " Enemy HP: " + str(EnemyStats[0]))
            AttackLoop = 1
    
    Gold = Gold + random.randint(0,500)
    XP = XP + random.randint(100,250)
    print("XP: " + str(XP) + " (lvl: " + str(level)+ ")" + "\nGold: " + str(Gold))

    if round(XP/1000) >= level:
        print("\nYou leveled up!\nYour stats have improved!\n")
        print("Old Stats: HP: " + str(PlayerStats[0]) + "   Attack: " + str(PlayerStats[1]) + "  Defence: " + str(PlayerStats[2]) + " Speed: " + str(PlayerStats[3]))
        PlayerStats[0] = PlayerStats[0] + random.randint(5,50)
        PlayerStats[1] = PlayerStats[1] + random.randint(5,50)
        PlayerStats[2] = PlayerStats[2] + random.randint(5,50)
        PlayerStats[3] = PlayerStats[3] + random.randint(5,50)
        print("New Stats: HP: " + str(PlayerStats[0]) + "   Attack: " + str(PlayerStats[1]) + "  Defence: " + str(PlayerStats[2]) + " Speed: " + str(PlayerStats[3]))
        level = level + 1
        XP = 0
        BonusGold = random.randint(level*100,level*1000)
        print("\nYou recived " + str(BonusGold) + " gold for leveling up to level " + str(level) + "!")
    input("Press enter to continue.")
    WorldGen()

def Collect():
    global PlayerInventory
    global PlayerInventoryAmmount
    global Resource1
    global Resource1Ammount
    global Resource1Text
    if Resource1Text == "":
        print("Theres nothing here to collect!\n")
        Display()

    print("Collect:\n1) " + str(Resource1) + " ("+ str(Resource1Ammount) +")")
    time.sleep(1)
    a = 1
    while a == 1:  
        if keyboard.is_pressed("1"):
                ItemCount = 1
                a = 0

    if ItemCount ==  1:
        if Resource1 in PlayerInventory:
            PlayerInventoryAmmount[PlayerInventory.index(Resource1)] = PlayerInventoryAmmount[PlayerInventory.index(Resource1)] + Resource1Ammount
        else:
            PlayerInventoryAmmount.append(Resource1Ammount)
            PlayerInventory.append(Resource1)

    time.sleep(1)
    print("")
    Display()

def Move():
    global MapX
    global MapY
    print("\nSelect a direction to move\n         (1)\n        North\n(4) West     East (2)\n        South\n         (3)")
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