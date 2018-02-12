import pygame
import os
from objects.engine.Global import GAMECFG
from objects.engine.Global import LEVELS
from objects.engine.Global import RESOURCES
import objects.engine.Factory as factory
import tools.config as config
import objects.level.Playground as playground
from objects.engine.Global import OBJECTMANAGER
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
        self.cnf = cnf
        self.load_level()


    def load_level(self):
        self.factory = factory.Factory(RESOURCES,self.all_sprites)
        LEVELS.loadLevel("level_1")
        self.i = 0
        self.player = self.factory.Get("player",10,10,self.cnf.getAsDict("player2KeyScheme"))
        self.gui = self.factory.Get("gui",10,10,self.cnf.getAsDict("player2KeyScheme"))
        self.player.GetAbility("playerControl").gui = self.gui
        self.sr = self.player.GetAbility("spriteRenderer")
        # self.player2 = self.factory.Get("player",60,30,{"left":pygame.K_a,"right":pygame.K_d,"up":pygame.K_w,"down":pygame.K_s})
        # self.sr2 = self.player2.GetAbility("spriteRenderer")
        self.playGround = playground.Playground(
            [pygame.transform.scale(LEVELS.currlevel.resources["soil.png"],self.size), pygame.transform.scale(LEVELS.currlevel.resources["space.png"],self.size),
             pygame.transform.scale(LEVELS.currlevel.resources["stones.jpg"],self.size)])

    def on_loop(self):
        OBJECTMANAGER.update(1/self.fps)

    def on_render(self):
        self.screen.fill((0, 0, 0))
        self.playGround.render(self.screen)
        self.all_sprites.draw(self.screen)
        self.gui.render(self.screen)
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