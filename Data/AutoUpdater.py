import urllib
import Data.Config
import linecache
import os

Version = ":-("

def ConnectionCheck():
    global Version
    try:
        urllib.request.urlretrieve("https://raw.githubusercontent.com" + Data.Config.AutoUpdaterBranch + "metadata.txt",os.path.dirname(os.path.abspath(__file__)) + "\\Data\\meta.txt")
        Version = int(linecache.getline(os.path.dirname(os.path.abspath(__file__)) + "\\Data\\meta.txt",3))
        print(str(Version))
    except:
        return ["Failure"]
    else:
        if UpdateCheckVersion != Version:
            return ["Success"]
        else:
            return ["Already Updated"]

