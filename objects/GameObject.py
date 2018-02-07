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
    def get_event(self,event):
        for element in self.abilities.values():
            get_event = getattr(element, "get_event", None)
            if callable(get_event):
                element.get_event(event)