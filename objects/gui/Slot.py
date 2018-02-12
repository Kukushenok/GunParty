import pygame
from objects.engine.Global import RESOURCES
from objects.engine.Global import GAMECFG
class Slot():
    def __init__(self,gui,weapon = None):
        tmpRect = RESOURCES["guislot.png"].get_rect()
        tmpCoeff = GAMECFG.GetScreenCoeff()
        self.notselected = pygame.transform.scale(RESOURCES["guislot.png"].convert_alpha(),(int(tmpCoeff[0]* tmpRect[2]),
            int(tmpCoeff[1] * tmpRect[3])))
        self.selected = pygame.transform.scale(RESOURCES["guislots.png"].convert_alpha(), (int(tmpCoeff[0] * tmpRect[2]),
                                                          int(tmpCoeff[1] * tmpRect[3])))
        self.pos = [0,0]
        self.gui = gui
        gui.AddSlot(self)

        if weapon:
            #tmpRect = RESOURCES[weapon].get_rect()
            self.weapon = pygame.transform.scale(RESOURCES[weapon], (int(tmpCoeff[0] * tmpRect[2]),
                                                          int(tmpCoeff[1] * tmpRect[3])))
    def render(self,screen):
        screen.blit(self.selected if self.gui.slots[self.gui.selected] == self else self.notselected,self.pos)
        if self.weapon:
            screen.blit(self.weapon,self.pos)
    def update(self,dt):
        pass