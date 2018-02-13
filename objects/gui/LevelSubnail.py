import pygame
from objects.engine.Global import LEVELS
class LevelSubnail():
    def __init__(self,startScreen,levelname,size):
        self.startScreen = startScreen
        self.level = LEVELS.levels[levelname]
        self.level.load()
        self.levelname=levelname
        self.rect = size
    def render(self):
        self.startScreen.screen.blit(pygame.transform.scale(self.level.resources["background.png"],(self.rect[2],self.rect[3])),(self.rect[0],self.rect[1]))
        masked = pygame.transform.scale(self.level.resources["ground.png"].copy(),(self.rect[2],self.rect[3]))
        masked.blit(pygame.transform.scale(self.level.resources["ground_mask.png"],(self.rect[2],self.rect[3])), (0, 0), None, pygame.BLEND_RGBA_MULT)
        self.startScreen.screen.blit(masked,(self.rect[0],self.rect[1]))
    def get_event(self,event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and self.rect.collidepoint(event.pos):
                self.startScreen.load_level(self.levelname)