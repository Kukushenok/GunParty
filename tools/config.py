import configparser
import os
import pygame
class Config():
    def __init__(self,path = None):
        self.config = configparser.ConfigParser()
        if path:
            self.config.read(os.path.join(path,'config.ini'))
        else:
            self.config.read('config.ini')
    def get(self,item):
        return self.config["SETTINGS"][item]
    def getAsDict(self,item):
        toDict = self.config["SETTINGS"][item]
        dictPairs = toDict.split(",")
        resDict = {}
        for e in dictPairs:
            splittedE = e.split(":")
            exec("resDict["+splittedE[0]+"] = "+splittedE[1])
        return resDict