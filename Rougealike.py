import linecache
import os
import time
import urllib.request
import zipfile
import colorama
SystemInfo = ["Build Version: 1/2/2020","1.0"]

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

    print("Trying to check update servers...\n\nTired of seeing this?\nChange the autoupdater setting in Prefs.ini\nThis shouldn't take more than 30 seconds")
    if str(linecache.getline(os.path.dirname(os.path.abspath(__file__)) + "Config.txt",3)) == "False":
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
                urllib.request.urlretrieve("https://raw.githubusercontent.com/TMAltair/RougalikeRPG/master/Rougalike.py",os.path.dirname(os.path.abspath(__file__)) + "\\Rougalike " + LatestVer +"\\Rougalike " + LatestVer + ".py")
                urllib.request.urlretrieve("https://raw.githubusercontent.com/TMAltair/RougalikeRPG/master/Data.zip",os.path.dirname(os.path.abspath(__file__)) + "\\Rougalike " + LatestVer +"\\Data.zip")
                with zipfile.ZipFile(os.path.dirname(os.path.abspath(__file__)) + "\\Rougalike " + LatestVer + "\\Data.zip", 'r') as zip_ref:
                    zip_ref.extractall(os.path.dirname(os.path.abspath(__file__)) + "\\Rougalike " + LatestVer)
                os.remove(os.path.dirname(os.path.abspath(__file__)) + "\\Rougalike " + LatestVer + "\\Data.zip")
                input("\n" + Colorama.Fore.GREEN + "Update Complete!" + Colorama.Fore.__getattribute__(PlayerPrefs[0]) + "\nTo run the latest version look for the folder called Rougalike " + LatestVer + "\n\nPress enter to close.")
                exit()
            elif keyboard.is_pressed("n"):
                Menu()
    Menu()

def Menu():
    print("Nice")

Intialise()