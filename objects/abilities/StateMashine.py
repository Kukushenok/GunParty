import pygame
import objects.abilities.SpriteRenderer as spriteRenderer
class StateMashine:
    def __init__(self,gameO,*args):
        self.gameObject = gameO
        self.states = {}
        for e in args:
            self.AddState(e[0],e[1])
        self.current_state = None

    def AddState(self,stateName,state):
        self.states[stateName] = state

    def GetState(self,name):
        return self.states[name]

    def CurrentState(self):
        return  self.current_state

    def SetState(self,name):
        self.current_state = self.states[name]
