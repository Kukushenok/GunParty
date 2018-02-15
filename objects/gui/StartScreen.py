import pygame

import ResourceManager

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
                    self.gameEngine.running = False
                for e in self.components: e.get_event(event)
            self.screen.blit(pygame.transform.scale(ResourceManager.ResourceManager.instResources()["background2.jpg"],
                                                    (ResourceManager.ResourceManager.instGameCFG().screenwidth,
                                                     ResourceManager.ResourceManager.instGameCFG().screenheight)), (0, 0))
            for e in self.components: e.render()
            pygame.display.flip()