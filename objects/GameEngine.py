import pygame
import os
from objects.Global import GAMECFG
from objects.Global import LEVELS
from objects.Global import RESOURCES
import objects.Ground as ground
import tools.config as config
import objects.Playground as playground
import objects.SpriteRenderer as spriteRenderer
class GameEngine:
    def __init__(self):
        pygame.init()
        self.all_sprites = pygame.sprite.Group()
        cnf = config.Config()
        self.fps = float(cnf.get("fps"))
        self.size = int(cnf.get("width")), int(cnf.get("height"))
        if cnf.get("fullscreen") != "0":
            self.screen = pygame.display.set_mode(self.size,pygame.FULLSCREEN)
        else:
            self.screen = pygame.display.set_mode(self.size)
        self.clock = pygame.time.Clock()
        self.running = True
        GAMECFG.screenwidth, GAMECFG.screenheight = self.size
        GAMECFG.fullscreen = cnf.get("fullscreen")!=0
        GAMECFG.fps = self.fps
        self.load_level()


    def load_level(self):
        LEVELS.loadLevel("level_1")
        self.i = 0
        self.sr = spriteRenderer.SpriteRenderer(RESOURCES["wwalk.png"],self.all_sprites)
        self.sr.selectImage(0)
        self.sr.rect = self.sr.image.get_rect()
        self.sr.left = 1600
        self.sr.y = 10
        self.playGround = playground.Playground(
            [LEVELS.currlevel.resources["soil.png"], LEVELS.currlevel.resources["space.png"],
             LEVELS.currlevel.resources["stones.jpg"]])

    def on_loop(self):
        pass

    def on_render(self):
        self.screen.fill((0, 0, 0))
        self.playGround.render(self.screen)
        self.i +=1
        self.sr.selectImage(self.i)
        self.all_sprites.draw(self.screen)
        self.all_sprites.update(1/self.fps)
        pygame.display.flip()
        pygame.display.update()

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
