import pygame
from objects.engine.Global import GAMECFG
from objects.engine.Global import RESOURCES
class StartScreen():
    def __init__(self,gameEngine,screen):
        self.screen = screen
        self.gameEngine = gameEngine
        self.components = []
        self.running = True
        self.page = 0
    def AddComponent(self,comp):
        self.components.append(comp)
    def load_level(self,levelname):
        self.gameEngine.load_level(levelname)
        self.running = False
    def run(self):
        while self.running:
            self.screen.fill(pygame.Color("black"))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                for e in self.components: e.get_event(event)
            self.screen.blit(pygame.transform.scale(RESOURCES["background2.jpg"],(GAMECFG.screenwidth,GAMECFG.screenheight)),(0,0))
            for e in self.components: e.render()
            pygame.display.flip()