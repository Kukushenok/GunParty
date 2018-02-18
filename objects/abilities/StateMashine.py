import pygame
import objects.abilities.SpriteRenderer as spriteRenderer
class StateMashine:
    def __init__(self,gameO,*args):
        self.gameObject = gameO
        self.states = {}
        for e in args:
            self.AddState(e[0],e[1])
        self.current_state = None
        self.subscribers = []

    def AddState(self,stateName,state):
        state.name = stateName
        self.states[stateName] = state

    def AddSubscriber(self,subscriber):
        self.subscribers.append(subscriber)

    def GetState(self,name):
        return self.states[name]

    def CurrentState(self):
        return  self.current_state

    def SetState(self,name,option="n"):
        state = self.states[name]
        if self.current_state != state:
            for e in self.subscribers: e.updateState(state)
        self.current_state = state
        self.current_state.SetCurrentOption(option)


    def BindStates(self, stateNameFirst, stateNameSecond, option="n"):
        first_state = self.states[stateNameFirst]
        second_state = self.states[stateNameSecond]
        first_state.SetCurrentOption(option)
        second_state.SetCurrentOption(option)
        first_state.nextState = second_state

    def SetStateAsIs(self, state, option="n"):
        if self.current_state != state:
            for e in self.subscribers: e.updateState(state)
        self.current_state = state
        self.current_state.SetCurrentOption(option)

