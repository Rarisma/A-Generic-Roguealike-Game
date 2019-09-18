#Created by TMAltair
import linecache #Allows reading lines from files without a load of code
import os        #Does file opperations and other stuff like clearing screen
import random    #Allows random number generation

#Select     - deals with user input Select.upper should allways follow after it                                         #slots.txt lines
#DataPath   - Path to data folder                                                                                       #1 - Terrain
#LoadStage  - Stage of loading                                                                                          #2 - Hostiles
#TempFile   - Current file that needs loading for linecache
#SlotNo     - Picks a random number
#Terrain    - Current Terrain
#Turn       - Current turn
#Character  - Save folder

global Tempfile
TempFile = "A tempory forever"  #He wanted to live forever.
DataPath = os.getcwd()          #Gets file path
DataPath = DataPath + "\\data"  #Leads to data folder
LoadStage = 1
Turn = 0
Character = DataPath + "\\char" 
MapX = random.randint(-100000,100000)
MapY = random.randint(-100000,100000)
PLMXMana = 100
PLMXHealth = 100
PLMXAttack = 100
EXP = 0
PLMana = PLMXMana
PLHealth = PLMXHealth
PLAttack = PLMXAttack

def MainMenu():
    Select = input("Project4\nNew game\n\n")
    Select = Select.upper() #Converts to caps so it cannot be missinterpreted due to case
    if Select == "NEW GAME":
        LoadInit()
    else:
        print("Invalid Command.")
        MainMenu()

def LoadInit():         #Initalises loading 
    global LoadStage    #Makes a global variable editable
    LoadStage = 1       #Sets LoadStage to 1
    Generation()        #Sends to Generation    

def Generation():   #Generates world
    if LoadStage == 1:
        TerrainGen()
    elif LoadStage == 2:
        ResAGen()
    elif LoadStage == 3:
        ResBGen()
    elif LoadStage == 4:
        Creature()
    elif LoadStage == 5:
        display()

def TerrainGen():
    TerrainSlots = 0    #Ammount of slots terrain has (Slots is how many lines of text it has)
    global TempFile
    global SlotNo
    TempFile = DataPath + "\\slots.txt"              #Writes the full path to slots.txt to TempFile
    TerrainSlots = int( linecache.getline(TempFile, 1) )
    SlotNo = random.randint(1,TerrainSlots)         #Picks a random number between 1 and how many slots are in line 1 of slots.txt
    TempFile = DataPath + "\\Terrain.txt"            #Path to terrain.txt
    global Terrain
    Terrain = linecache.getline(TempFile,SlotNo)    #Gets terrain
    global LoadStage
    LoadStage = LoadStage + 1
    Generation()

def ResAGen():  #Generates 1st resource
    ResASlotNo = SlotNo       #Ammount of slots 
    global ResAName
    ResAName  = "UNKNOWN"     #NoTE:So I havce no idea how inventory should work but here is an idea it looks inside a folder called inventory for whatever ResAName when collected it adds the ammount to the number in it if it doesnt exist create it
    TempFile = DataPath + "\\ResA.txt"
    global ResANum
    ResAName = linecache.getline(TempFile,ResASlotNo)
    ResANum = random.randint(1,5)   #Rewrite this one day to make it harder to get higher numbers like rolling a 1 rerolls between 1 and 2 and if its a 2 on roll 1 then it rerolls between 2 and 3
    global LoadStage
    LoadStage = LoadStage + 1
    Generation()

def ResBGen():  #Generates 2nd resource (This is the exact same as ResB)
    ResBSlotNo = SlotNo       #Ammount of slots 
    global ResBName
    ResBName  = "UNKNOWN"     #NoTE:So I havce no idea how inventory should work but here is an idea it looks inside a folder called inventory for whatever ResAName when collected it adds the ammount to the number in it if it doesnt exist create it
    TempFile = DataPath + "\\ResB.txt"
    global ResBNum
    ResBName = linecache.getline(TempFile,ResBSlotNo)
    ResBNum = random.randint(0,10)   #Rewrite this one day to make it harder to get higher numbers like rolling a 1 rerolls between 1 and 2 and if its a 2 on roll 1 then it rerolls between 2 and 3 ect.
    global LoadStage
    LoadStage = LoadStage + 1
    Generation()

