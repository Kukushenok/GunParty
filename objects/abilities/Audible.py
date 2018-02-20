import pygame
class Audible:
    def __init__(self,gameObject):
        self.gameObject = gameObject
        self.prevState = None
        self.sounds = {}
    def addSound(self,name,sound):
        self.sounds[name] = sound
    def getSound(self,name):
        return self.sounds[name]
    def playSound(self,name,loop = 0):
        self.sounds[name].play(loop)
    def stopSound(self,name):
        self.sounds[name].stop()

    def updateState(self,state):
        if self.prevState != state and self.prevState:
            if self.prevState.sound:
                self.prevState.sound.stop()
        if state.sound:
            if state.loop:
                state.sound.play(-1)
            else: state.sound.play()
        self.prevState = state