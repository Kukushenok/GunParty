import os
import objects.Level as level
class Levels:
    def __init__(self):
        self.levels = {}
        self.currlevel = None
        self.levelRoot = os.path.join(os.getcwd(), "resources", "levels")
        for e in [os.path.join(self.levelRoot, o) for o in os.listdir(self.levelRoot)]:
            self.addLevel(e.split("\\")[-1],e)

    def addLevel(self,name,path):
        self.levels[name] = level.Level(path)
    def loadLevel(self,name):
        if self.currlevel: self.currlevel.unload()
        self.currlevel = self.levels[name]
        self.currlevel.load()