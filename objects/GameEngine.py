import pygame
import os
from objects.Global import GAMECFG
from objects.Global import LEVELS
from objects.Global import RESOURCES
import objects.Factory as factory
import tools.config as config
import objects.Playground as playground
from objects.Global import OBJECTMANAGER
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
        self.factory = factory.Factory(RESOURCES,self.all_sprites)
        LEVELS.loadLevel("level_1")
        self.i = 0
        self.player = self.factory.Get("player",10,10,{"left":pygame.K_LEFT,"right":pygame.K_RIGHT,"up":pygame.K_UP,"down":pygame.K_DOWN})
        self.sr = self.player.GetAbility("spriteRenderer")
        self.player2 = self.factory.Get("player",60,30,{"left":pygame.K_a,"right":pygame.K_d,"up":pygame.K_w,"down":pygame.K_s})
        self.sr2 = self.player2.GetAbility("spriteRenderer")
        self.playGround = playground.Playground(
            [LEVELS.currlevel.resources["soil.png"], LEVELS.currlevel.resources["space.png"],
             LEVELS.currlevel.resources["stones.jpg"]])

    def on_loop(self):
        OBJECTMANAGER.update(1/self.fps)

    def on_render(self):
        self.screen.fill((0, 0, 0))
        self.playGround.render(self.screen)
    #    self.i +=1
     #   self.sr.selectImage(self.i)
      #  self.sr2.selectImage(self.i)
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
                OBJECTMANAGER.get_event(event)
            self.clock.tick(self.fps)

            self.on_loop()
            self.on_render()

        self.on_cleanup()
