import pygame
from objects.engine.Global import RESOURCES
from objects.engine.Global import GAMECFG
class Slot():
    def __init__(self,gui):
        tmpRect = RESOURCES["guislot.png"].get_rect()
        tmpCoeff = GAMECFG.GetScreenCoeff()
        self.notselected = pygame.transform.scale(RESOURCES["guislot.png"],(int(tmpCoeff[0]* tmpRect[2]),
            int(tmpCoeff[1] * tmpRect[3])))
        self.selected = pygame.transform.scale(RESOURCES["guislots.png"], (int(tmpCoeff[0] * tmpRect[2]),
                                                          int(tmpCoeff[1] * tmpRect[3])))
        self.pos = [0,0]
        self.gui = gui
        gui.AddSlot(self)
        self.weapon = None
    def render(self,screen):
        screen.blit(self.selected if self.gui.slots[self.gui.selected] == self else self.notselected,self.pos)
    def update(self,dt):
        pass