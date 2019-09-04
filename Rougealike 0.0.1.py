    #Project4 MKII - Created by TMAltair
#Found out that linecache would be way better 
import linecache #Allows reading lines from files without a load of code
import os        #Does file opperations and other stuff like clearing screen
import random    #Allows random number generation

#Select     - deals with user input Select.upper should allways follow after it                                         #slots.txt lines
#DataPath   - Path to data folder                                                                                       #1 -Terrain
#LoadStage  - Stage of loading                                                                                          #2 -Resource A
#TempFile   - Current file that needs loading for linecache
#SlotNo     - Picks a random number
#Terrain    - Current Terrain

DataPath = os.getcwd()        #Gets file path
DataPath = DataPath + "\data" #Leads to data folder
LoadStage = 1

def MainMenu():
    Select = input("Project4\nNew game\n\n")
    Select = Select.upper() #Converts to caps so it cannot be missinterpreted due to case
    if Select == "NEW GAME":
        global LoadStage    #Makes a global variable editable
        LoadStage = 1       #Sets LoadStage to 1
        Generation()        #Sends to Generation
    else:
        print("Invalid Command.")
        MainMenu()

def Generation():   #Generates world
    if LoadStage == 1:
        TerrainGen()
    elif LoadStage == 2:
        ResAGen()
    elif LoadStage == 3:
        global Reload
        Reload = 1
        display()

def TerrainGen():
    TerrainSlots = 0    #Ammount of slots terrain has (Slots is how many lines of text it has)
    global Tempfile
    global SlotNo
    TempFile = DataPath + "\slots.txt"              #Writes the full path to slots.txt to TempFile
    TerrainSlots = int( linecache.getline(TempFile, 1) )
    SlotNo = random.randint(1,TerrainSlots)         #Picks a random number between 1 and how many slots are in line 1 of slots.txt
    TempFile = DataPath + "\Terrain.txt"            #Path to terrain.txt
    global Terrain
    Terrain = linecache.getline(TempFile,SlotNo)    #Gets terrain
    global LoadStage
    LoadStage = LoadStage + 1
    Generation()

def ResAGen():  #Generates 1st resource
    ResASlotNo = SlotNo       #Ammount of slots 
    ResAName  = "UNKNOWN"     #NoTE:So I havce no idea how inventory should work but here is an idea it looks inside a folder called inventory for whatever ResAName when collected it adds the ammount to the number in it if it doesnt exist create it
    TempFile = DataPath + "\ResA.txt"
    global ResANum
    ResAName = linecache.getline(TempFile,ResASlotNo)
    ResANum = random.randint(1,5)   #Rewrite this one day to make it harder to get higher numbers like rolling a 1 rerolls between 1 and 2 and if its a 2 on roll 1 then it rerolls between 2 and 3
    global LoadStage
    LoadStage = LoadStage + 1
    Generation()

def display():  #It took AEONS to get this to work.
    print("You are in",Terrain)
    print("There are",ResANum)

    global Reload
    if Reload == 0: #Room loads incorrectly on 1st try so it reloads the exact same room
        Reload = 1  #Stops a reload loop
        display()











MainMenu() #Not enough time to see everything he wanted to see, He wanted to live forever so this is how it will be. - Somone