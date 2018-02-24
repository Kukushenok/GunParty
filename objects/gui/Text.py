import pygame
class Text():
    def __init__(self,startScreen,pos,text,size,color):
        self.font = pygame.font.SysFont("comicsansms", size)
        self.text = self.font.render(text, True,color)
        self.pos = pos
        self.page = -1
        self.startScreen = startScreen
    def render(self):
        if self.page != -1 and self.startScreen.page != self.page: return None
        self.startScreen.screen.blit(self.text,self.pos)
    def get_event(self,event): pass
