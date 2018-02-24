import pygame

import ResourceManager


class Slot():
    def __init__(self,gui,weapon = None):
        tmpRect = ResourceManager.ResourceManager.instResources()["guislot.png"].get_rect()
        tmpCoeff = ResourceManager.ResourceManager.instGameCFG().GetScreenCoeff()
        self.delay = 0
        self.notselected = pygame.transform.scale(
            ResourceManager.ResourceManager.instResources()["guislot.png"].convert_alpha(),
            (int(tmpCoeff[0]* tmpRect[2]), int(tmpCoeff[1] * tmpRect[3])))
        self.selected = pygame.transform.scale(
            ResourceManager.ResourceManager.instResources()["guislots.png"].convert_alpha(),
            (int(tmpCoeff[0] * tmpRect[2]), int(tmpCoeff[1] * tmpRect[3])))
        self.coeff = tmpCoeff
        self.rect= self.selected.get_rect()
        self.pos = [0,0]
        self.gui = gui
        self.ready = 0
        gui.AddObject(self)

        if weapon:
            #tmpRect = RESOURCES[weapon].get_rect()
            self.weapon = pygame.transform.scale(ResourceManager.ResourceManager.instResources()[weapon], (int(tmpCoeff[0] * tmpRect[2]),
                                                                                                           int(tmpCoeff[1] * tmpRect[3])))
    def render(self,screen):
        self.rect.x = self.pos[0]
        self.rect.y = self.pos[1]
        screen.blit(self.selected if self.gui.slots[self.gui.selected] == self else self.notselected,self.pos)
        if self.weapon:
            screen.blit(self.weapon,self.pos)
        if self.gui.slots[self.gui.selected] == self:
            color = pygame.Color("green" if self.delay == 0 else "red")
            text = pygame.font.SysFont("comicsansms",self.rect[3]//4).render("Ready" if self.delay == 0 else str(int(self.delay)+1), True, color)
            screen.blit(text,(self.rect[0]+self.rect[2]//2-text.get_rect()[2]//2,self.rect[1]+self.rect[3]))
    def update(self,dt):
        if self.delay > 0:
            self.delay-=dt
            self.ready = False
            if self.ready == 2: self.ready = 0
        else:
            self.delay = 0
            if self.ready == 0: self.ready = 1