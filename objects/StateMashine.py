import pygame
import objects.SpriteRenderer as spriteRenderer
class StateMashine:
    def __init__(self,*args):
        self.spriteRenderer = None
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
        if self.spriteRenderer:
            self.spriteRenderer.load()

    def SetSpriteRenderer(self,spriteRenderer):
        self.spriteRenderer = spriteRenderer