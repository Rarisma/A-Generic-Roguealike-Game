SystemStats = [0,"0.7.1 Dec/24/12/19"] # 0 - Debug  1 - BuildDate/Version
def BootCheck():    #Starts up and checks required modules are installed
    try:
        import keyboard
        from colorama import Fore, Back, Style, init
    except ImportError:
        input("You are missing the required modules\nPlease run this command to in Powershell or Command Prompt to continue.")

BootCheck()
import time
import keyboard
import random
import os      
import linecache
import json
import threading
from colorama import Fore, Back, Style, init    #C O L O U R
init(convert=True)  #Allows CMD and Powershell to display colors instead of the acsii codes


WorldStats = [random.randint(-2147483500,2147483500),random.randint(-2147483500,2147483500),1]    #0-X coord 1- Y coord  2 - Difficulty
EnemyStats  = [50,50,50,50,3]
PlayerInventory = []
PlayerInventoryAmmount = []
PlayerGeneral = [0,0,1] # 0 - XP   1 - Gold   2 - Level
PlayerMaxStats = [50,50,50]  #0-HP 1-Attack 2-Defence
EnemyStats = [0,0,0]
Resource1Ammount = 0
TurnCount        = 0
AlternateTerrain = 0
WorldText     = "ERROR"
EnemyText     = "ERROR"
Resource1Text = "ERROR"
Resource1     = "ERROR"
PlayerHealingItems = ["Basic Healing Potion","Advanced Healing Potion"]
PlayerHealingItemsAmmount = [0,0]
Z = 0
PlayerInventoryArmourRes = []
PlayerInventoryArmour = []
PlayerInventoryArmourDef = []
EquipedArmour = "Nothing"   #Name of armour
EquipedArmourDef = 0 #Defence increase
EquipedArmourRes = 0 #Durabilty
PlayerInventoryWeapon = []
PlayerInventoryWeaponAtk = []
PlayerInventoryWeaponRes = []
PlayerInventoryWeaponCrt = []
PlayerInventoryWeaponhit = []
EquipedWeapon = "Hands"
EquipedWeaponhit = 100
EquipedWeaponatk = 0
EquipedWeaponcrt = 0
EquipedWeaponres = 0
#Nickolas Bourbaki?

if SystemStats[0] == 1:
    print("\nYou are in developer mode.\nScreens will not be cleared\n" + Fore.RED + "DO NOT SUBMIT BUG REPORTS WITH THIS ENABLED\nTo disable developer mode change SystemStats[0] to 0" + Fore.RESET + "\n\n")

def Menu(): #Handles the mainmenu   
    global SystemStats
    global WorldStats
    print("Rougalike Game\n\n1) Play\n2) Load\n3) Exit\n\n\nCreated by TMAltair\nGet updates here: http://bit.ly/Rougalike \n\nPress the number/letter in brackets to select your options ")
    if SystemStats[0] == 1:
        print(Fore.RED+ "YOU ARE IN DEVELOPER MODE.\nBuildNumber = " + str(SystemStats[1]) + Fore.RESET)
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
                    B = 0
                elif keyboard.is_pressed("L"):
                    WorldStats[2] = 4
                    B = 0
            
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
        elif keyboard.is_pressed("4"):
            global AlternateTerrain
            AlternateTerrain = int(input("Select a number"))
            AlternateTerrains()

