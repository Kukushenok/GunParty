import objects.Resources as resources
import objects.Levels as levels
import objects.GameCFG as gameconfig
import os

GAMECFG = gameconfig.GameCFG()
LEVELS = levels.Levels()
RESOURCES = resources.Resources(os.path.join(os.getcwd(),"resources","images")).resources

