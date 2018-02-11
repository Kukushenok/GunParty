import objects.level.Resources as resources
import objects.level.Levels as levels
import objects.engine.GameCFG as gameconfig
import objects.engine.ObjectManager as objectManager
import os

GAMECFG = gameconfig.GameCFG()
LEVELS = levels.Levels()
RESOURCES = resources.Resources(os.path.join(os.getcwd(),"resources","images")).resources
OBJECTMANAGER = objectManager.ObjectManager()
