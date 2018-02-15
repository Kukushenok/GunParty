import pygame
class Audible:
    def __init__(self,gameObject):
        self.gameObject = gameObject
        self.prevState = None
    def updateState(self,state):
        if self.prevState != state and self.prevState:
            if self.prevState.sound:
                self.prevState.sound.stop()
        if state.sound:
            if state.loop:
                state.sound.play(-1)
            else: state.sound.play()
        self.prevState = state