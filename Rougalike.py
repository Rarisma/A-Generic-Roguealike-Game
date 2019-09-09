#Created by TMAltair
import linecache #Allows reading lines from files without a load of code
import os        #Does file opperations and other stuff like clearing screen
import random    #Allows random number generation

#Select     - deals with user input Select.upper should allways follow after it                                         #slots.txt lines
#DataPath   - Path to data folder                                                                                       #1 -Terrain
#LoadStage  - Stage of loading                                                                                          #2 -Resource A
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

def MainMenu():
    Select = input("Project4\nNew game\n\n")
    Select = Select.upper() #Converts to caps so it cannot be missinterpreted due to case
    if Select == "NEW GAME":
        CharCreate()
    else:
        print("Invalid Command.")
        MainMenu()

def CharCreate():
    global Name
    global MXMana
    global MXHealth
    global MXStamina
    global MXSpeed
    Name = input("Enter your name: ")
    while LoadStage == 1:        
        Stat = input("Pick your starting stat boost (Health/Mana/Stamina/Speed) ")
        Stat = Stat.upper()
        if Stat == "HEALTH":
            MXHealth = 125
            MXMana = 100
            MXStamina = 100
            MXSpeed = 100
            LoadInit()
        elif Stat == "MANA":
            MXHealth = 100
            MXMana = 125
            MXStamina = 100
            MXSpeed = 100
            LoadInit()        
        elif Stat == "STAMINA":
            MXHealth = 100
            MXMana = 100
            MXStamina = 125
            MXSpeed = 100
            LoadInit()
        elif Stat == "SPEED":
            MXHealth = 100
            MXMana = 100
            MXStamina = 100
            MXSpeed = 125
            LoadInit()
        else:
            print("Invalid stat, Please pick Health/Mana/Stamina/Speed please")


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

    print("Turn: ",Turn)
    print("Actions:\nMove\nWait")
    Select = input()
    Select = Select.upper()
    if Select == "WAIT":
        display()
    elif Select == "MOVE":
        
        LoadInit()
    else:
        print("Invalid command.")
        PlayerTurn()

MainMenu()
