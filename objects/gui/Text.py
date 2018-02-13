import pygame
class Text():
    def __init__(self,startScreen,pos,text,size,color):
        self.font = pygame.font.SysFont("comicsansms", size)
        self.text = self.font.render(text, True,color)
        self.pos = pos
        self.startScreen = startScreen
    def render(self):
        self.startScreen.screen.blit(self.text,self.pos)
    def get_event(self,event): pass
