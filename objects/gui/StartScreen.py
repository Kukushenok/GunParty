import pygame
import objects.gui.ExitDialog
import ResourceManager

class StartScreen():
    def __init__(self,gameEngine,screen):
        self.screen = screen
        self.gameEngine = gameEngine
        self.components = []
        self.running = True
        self.page = 0
        self.exitButton = None
        self.sound = ResourceManager.ResourceManager.instSFXResources()["startScreen.wav"]
    def AddComponent(self,comp):
        self.components.append(comp)
        if isinstance(comp, objects.gui.ExitDialog.ExitDialog):
            self.exitButton = comp
    def load_level(self,levelname):
        self.gameEngine.load_level(levelname)
        self.running = False
    def run(self):
        self.sound.play(-1)
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    self.gameEngine.running = False
                if not self.exitButton.show:
                    for e in self.components: e.get_event(event)
                else:
                    self.exitButton.get_event(event)
            self.screen.fill(pygame.Color("black"))
            self.screen.blit(pygame.transform.scale(ResourceManager.ResourceManager.instResources()["background.png"],
                                                    (ResourceManager.ResourceManager.instGameCFG().screenwidth,
                                                     ResourceManager.ResourceManager.instGameCFG().screenheight)), (0, 0))
            for e in self.components: e.render()
            pygame.display.flip()
        self.sound.stop()