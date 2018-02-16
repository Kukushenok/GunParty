import pygame
import objects.gui.ForceIndicator as forceIndicator
class GUI:
    def __init__(self,keymask):
        self.slots = []
        self.selected=2
        self.keymask = keymask
    def AddObject(self,obj):
        if isinstance(obj,forceIndicator.ForceIndicator):
            self.forceInd = obj
        self.slots.append(obj)
    def render(self,screen):
        for e in self.slots:
            e.render(screen)
    def update(self,dt):
        pass
    def get_event(self,event):
        if not self.keymask: return None
        if event.type == pygame.KEYDOWN:
            if event.key == self.keymask["switchweaponl"]:
                self.selected-=1
            if event.key == self.keymask["switchweaponr"]:
                self.selected+=1
            if self.selected > len(self.slots) - 1:
                self.selected = 0
            elif self.selected < 0:
                self.selected = len(self.slots) - 1
    def destroy(self):
        self.slots = []

