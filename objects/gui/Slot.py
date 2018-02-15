import pygame

import ResourceManager


class Slot():
    def __init__(self,gui,weapon = None):
        tmpRect = ResourceManager.ResourceManager.instResources()["guislot.png"].get_rect()
        tmpCoeff = ResourceManager.ResourceManager.instGameCFG().GetScreenCoeff()
        self.notselected = pygame.transform.scale(
            ResourceManager.ResourceManager.instResources()["guislot.png"].convert_alpha(),
            (int(tmpCoeff[0]* tmpRect[2]), int(tmpCoeff[1] * tmpRect[3])))
        self.selected = pygame.transform.scale(
            ResourceManager.ResourceManager.instResources()["guislots.png"].convert_alpha(),
            (int(tmpCoeff[0] * tmpRect[2]), int(tmpCoeff[1] * tmpRect[3])))
        self.pos = [0,0]
        self.gui = gui
        gui.AddObject(self)

        if weapon:
            #tmpRect = RESOURCES[weapon].get_rect()
            self.weapon = pygame.transform.scale(ResourceManager.ResourceManager.instResources()[weapon], (int(tmpCoeff[0] * tmpRect[2]),
                                                                                                           int(tmpCoeff[1] * tmpRect[3])))
    def render(self,screen):
        screen.blit(self.selected if self.gui.slots[self.gui.selected] == self else self.notselected,self.pos)
        if self.weapon:
            screen.blit(self.weapon,self.pos)
    def update(self,dt):
        pass