def WorldGen(): #generates terrain
    global WorldText
    global EnemyStats
    global WorldStats
    global EnemyText
    global Resource1
    global Resource1Ammount
    global Resource1Text
    global AlternateTerrain
    
    AlternateTerrain = random.randint(0,50)
    if AlternateTerrain <= 4:
        AlternateTerrains()

    if SystemStats != 1:
        os.system("cls")

    TerrainSlots = int(linecache.getline(os.path.dirname(os.path.abspath(__file__)) + "\\Data\\Slots.txt", 1))    #Gets total ammount of terrain
    TerrainID    = random.randint(1,TerrainSlots) #Line Number of Terrain
    Terrain      = linecache.getline(os.path.dirname(os.path.abspath(__file__)) + "\\Data\\Terrain\\Terrain.txt", TerrainID)       #Rolls Terrain
    TerrainBr    = linecache.getline(os.path.dirname(os.path.abspath(__file__)) + "\\Data\\Terrain\\Brightness.txt", TerrainID)     #Gets brightness
    TerrainCl    = linecache.getline(os.path.dirname(os.path.abspath(__file__)) + "\\Data\\Terrain\\Color.txt", TerrainID)          #Gets color
    Terrain      = Terrain.strip()      #Removes \n
    TerrainBr    = TerrainBr.strip()    #Removes \n
    TerrainCl    = TerrainCl.strip()    #Removes \n
    try:    #Stops crashes
        TerrainText  = "You are " + Fore.__getattribute__(TerrainCl) + Style.__getattribute__(TerrainBr) + Terrain + "." + Fore.RESET + Back.RESET
    except AttributeError:
        WorldGen()
    TerrainText  = "You are " + Fore.__getattribute__(TerrainCl) + Style.__getattribute__(TerrainBr) + Terrain + "." + Fore.RESET + Back.RESET

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

    EnemySlots = int(linecache.getline(os.path.dirname(os.path.abspath(__file__)) + "\\Data\\Slots.txt",3))
    EnemyID = random.randint(1,EnemySlots)
    EnemyName = linecache.getline(os.path.dirname(os.path.abspath(__file__)) + "\\Data\\Enemys.txt",EnemyID)
    EnemyText = Fore.RESET + "There is a " + Fore.RED + str(EnemyName.strip()) + Fore.RESET + " here."

    TerLen = len(TerrainText)
    Re1Len = len(Resource1Text)
    EneLen = len(EnemyText)

    MapLen = []
    MapLen.append(len(TerrainText))
    MapLen.append(len(Resource1Text))
    MapLen.append(len(EnemyText))
    MaxLen = max(MapLen)

    WorldText = str(TerrainText) + "\n" + str(Resource1Text) + "\n" + str(EnemyText)
    if Resource1Text == "":
        WorldText = str(TerrainText) + "\n" + str(EnemyText)

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

    if SystemStats != 1:
        os.system("cls")

    TurnCount = TurnCount + 1
    print(Fore.RESET + Style.RESET_ALL +"Turn: " + str(TurnCount) + "\n" + WorldText + Fore.RESET + Style.RESET_ALL + "\n\n\nOptions:\n1) Battle     2) Move  3) Collect items  4) Inventory\n5) Save/Load  6) Map   7) Settings       8) Quit")
  
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
            print("Select a catagory to display:\n\n1) Items    3) Armour\n2) Potions  4) Weapons")
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
                        armourSelect = input("Type the id of an armour to equip it (or type leave with no capitals to leave)\n")
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
            print("\n1) Save\n2) Load")
            while A == 0:
                if keyboard.is_pressed("1"):
                    Save()
                elif keyboard.is_pressed("2"):
                    Load()
        
        elif keyboard.is_pressed("6"):
            print("\n#  #  #  #  #  #  #  #  #  #  #  #  #  #  #\n#  #  #  #  #  #  #  #  #  #  #  #  #  #  #\n#  #  #  #  #  #  #  @  #  #  #  #  #  #  #\n#  #  #  #  #  #  #  #  #  #  #  #  #  #  #\n#  #  #  #  #  #  #  #  #  #  #  #  #  #  #\n")
            TurnCount = TurnCount - 1
            time.sleep(1)
            PlayerTurn()

        elif keyboard.is_pressed("7"):
            a=1
        elif keyboard.is_pressed("8"):
            print(Fore.RED + "Unless you have saved all data will be lost." + Fore.RESET + "\nAre you sure? (Y/N)")
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
    Loop = 1

    if SystemStats != 1:
        os.system("cls")

    if AlternateTerrain == 1:   #Monolith
        TerrainMonolith = random.randint(1,50)         #Stat increase
        TerrainMonolithType = random.randint(1,110)  #Abilitys of monolith
        print("You are at a monolith.\n1) Read the monolith")

        if PlayerGeneral[2] >= 25:
            print("You feel you could unlock the power of the monolith.\n2) Unlock the monothlith")
        
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
                        WorldGen()
                Battle()
    #0-HP 1-Attack 2-Defence
    elif AlternateTerrain == 2: #Caves
        Risk = 0
        RskTxt = "None"
        LayersDeep = 0
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
                RskTxt = Fore.RED + "COLASPE IMMINENT." + Fore.RESET
            elif Risk >= 75:
                RskTxt ="Risk: " + Fore.RED + "High" + Fore.RESET
            elif Risk >= 50:
                RskTxt ="Risk: " + Fore.YELLOW + "Medium" + Fore.RESET
            elif Risk >= 25:
                RskTxt ="Risk: " + Fore.BLUE + "Low" + Fore.RESET
            elif Risk >= 0: 
                RskTxt ="Risk: " + Fore.CYAN + "None" + Fore.RESET
            print("\nYou are in a cave\n\nThere are: \n" + str(CaveResourcesAmmount[1]) + " KG of " + CaveResources[1] + "\n" + str(CaveResourcesAmmount[2]) + " KG of " + CaveResources[2] + "\n" + str(CaveResourcesAmmount[3]) + " KG of " + CaveResources[3] + "\n" + str(CaveResourcesAmmount[4]) + " KG of " + CaveResources[4] + "\n" + str(CaveResourcesAmmount[5]) + " KG of " + CaveResources[5] + "\n" + RskTxt + "\n\nOptions:\n1) Collect\n2) Explore deeper\n3) Leave\n4) Guide")
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
        print("You are at a village\n1) Use Workbench\n2) Shop\n3) leave")
        tm = 1
        time.sleep(1)
        while tm == 1:
            if keyboard.is_pressed("1"):    #Workbench code
                
                A = 1
                time.sleep(1)
                while A == 1:  

                    if SystemStats[0] != 1:
                        os.system("cls")

                    print("What do you want to craft\n1) Items\n2) Armour\n3) Weapons")
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

                    F = 1
                    while F == 1:
                        CraftingRequiredResource = [""]
                        CraftingRequiredAmmount  = [""]
                        CraftingProduct          = [""]
                        CraftingProductInternal  = [""]
                        
                        CraftingSlots = int(linecache.getline(os.path.dirname(os.path.abspath(__file__)) + "\Data\Terrain\AlternateTerrains\Villages\Slots.txt",CraftSlotLine))
                        Temp = 1

                        while CraftingSlots >= Temp:   #Gets crafing data
                            CraftingRequiredResource.append(linecache.getline(os.path.dirname(os.path.abspath(__file__)) + "\Data\Terrain\AlternateTerrains\Villages\WorkBench\\" + str(Craft) + "\\Material.txt",Temp))
                            CraftingRequiredResource[Temp] = CraftingRequiredResource[Temp].strip()

                            CraftingRequiredAmmount.append(int(linecache.getline(os.path.dirname(os.path.abspath(__file__)) + "\Data\Terrain\AlternateTerrains\Villages\WorkBench\\" + str(Craft) + "\\Ammount.txt",Temp)))

                            CraftingProduct.append(linecache.getline(os.path.dirname(os.path.abspath(__file__)) + "\Data\Terrain\AlternateTerrains\Villages\WorkBench\\" + str(Craft) + "\\Product.txt",Temp))
                            CraftingProduct[Temp] = CraftingProduct[Temp].strip()
                            
                            CraftingProductInternal.append(CraftingProduct[Temp].upper()) 

                            Temp = Temp + 1

                        RedText   =  Fore.RED + ""
                        GreenText = Fore.GREEN + ""
                        Temp = 1

                        while CraftingSlots >= Temp:
                            if CraftingRequiredResource[Temp] in PlayerInventory:
                                if int(CraftingRequiredAmmount[Temp]) <= int(PlayerInventoryAmmount[PlayerInventory.index(CraftingRequiredResource[Temp])]):
                                    GreenText = GreenText + "\n" + CraftingProduct[Temp] + " - Requires: " + CraftingRequiredResource[Temp] + " (" + str(PlayerInventoryAmmount[PlayerInventory.index(CraftingRequiredResource[Temp])]) + " / " + str(CraftingRequiredAmmount[Temp]) + ")"
                                else:
                                    RedText = RedText + "\n" + CraftingProduct[Temp] + " - Requires: " + CraftingRequiredResource[Temp] + " (" + str(PlayerInventoryAmmount[PlayerInventory.index(CraftingRequiredResource[Temp])]) + " / " + str(CraftingRequiredAmmount[A]) +  ")"
                            else:
                                RedText = RedText + "\n" + CraftingProduct[Temp] + " - Requires: " + CraftingRequiredResource[Temp] + " (0 / " + str(CraftingRequiredAmmount[Temp]) + " )"

                            temp2 = 0
                            Temp = Temp + 1

                        RedText = RedText + Fore.RESET
                        GreenText = GreenText + Fore.RESET

                        E = 1
                        if SystemStats[0] != 1:
                            os.system("cls")
                        while E == 1:


                            print(GreenText + RedText)
                            CraftingSelect = input("Type the name of a product to craft it (or type leave to leave)\n")
                            CraftingSelect = CraftingSelect.upper()

                            if CraftingSelect == "LEAVE":
                                AlternateTerrains()

                            if CraftingSelect in CraftingProductInternal:   #looks for product
                                if CraftingRequiredResource[CraftingProductInternal.index(CraftingSelect)] in PlayerInventory:  #check player has the required material
                                    if CraftingRequiredAmmount[CraftingRequiredResource.index(CraftingRequiredResource[CraftingProductInternal.index(CraftingSelect)])] <= PlayerInventoryAmmount[PlayerInventory.index(PlayerInventory[CraftingRequiredResource.index(CraftingRequiredResource[CraftingProductInternal.index(CraftingSelect)])])]: # checks player has enoguh required
                                        E = 0
                                        PlayerInventoryAmmount[PlayerInventory.index(CraftingRequiredResource[CraftingProductInternal.index(CraftingSelect)])] = PlayerInventoryAmmount[PlayerInventory.index(CraftingRequiredResource[CraftingProductInternal.index(CraftingSelect)])] -  CraftingRequiredAmmount[CraftingRequiredResource.index(CraftingRequiredResource[CraftingProductInternal.index(CraftingSelect)])]
                                        
                                        if PlayerInventoryAmmount[PlayerInventory.index(CraftingRequiredResource[CraftingProductInternal.index(CraftingSelect)])] <= 0: #checks if the item is now 0
                                            PlayerInventory.pop(PlayerInventoryAmmount.index(PlayerInventoryAmmount[PlayerInventory.index(CraftingRequiredResource[CraftingProductInternal.index(CraftingSelect)])]))
                                            PlayerInventoryAmmount.pop(PlayerInventoryAmmount.index(PlayerInventoryAmmount[PlayerInventory.index(PlayerInventory[CraftingRequiredResource.index(CraftingRequiredResource[CraftingProductInternal.index(CraftingSelect)])])]))
                                            
                                        if CraftMode == 0: #Adds item to inventory
                                            if CraftingProduct[CraftingRequiredResource.index(CraftingRequiredResource[CraftingProductInternal.index(CraftingSelect)])] in PlayerInventory: # Checks if player has the product already
                                                PlayerInventory.append(CraftingProduct[CraftingRequiredResource.index(CraftingRequiredResource[CraftingProductInternal.index(CraftingSelect)])])
                                                PlayerInventoryAmmount.append(1)
                                        elif CraftMode == 1:
                                            res = random.randint(CraftingProductInternal.index(CraftingSelect) * 10,CraftingProductInternal.index(CraftingSelect)* 100)
                                            defence = random.randint(CraftingProductInternal.index(CraftingSelect) * 10,CraftingProductInternal.index(CraftingSelect)* 100)

                                            PlayerInventoryArmour.append(CraftingProduct[CraftingRequiredResource.index(CraftingRequiredResource[CraftingProductInternal.index(CraftingSelect)])])
                                            PlayerInventoryArmourDef.append(defence)
                                            PlayerInventoryArmourRes.append(res)

                                        elif CraftMode == 2:
                                            if WeaponType == 1:
                                                res = random.randint(CraftingProductInternal.index(CraftingSelect) * 10,CraftingProductInternal.index(CraftingSelect)* 100)
                                                attack = random.randint(CraftingProductInternal.index(CraftingSelect) * 10,CraftingProductInternal.index(CraftingSelect)* 100)
                                                crit = random.randint(1,25)
                                                hit = random.randint(50,100)

                                                PlayerInventoryWeapon.append(CraftingProduct[CraftingRequiredResource.index(CraftingRequiredResource[CraftingProductInternal.index(CraftingSelect)])])
                                                PlayerInventoryWeaponAtk.append(attack)
                                                PlayerInventoryWeaponRes.append(res)
                                                PlayerInventoryWeaponCrt.append(crit)
                                                PlayerInventoryWeaponhit.append(hit)

                                            elif WeaponType == 2:
                                                res = random.randint(CraftingProductInternal.index(CraftingSelect) * 90,CraftingProductInternal.index(CraftingSelect)* 100)
                                                attack = random.randint(CraftingProductInternal.index(CraftingSelect) * 75,CraftingProductInternal.index(CraftingSelect)* 200)
                                                crit = random.randint(1,25)
                                                hit = random.randint(75,100)

                                                PlayerInventoryWeapon.append(CraftingProduct[CraftingRequiredResource.index(CraftingRequiredResource[CraftingProductInternal.index(CraftingSelect)])])
                                                PlayerInventoryWeaponAtk.append(attack)
                                                PlayerInventoryWeaponRes.append(res)
                                                PlayerInventoryWeaponCrt.append(crit)
                                                PlayerInventoryWeaponhit.append(hit)

                                            elif WeaponType == 3:
                                                res = random.randint(CraftingProductInternal.index(CraftingSelect) * 10,CraftingProductInternal.index(CraftingSelect)* 50)
                                                attack = random.randint(CraftingProductInternal.index(CraftingSelect) * 50,CraftingProductInternal.index(CraftingSelect)* 100)
                                                crit = random.randint(1,30)
                                                hit = random.randint(75,100)

                                                PlayerInventoryWeapon.append(CraftingProduct[CraftingRequiredResource.index(CraftingRequiredResource[CraftingProductInternal.index(CraftingSelect)])])
                                                PlayerInventoryWeaponAtk.append(attack)
                                                PlayerInventoryWeaponRes.append(res)
                                                PlayerInventoryWeaponCrt.append(crit)
                                                PlayerInventoryWeaponhit.append(hit)

                                            elif WeaponType == 4:
                                                res = random.randint(CraftingProductInternal.index(CraftingSelect) * 10,CraftingProductInternal.index(CraftingSelect)* 100)
                                                attack = random.randint(CraftingProductInternal.index(CraftingSelect) * 10,CraftingProductInternal.index(CraftingSelect)* 50)
                                                crit = random.randint(1,5)
                                                hit = random.randint(25,100)

                                                PlayerInventoryWeapon.append(CraftingProduct[CraftingRequiredResource.index(CraftingRequiredResource[CraftingProductInternal.index(CraftingSelect)])])
                                                PlayerInventoryWeaponAtk.append(attack)
                                                PlayerInventoryWeaponRes.append(res)
                                                PlayerInventoryWeaponCrt.append(crit)
                                                PlayerInventoryWeaponhit.append(hit)


                                    else:
                                        print("You don't have enough of "+ CraftingRequiredResource[CraftingProductInternal.index(CraftingSelect)] + "\nNeeded: " + str(CraftingRequiredResource[CraftingRequiredResource[CraftingProduct.index(CraftingSelect)]]) + "\nYou have: " + str(PlayerInventoryAmmount[PlayerInventory[CraftingRequiredResource[CraftingProduct.index(CraftingSelect)]]]))
                                else:
                                    print("You don't have " + CraftingRequiredResource[CraftingProductInternal.index(CraftingSelect)])
                            else:
                                print("Couldn't find the item, did you spell it right?")

            elif keyboard.is_pressed("2"):  #Shops
                print("You are at a shop, You wonder what catagorys you should browse:\n1) Items\n2) Weapons\n3) Armour\n")
                time.sleep(1)
                A = 1
                while A == 1:
                    loop = 1
                    while loop == 1:
                        if keyboard.is_pressed("1"):
                            location = "\\Data\\Terrain\\AlternateTerrains\\Villages\\Shop\\Items"
                            loop = 2
                            length = int(linecache.getline(os.path.dirname(os.path.abspath(__file__)) + "\\Data\\Terrain\\AlternateTerrains\\Villages\\Slots.txt",29))
                            mode = 1
                        if keyboard.is_pressed("2"):
                            location = "\\Data\\Terrain\\AlternateTerrains\\Villages\\Shop\\Weapons"
                            loop = 2
                            length = int(linecache.getline(os.path.dirname(os.path.abspath(__file__)) + "\\Data\\Terrain\\AlternateTerrains\\Villages\\Slots.txt",32))
                            mode = 2
                        if keyboard.is_pressed("3"):
                            location = "\\Data\\Terrain\\AlternateTerrains\\Villages\\Shop\\Armour"
                            loop = 2
                            length = int(linecache.getline(os.path.dirname(os.path.abspath(__file__)) + "\\Data\\Terrain\\AlternateTerrains\\Villages\\Slots.txt",35))
                            mode = 3
                    
                    loop3 = 1
                    while loop3 == 1:
                        B = 1            
                        GreenText = Fore.GREEN + ""
                        RedText = Fore.RED + ""
                        ShopPrice = ["A"]
                        ShopProducts = ["A"]
                        while length >= B:
                            ShopProducts.append(linecache.getline(os.path.dirname(os.path.abspath(__file__)) + location + "\\Products.txt", B))
                            ShopPrice.append(linecache.getline(os.path.dirname(os.path.abspath(__file__)) + location + "\\Prices.txt",B))
                            ShopPrice[B] = ShopPrice[B].strip()
                            ShopPrice[B] = int(ShopPrice[B])
                            ShopProducts[B] = ShopProducts[B].strip()
                            B = B + 1
    
                        B = 1
                        while length >= B:
                            if PlayerGeneral[1] >= ShopPrice[B]:
                                GreenText = GreenText + str(B) +") " + str(ShopProducts[B]) + " - " + str(ShopPrice[B]) + " gold\n"
                            else:
                                RedText = RedText + str(ShopProducts[B]) + " - " + str(ShopPrice[B]) + " gold\n"
                            B = B + 1

                        loop2 = 1
                        while loop2 == 1:
                            print(Fore.RESET + "Your gold: " + str(PlayerGeneral[1]) + "\n" + GreenText + RedText + Fore.RESET + "\nType the number in brackets and press enter to buy it.\nOr type leave (with no capitals) to leave\n")
                            Number = input("")
                            tempory = 0

                            try:
                                Number = int(Number)
                            except:
                                if Number == "leave":
                                    AlternateTerrains()
                                else:
                                    print("")
                                tempory = 0
                            else:
                                if Number <= length:
                                    tempory = 1
                                else:
                                    tempory = 0

                            if mode == 1:
                                if tempory == 1 and PlayerGeneral[1] >= ShopPrice[Number]:
                                    Number = int(Number)
                                    PlayerGeneral[1] = PlayerGeneral[1] - ShopPrice[Number]
                                    if ShopProducts[Number] in PlayerInventory:
                                        PlayerInventoryAmmount[PlayerInventory.index(ShopProducts[Number])] = PlayerInventoryAmmount[PlayerInventory.index(ShopProducts[Number])] + 1
                                    else:
                                        PlayerInventory.append(ShopProducts[Number])
                                        PlayerInventoryAmmount.append(1)
                                    loop2 = 0
                                    print("You bought " + str(ShopProducts[Number]) + " for " + str(ShopPrice[Number]) + " gold")
                                else:
                                    print("That item doesn't exist or you can't afford it")
                            elif mode == 2:
                                if tempory == 1 and PlayerGeneral[1] >= ShopPrice[Number]:
                                    b = 1
                                    stats = [0]
                                    while b <= length:
                                        stats.append(linecache.getline(os.path.dirname(os.path.abspath(__file__)) + location + "\\Stats.txt",b))
                                        stats[b] = stats[b].strip()
                                        stats[b] = int(stats[b])
                                        b = b + 1
                                    PlayerGeneral[1] = PlayerGeneral[1] - ShopPrice[Number]
                                    PlayerInventoryWeaponAtk.append(random.randint(round(stats[Number] / 10),stats[Number] * 10))
                                    PlayerInventoryWeaponRes.append(random.randint(round(stats[Number] / 10),stats[Number] * 10))
                                    PlayerInventoryWeaponCrt.append(random.randint(1,50))
                                    PlayerInventoryWeaponhit.append(random.randint(90,100))
                                    PlayerInventoryWeapon.append(ShopProducts[Number])
                                    print("You bought " + str(ShopProducts[Number]) + " for " + str(ShopPrice[Number]) + " gold")
                                else:
                                    print("That item doesn't exist or you can't afford it")
                            elif mode == 3:
                                if tempory == 1 and PlayerGeneral[1] >= ShopPrice[Number]:
                                    b = 1
                                    stats = [0]
                                    while b <= length:
                                        stats.append(linecache.getline(os.path.dirname(os.path.abspath(__file__)) + location + "\\Stats.txt",b))
                                        stats[b] = stats[b].strip()
                                        stats[b] = int(stats[b])
                                        b = b + 1
                                    PlayerGeneral[1] = PlayerGeneral[1] - ShopPrice[Number]
                                    PlayerInventoryArmour.append(ShopProducts[Number])
                                    PlayerInventoryArmourDef.append(random.randint(round(stats[Number] / 10), stats[Number] * 10))
                                    PlayerInventoryArmourRes.append(random.randint(round(stats[Number] / 10), stats[Number] * 10))
                                    print("You bought " + str(ShopProducts[Number]) + " for " + str(ShopPrice[Number]) + " gold")
                                else:
                                    print("That item doesn't exist or you can't afford it")

            elif keyboard.is_pressed("4"):
                WorldGen()

    elif AlternateTerrain == 4: #Traders
        C = 0
        while C == 0:
            if SystemStats[0] != 1:
                os.system("cls")

            print("There is a trader here, you can probably buy somthing here.\n1) Buy\n")
            if PlayerGeneral[1] >= 100:
                print(Fore.GREEN + "1) Basic Healing Potion - 100\nHeals 50 HP\n" + Fore.RESET)
            else:
                print(Fore.RED + "1) Basic Healing Potion - 100\nHeals 50 HP\n" + Fore.RESET)

            if PlayerGeneral[1] >= 250:
                print(Fore.GREEN + "2) Advanced Healing Potion - 500\nHeals 250 HP\n" + Fore.RESET)
            else:
                print(Fore.RED + "2) Advanced Healing Potion - 500\nHeals 250 HP\n" + Fore.RESET)

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

    print("Saved!\n\n")
    PlayerTurn()
 