def Creature():  #Sorts out Hostiles
    global TempFile
    global SlotNo
    global LoadStage
    global Terrain
    global Enemy
    global EMMana
    global EMHealth
    global EMAttack
    TempFile = DataPath + "\\slots.txt"              #Writes the full path to slots.txt to TempFile
    CreatureSlots = int( linecache.getline(TempFile, 2) )
    SlotNo = random.randint(1,CreatureSlots)         #Picks a random number between 1 and how many slots are in line 1 of slots.txt
    TempFile = DataPath + "\\hostile.txt"            #Path to hostile.txt
    Enemy = linecache.getline(TempFile,SlotNo)     #Gets hostile
    LoadStage = LoadStage + 1
    EMMana = random.randint(1, PLMXMana*1.5)
    EMHealth = random.randint(1, PLMXHealth*1.5)
    EMAttack = random.randint(1, PLMXAttack*1.5)
    Generation()

def display():
    global Turn
    Turn = Turn + 1
    print("You are in",Terrain)
    global ResAName
    global ResBName
    print("There are",ResANum,ResAName)
    print("There are",ResBNum,ResBName)
    PlayerTurn()

def PlayerTurn():   #Player turn
    global Turn
    global Character
    print("There is a",Enemy)
    print("Turn: ",Turn)
    print("Actions:\nMove\nWait\nBattle")
    Select = input()
    Select = Select.upper()
    if Select == "WAIT":
        display()
    elif Select == "MOVE":
        Move()
    elif Select == "BATTLE":
        Battle()
    else:
        print("Invalid command.")
        PlayerTurn()

def Move(): #Remember Add map Perminance
    #Add a check for a file with the maps name
    global MapX
    global MapY
    Select = input("Move in what direction:\nNorth, South, East & West: ")
    Select = Select.upper()
    if Select == "NORTH":
        MapY = MapY + 1
    elif Select == "SOUTH":
        MapY = MapY - 1
    elif Select == "EAST":
        MapX = MapX + 1
    elif Select == "WEST":
        MapX = MapX - 1
    else:
        print("Invalid Command")
        Move()
    LoadInit()

def Battle():
    global PLMana
    global PLHealth
    global PLAttack
    global PLMXMana
    global PLMXHealth
    global PLMXAttack
    global EMMana
    global EMHealth
    global EMAttack
    global EXP
    global Enemy
    PLMana = PLMXMana
    PLHealth = PLMXHealth
    PLAttack = PLMXAttack
    print("There is a",Enemy," Attack / Defend / Flee\n\n Your HP:",PLHealth,"\nEnemy HP:",EMHealth)
    Select = input()
    Select = Select.upper()
    if Select == "ATTACK":
        EMHealth = EMHealth - random.randint(PLAttack/2,PLAttack*2)
        PLHealth = PLHealth - EMAttack
    elif Select == "DEFEND":
        PLHealth = PLHealth - EMHealth / 2
    elif Select == "FLEE":
        display()
    else:
        print("Invalid Command.")

    if EMHealth <= 0 :
        print("Congratulations! You defeated",Enemy)
        MX = EMAttack + EMMana / 2
        EXP = EXP + MX
        display()
    elif PLHealth <= 0:
        print("You died. Press enter to restart")
        input()
        LoadInit()
    else:
        Battle2()

def Battle2():
    global PLMana
    global PLHealth
    global PLAttack
    global PLMXMana
    global PLMXHealth
    global PLMXAttack
    global EMMana
    global EMHealth
    global EMAttack
    global EXP
    global Enemy
    print("There is a",Enemy," Attack / Defend / Flee\n\n Your HP:",PLHealth,"\nEnemy HP:",EMHealth)
    Select = input()
    Select = Select.upper()
    if Select == "ATTACK":
        EMHealth = EMHealth - random.randint(PLAttack/2,PLAttack*2)
        PLHealth = PLHealth - EMAttack
    elif Select == "DEFEND":
        PLHealth = PLHealth - EMHealth / 2
    elif Select == "FLEE":
        display()
    else:
        print("Invalid Command.")

    if EMHealth <= 0 :
        print("Congratulations! You defeated",Enemy)
        MX = EMAttack + EMMana / 2
        EXP = EXP + MX
        display()
    elif PLHealth <= 0:
        print("You died. Press enter to restart")
        input()
        LoadInit()
    else:
        Battle2()



MainMenu()