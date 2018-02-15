import pygame

import ResourceManager


class Scroller():
    def __init__(self,startScreen,size):
        self.startScreen = startScreen
        self.rect = size
        self.image = pygame.transform.scale(
            pygame.transform.rotate(
                ResourceManager.ResourceManager.instResources()["textbox.png"],90)
            if size[2] < size[3] else ResourceManager.ResourceManager.instResources()["textbox.png"],
            (self.rect[2],self.rect[3]))
        if size[2] > size[3]:
            self.scsize = self.rect[3]
            self.scroller = pygame.transform.scale(
                ResourceManager.ResourceManager.instResources()["scroll.png"],(self.rect[3], self.rect[3]))
            self.vertical = False
        else:
            self.scsize = self.rect[2]
            self.scroller = pygame.transform.scale(
                ResourceManager.ResourceManager.instResources()["scroll.png"], (self.rect[2], self.rect[2]))
            self.vertical = True
        self.scrollerpos = [size[0],size[1]]
        self.coeff = 0
        self.move = False
    def check_pos(self):
        if self.vertical:
            if self.scrollerpos[1]<self.rect[1]:
                self.scrollerpos[1] = self.rect[1]
            elif self.scrollerpos[1]>self.rect[1]+self.rect[3]-self.scsize:
                self.scrollerpos[1] = self.rect[1]+self.rect[3]-self.scsize
        else:
            if self.scrollerpos[0]<self.rect[0]:
                self.scrollerpos[0] = self.rect[0]
            elif self.scrollerpos[0]>self.rect[0]+self.rect[2]-self.scsize:
                self.scrollerpos[0] = self.rect[0]+self.rect[2]-self.scsize
    def get_event(self,event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and self.rect.collidepoint(event.pos):
                self.move = True
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1 and self.move:
                self.move = False
        if event.type == pygame.MOUSEMOTION and self.move:
            if self.vertical:
                self.scrollerpos[1] = event.pos[1]-self.scsize//2
            else:
                self.scrollerpos[0] = event.pos[0]-self.scsize//2
        self.check_pos()
        if self.vertical:
            self.coeff = (self.scrollerpos[1]-self.rect[1])/(self.rect[3]-self.scsize)
        else:
            self.coeff = (self.scrollerpos[0] - self.rect[0]) / (self.rect[2] - self.scsize)
    def render(self):
        self.startScreen.screen.blit(self.image, (self.rect[0],self.rect[1]))
        self.startScreen.screen.blit(self.scroller,self.scrollerpos)