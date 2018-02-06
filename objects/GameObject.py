import pygame
class GameObject:
    def __init__(self,*args):
        self.abilities = {}
        for e in args:
            self.AddAbility(e[0],e[1])
    def AddAbility(self,abilityName,ability):
        self.abilities[abilityName] = ability
    def GetAbility(self,name):
        return self.abilities[name]
