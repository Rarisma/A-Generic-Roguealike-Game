import linecache
import os
import time
import urllib.request
import zipfile
from colorama import Fore, Back, Style, init
import keyboard
init(convert=True)
#chess pieces!

SystemInfo = ["Build Version: 1/2/2020","1.0"]
LatestVer = "ERROR"

def Intialise():
    global SystemInfo

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
    if str(linecache.getline(os.path.dirname(os.path.abspath(__file__)) + "Config.txt",3)) == "False":  #Checks if AutoUpdate is disabled if so then it goes to the menu
        Menu()

    try:    #Tries to get check github
        urllib.request.urlretrieve("https://raw.githubusercontent.com/TMAltair/RougalikeRPG/master/metadata.txt",os.path.dirname(os.path.abspath(__file__)) + "\\meta.txt")
        LatestVer = str(linecache.getline(os.path.dirname(os.path.abspath(__file__)) + "\\meta.txt",3))
    except: #Upon any type of failure it skips AutoUpdate
        LatestVer = "Failed"
        Menu()
    LatestVer = LatestVer.strip
    
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
                print("Downloading latest version from github (1/4)")
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

def Menu():
    os.system("cls")
    print("Rougealike RPG by TMAltair\n1) Play\n2) Load\nQ) Quit\n\nVersion " + str(SystemInfo[1]) + "\n(" + str(SystemInfo[0]) + ")")
    
    if LatestVer == "Failed": #If an error occurs prints this
        print("Could not talk to the AutoUpdate webpage.\nTo see if Rougealike has an update go to\nhttps://github.com/TMAltair/Roguealike/")
    elif LatestVer == "Declined": #If update is declined 
        print("Update available!\nPress U) to update!")
    elif LatestVer == "ERROR": #If auto update is not changed for some reason
        print("An Error occured in the update.")

    Loop = 1
    while Loop == 1:
        if keyboard.is_pressed("1"):
            PlayerInfo = [input("Enter a name: "),2]
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
            WorldGeneration()
        elif keyboard.is_pressed("2"):
            print()

def WorldGeneration():
    print("confed")
Intialise()