def Load():
    global PlayerInventory
    global PlayerInventoryAmmount
    global PlayerMaxStats
    print("Select a slot to load slot (1-5)")
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
    
    A = 1
    while A == 1:
        if keyboard.is_pressed("y"):
            A = 1
        elif keyboard.is_pressed("n"):
            Load()
    
        destination = os.path.dirname(os.path.abspath(__file__)) + "\\Data\\PlayerData\\" + str(SlotNo) + "\\PlayerInventory.json"
        with open(destination) as file:
            PlayerInventory = json.load(file)

        destination = os.path.dirname(os.path.abspath(__file__)) + "\\Data\\PlayerData\\" + str(SlotNo) + "\\PlayerInventoryAmmount.json"
        with open(destination) as file:
            PlayerInventoryAmmount = json.load(file)

        destination = os.path.dirname(os.path.abspath(__file__)) + "\\Data\\PlayerData\\" + str(SlotNo) + "\\PlayerStats.json"
        with open(destination) as file:
            PlayerStats = json.load(file)

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

    if SystemStats != 1:
        os.system("cls")

    PlayerAttack = PlayerMaxStats[1]
    PlayerDefence = PlayerMaxStats[2]
    PlayerHP = PlayerMaxStats[0]
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

        if EnemyStats[0] < 0:
            if PlayerGeneral[0] >= PlayerGeneral[2] * 1000:
                print("You leveled up!")
                LevelUpBonus = random.randint(1,50)
                PlayerMaxStats[0] = PlayerMaxStats[0] + LevelUpBonus
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
    if Resource1Text == "":
        print("Theres nothing here to collect!\n")
        PlayerTurn()

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
    PlayerTurn()

def Move():
    global WorldStats

    print("\nSelect a direction to move\n         (1)\n        North\n(4) West     East (2)\n        South\n         (3)")
    time.sleep(1)
    a = 1
    while a == 1:
        if keyboard.is_pressed("1"):
            WorldStats[1] = WorldStats[1] + 1
            a = 0
        elif keyboard.is_pressed("2"):
            WorldStats[0] = WorldStats[0] + 1
            a = 0
        elif keyboard.is_pressed("3"):
            WorldStats[1] = WorldStats[1] - 1
            a = 0
        elif keyboard.is_pressed("4"):
            WorldStats[0] = WorldStats[0] - 1
            a = 0
    WorldGen()

Menu()