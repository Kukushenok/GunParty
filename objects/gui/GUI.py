import pygame
import objects.gui.ForceIndicator
import objects.gui.Slot
class GUI:
    def __init__(self,keymask):
        self.slots = []
        self.selected=2
        self.keymask = keymask
        self.objects = []
        self.gameObject = None
    def AddObject(self,obj):
        if isinstance(obj,objects.gui.ForceIndicator.ForceIndicator):
            self.forceInd = obj
        elif isinstance(obj,objects.gui.Slot.Slot):
            self.slots.append(obj)
        self.objects.append(obj)
    def render(self,screen):
        for e in self.objects:
            e.render(screen)
    def update(self,dt):
        for e in self.slots:
            e.update(dt)
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

