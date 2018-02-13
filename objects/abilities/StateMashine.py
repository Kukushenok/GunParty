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

    def SetState(self,name,option="n"):
        self.current_state = self.states[name]
        self.current_state.SetCurrentOption(option)

    def BindStates(self, stateNameFirst, stateNameSecond, option="n"):
        first_state = self.states[stateNameFirst]
        second_state = self.states[stateNameSecond]
        first_state.SetCurrentOption(option)
        second_state.SetCurrentOption(option)
        first_state.nextState = second_state

    def SetStateAsIs(self, state, option="n"):
        self.current_state = state
        self.current_state.SetCurrentOption(option)

