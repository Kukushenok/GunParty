import pygame
import os
import tools.config as config
import objects.Playground as playground
import objects.SpriteRenderer as spriteRenderer
class GameEngine:
    def __init__(self):
        pygame.init()
        cnf = config.Config()
        self.fps = float(cnf.get("fps"))
        self.size = int(cnf.get("width")), int(cnf.get("height"))
        if cnf.get("fullscreen") != "0":
            self.screen = pygame.display.set_mode(self.size,pygame.FULLSCREEN)
        else:
            self.screen = pygame.display.set_mode(self.size)
        self.clock = pygame.time.Clock()
        self.running = True
        self.load_level()

    def load_level(self):
        self.playGround = playground.Playground(
            [os.path.join(os.getcwd(), "resources","images","masks","soil.png"), os.path.join(os.getcwd(),"resources","images","skies","space.png"), os.path.join(os.getcwd(),"resources","images","grounds","stones.jpg")])

    def on_loop(self):
        pass

    def on_render(self):





        self.screen.fill((0, 0, 0))
        self.playGround.render(self.screen)
        sr = spriteRenderer.SpriteRenderer(os.path.join(os.getcwd(), "resources", "images", "sprites", "waccused.png"))
        sr.render(self.screen,20,20)
        pygame.display.flip()

    def on_cleanup(self):
        pygame.quit()

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            self.clock.tick(self.fps)
            self.on_loop()
            self.on_render()
        self.on_cleanup()
