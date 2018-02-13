import pygame
import os
from objects.engine.Global import GAMECFG
from objects.engine.Global import LEVELS
from objects.engine.Global import RESOURCES
import objects.engine.Factory as factory
import tools.config as config
import objects.level.Playground as playground
from objects.engine.Global import OBJECTMANAGER
import objects.gui.StartScreen as startScreen
import objects.gui.Scroller as scroller
import objects.gui.Text as text
import objects.gui.LevelSubnail as levelSubnail
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
        self.coeff = GAMECFG.GetScreenCoeff()
        self.load_start_screen()

    def load_start_screen(self):
        self.startScreen = startScreen.StartScreen(self,self.screen)
        cx = self.coeff[0]
        cy = self.coeff[1]
        i = 0
        for e in LEVELS.levels.keys():
            if i == 0:
                self.startScreen.AddComponent(levelSubnail.LevelSubnail(self.startScreen,e,pygame.Rect(20*cx,20*cy,640*cx,480*cy)))
            elif i == 1:
                self.startScreen.AddComponent(levelSubnail.LevelSubnail(self.startScreen, e, pygame.Rect(680 * cx, 20 * cy, 640 * cx, 480 * cy)))
            i+=1
        self.startScreen.AddComponent(scroller.Scroller(self.startScreen,pygame.Rect(1000*cx,100*cy,240*cx,60*cy)))
        self.startScreen.AddComponent(text.Text(self.startScreen,(1000*cx,30*cy),"Gravity",int(50*cy),pygame.Color("black")))
        self.startScreen.run()

    def load_level(self,name):
        self.factory = factory.Factory(RESOURCES,self.all_sprites)
        LEVELS.loadLevel(name)
        self.i = 0
        self.player = self.factory.Get("player",10,10,self.cnf.getAsDict("player2KeyScheme"))
        self.gui = self.factory.Get("gui",10,10,self.cnf.getAsDict("player2KeyScheme"))
        self.player.GetAbility("playerControl").gui = self.gui
        #RESOURCES["walkcompress.wav"].play(99)
        self.sr = self.player.GetAbility("spriteRenderer")
        # self.player2 = self.factory.Get("player",60,30,{"left":pygame.K_a,"right":pygame.K_d,"up":pygame.K_w,"down":pygame.K_s})
        # self.sr2 = self.player2.GetAbility("spriteRenderer")
        self.playGround = playground.Playground(
            [pygame.transform.scale(LEVELS.currlevel.resources["ground.png"],self.size), pygame.transform.scale(LEVELS.currlevel.resources["background.png"],self.size),
             pygame.transform.scale(LEVELS.currlevel.resources["ground_mask.png"],self.size)])

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
        if not LEVELS.currlevel: return None
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                OBJECTMANAGER.get_event(event)
            self.clock.tick(self.fps)

            self.on_loop()
            self.on_render()

        self.on_cleanup()
