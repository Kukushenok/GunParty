import pygame
from objects.engine.Global import RESOURCES
class ExitButton():
    def __init__(self,startScreen,rect):
        self.startScreen = startScreen
        self.rect = rect
        self.image = pygame.transform.scale(RESOURCES["exit.png"],(rect[2],rect[3]))
    def render(self):
        self.startScreen.screen.blit(self.image,(self.rect[0],self.rect[1]))
    def get_event(self,event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and self.rect.collidepoint(event.pos):
                self.startScreen.running = False