import pygame
class Audible:
    def __init__(self,gameObject):
        self.gameObject = gameObject
        self.prevState = None
        self.sounds = {}
        self.disabledSounds = []
    def addSound(self,name,sound):
        self.sounds[name] = sound

    def disableSound(self, name):
        if name in self.disabledSounds: return None
        self.disabledSounds.append(name)
    def enableSound(self,name):
        try:
            self.disabledSounds.pop(self.disabledSounds.index(name))
        except Exception:pass
    def getSound(self,name):
        return self.sounds[name]
    def playSound(self,name,loop = 0):
        if name in self.disabledSounds: return None
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