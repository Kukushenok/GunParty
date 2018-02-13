import pygame
from objects.engine.Global import RESOURCES
class SwitchPageButton:
    def __init__(self,startScreen,dpage,rect):
        self.startScreen = startScreen
        self.dpage = dpage
        self.rect = rect
        self.work = True
        if dpage > 0:
            self.image = pygame.transform.scale(RESOURCES["arrowR.png"],(rect[2],rect[3]))
        else:
            self.image = pygame.transform.scale(pygame.transform.flip(RESOURCES["arrowR.png"],True,False), (rect[2], rect[3]))

    def get_event(self,event):
        if not self.work: return None
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and self.rect.collidepoint(event.pos):
                self.startScreen.page+=self.dpage

    def render(self):
        if self.startScreen.page+self.dpage< 0:
            self.work = False
        elif self.startScreen.page+self.dpage> self.startScreen.maxPage:
            self.work = False
        else:
            self.work = True
        if not self.work: return None
        self.startScreen.screen.blit(self.image,(self.rect[0],self.rect[1]))