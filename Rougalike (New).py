import os
import Data.AutoUpdater
import Data.Config

if Data.Config.AutoUpdaterEnabled is True: # Checks if AutoUpdate is enabled
    UpdateCheck = Data.AutoUpdater.ConnectionCheck()

print(Data.AutoUpdater.Version)
print(UpdateCheck)
