import pygame

import ResourceManager


class LevelSubnail():
    def __init__(self,startScreen,levelname,size,page):
        self.page = page
        self.startScreen = startScreen
        self.level = ResourceManager.ResourceManager.intsLevels().levels[levelname]
        self.levelname=levelname
        self.image = self.level.get_subnail(size)
        self.rect = size
    def render(self):
        if self.startScreen.page != self.page: return None
        self.startScreen.screen.blit(self.image,(self.rect[0],self.rect[1]))
    def get_event(self,event):
        if self.startScreen.page != self.page: return None
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and self.rect.collidepoint(event.pos):
                self.startScreen.load_level(self.levelname)