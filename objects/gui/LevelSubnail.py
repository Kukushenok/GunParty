import pygame
from objects.engine.Global import LEVELS
class LevelSubnail():
    def __init__(self,startScreen,levelname,size,page):
        self.page = page
        self.startScreen = startScreen
        self.level = LEVELS.levels[levelname]
        self.level.load()
        self.levelname=levelname
        self.level.resources["background.png"] = self.level.resources["background.png"].convert_alpha()
        self.level.resources["ground.png"] = self.level.resources["ground.png"].convert_alpha()
        self.level.resources["ground_mask.png"] = self.level.resources["ground_mask.png"].convert_alpha()
        self.rect = size
    def render(self):
        if self.startScreen.page != self.page: return None
        self.startScreen.screen.blit(pygame.transform.scale(self.level.resources["background.png"],(self.rect[2],self.rect[3])),(self.rect[0],self.rect[1]))
        masked = pygame.transform.scale(self.level.resources["ground.png"].copy(),(self.rect[2],self.rect[3]))
        masked.blit(pygame.transform.scale(self.level.resources["ground_mask.png"],(self.rect[2],self.rect[3])), (0, 0), None, pygame.BLEND_RGBA_MULT)
        self.startScreen.screen.blit(masked,(self.rect[0],self.rect[1]))
    def get_event(self,event):
        if self.startScreen.page != self.page: return None
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and self.rect.collidepoint(event.pos):
                self.startScreen.load_level(self.levelname)