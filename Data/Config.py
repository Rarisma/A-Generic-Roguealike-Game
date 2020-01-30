#This is the configuration file for Rougalike.
#The Variables below can be edited.
#If the value is invalid then the default will be used (Unless otherwise noted).


AutoUpdaterEnabled = True 
#Enables AutoUpdate diologue (Default is True)
#Allowed values (True,False)

AutoUpdaterBranch = "/TMAltair/Roguealike/master/"
#Tells the AutoUpdater which branch to use (Default is /master/)
#Allowed Values (/master/,/Development/) and any other open branch also note if this branch is not by TMAltair edit the branch to (/NAME/RougalikeRPG/BRANCH/)
#Please note that this will not fallback to /master/

#Don't edit these as it may have unknow effects
Version = "1.0.0"
WorldStats = [0,0,1]    #0-X coord 1- Y coord  2 - Difficulty random.randint(-2147483500,2147483500)
EnemyStats  = [50,50,50,50,3]
PlayerInventory = [""]
PlayerInventoryAmmount = [""]
PlayerGeneral = [0,0,1] # 0 - XP   1 - Gold   2 - Level
PlayerMaxStats = [50,50,50]  #0-HP 1-Attack 2-Defence
EnemyStats = [0,0,0]
SaveInfo = ["Unknown","Unknown"] #Latest Version 1- Last saved to
BattleLog = ["","","","","","",""]
QuestName = ["","QuestTest1","QuestTest2 -  Triple Darkness","QuestTest3","Quest test 3 - Connectivity"] # name of the quest
QuestDescription = ["","Quest test!","This is a quest to test","Beast drops?","Who is this guy?"]
QuestReq1Ammount = ["",20,5,10,5]
QuestReq1Item = ["","Iron Bar","Branches","Beast Hide","Sword of gods"]
QuestReward = ["",1000]
PlayerHP = 50
EquipedArmour = "Nothing"   #Name of armour
EquipedArmourDef = 0 #Defence increase
EquipedArmourRes = 0 #Durabilty
EquipedWeapon = "Hands"
EquipedWeaponhit = 100
EquipedWeaponatk = 0
EquipedWeaponcrt = 0
EquipedWeaponres = 0
SaveUI = 1  #0- Player has a chance to select a slot 1- disables UI and forces auto save
PlayerInventoryArmourRes = []
PlayerInventoryArmour    = []
PlayerInventoryArmourDef = []
PlayerInventoryWeapon    = []
PlayerInventoryWeaponAtk = []
PlayerInventoryWeaponRes = []
PlayerInventoryWeaponCrt = []
PlayerInventoryWeaponhit = []
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
