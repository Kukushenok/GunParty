import pygame

import ResourceManager
import objects.gui.ExitDialog
import objects.gui.LevelSubnail
import objects.gui.Scroller
import objects.gui.StartScreen
import objects.gui.SwitchPageButton
import objects.gui.Text
import objects.level.Playground
import tools.config

class GameEngine:
    def __init__(self):
        pygame.init()
        cnf = tools.config.Config()
        self.fps = float(cnf.get("fps"))
        self.size = int(cnf.get("width")), int(cnf.get("height"))
        if cnf.get("fullscreen") != "0":
            self.screen = pygame.display.set_mode(self.size,pygame.FULLSCREEN|pygame.DOUBLEBUF)
        else:
            self.screen = pygame.display.set_mode(self.size)
        self.clock = pygame.time.Clock()
        self.running = True
        ResourceManager.ResourceManager.instGameCFG().screenwidth, ResourceManager.ResourceManager.instGameCFG().screenheight = self.size
        ResourceManager.ResourceManager.instGameCFG().fullscreen = cnf.get("fullscreen") != 0
        ResourceManager.ResourceManager.instGameCFG().fps = self.fps
        self.cnf = cnf
        self.coeff = ResourceManager.ResourceManager.instGameCFG().GetScreenCoeff()
        self.load_start_screen()

    def load_start_screen(self):
        self.startScreen = objects.gui.StartScreen.StartScreen(self,self.screen)
        cx = self.coeff[0]
        cy = self.coeff[1]
        i = -1
        page = 0
        rect = None
        for e in ResourceManager.ResourceManager.intsLevels().levels.keys():
            i += 1
            if i == 0:
                rect = pygame.Rect(20 * cx, 20 * cy, 320 * cx, 200 * cy)
            elif i == 1:
                rect = pygame.Rect(360 * cx, 20 * cy, 320 * cx, 200 * cy)
            elif i == 2:
                rect = pygame.Rect(700 * cx, 20 * cy, 320 * cx, 200 * cy)
            else:
                i = -1
                rect = pygame.Rect(1040 * cx, 20 * cy, 320 * cx, 200 * cy)
                page += 1
            levelsub = objects.gui.LevelSubnail.LevelSubnail(self.startScreen,e,rect,page if i!=-1 else page-1)
            txt = objects.gui.Text.Text(self.startScreen,(rect[0],rect[1]+200*cy),levelsub.level.config.get("name"),int(40*cy),pygame.Color("black"))
            txt.page = page if i!=-1 else page-1
            self.startScreen.AddComponent(levelsub)
            self.startScreen.AddComponent(txt)


        self.startScreen.maxPage = page-1 if i==-1 else page
        self.startScreen.AddComponent(objects.gui.SwitchPageButton.SwitchPageButton(self.startScreen,-1,pygame.Rect(1500*cx,40*cy,120*cx,150*cy)))
        self.startScreen.AddComponent(objects.gui.SwitchPageButton.SwitchPageButton(self.startScreen,1,pygame.Rect(1700*cx,40*cy,120*cx,150*cy)))
        #self.startScreen.AddComponent(objects.gui.Scroller.Scroller(self.startScreen,pygame.Rect(1500*cx,300*cy,240*cx,60*cy)))
        self.startScreen.AddComponent(objects.gui.ExitDialog.ExitDialog(self.startScreen,
                                                                        pygame.Rect(530 * cx, 320 * cy, 860 * cx,
                                                                                    440 * cy),"Are you sure to want to exit?"))
        #self.startScreen.AddComponent(objects.gui.Text.Text(self.startScreen,(1500*cx,230*cy),"Gravity",int(50*cy),pygame.Color("black")))
        self.startScreen.run()
        self.exitButton = objects.gui.ExitDialog.ExitDialog(self, pygame.Rect(530 * cx, 320 * cy, 860 * cx, 440 * cy),
                                                            "Are you sure to want to exit?")

    def run_start_screen(self):
        ResourceManager.ResourceManager.intsLevels().currlevel.resources["backgroundMusic.wav"].stop()
        self.startScreen.running = True
        self.startScreen.run()

    def load_level(self,name):
        ResourceManager.ResourceManager.instObjectManager().clear()
        self.all_sprites = pygame.sprite.Group()
        self.factory = ResourceManager.ResourceManager.instFactory()
        self.factory.initFactory(self.all_sprites)
        ResourceManager.ResourceManager.intsLevels().loadLevel(name)
        self.levelConfig = ResourceManager.ResourceManager.intsLevels().currlevel.config
        self.i = 0
        self.player = self.factory.get("player",int(self.levelConfig.get("player2x"))*self.coeff[0],int(self.levelConfig.get("player2y"))*self.coeff[1],self.cnf.getAsDict("player2KeyScheme"),(1600*self.coeff[0],10*self.coeff[1]),self.screen)
        self.player.GetAbility("physics").G = float(self.levelConfig.get("gravity"))
        self.player.GetAbility("physics").SetGravity(True)
        self.player2 = self.factory.get("player",int(self.levelConfig.get("player1x"))*self.coeff[0],int(self.levelConfig.get("player1y"))*self.coeff[1],self.cnf.getAsDict("player1KeyScheme"),(10*self.coeff[0],10*self.coeff[1]),self.screen)
        self.player2.GetAbility("physics").G = float(self.levelConfig.get("gravity"))
        self.player2.GetAbility("physics").SetGravity(True)
        ResourceManager.ResourceManager.intsLevels().currlevel.resources["backgroundMusic.wav"].set_volume(0.6)
        ResourceManager.ResourceManager.intsLevels().currlevel.resources["backgroundMusic.wav"].play(-1)
        self.sr = self.player.GetAbility("spriteRenderer")
        self.playGround = objects.level.Playground.Playground(
            [pygame.transform.scale(
                ResourceManager.ResourceManager.intsLevels().currlevel.resources["ground.png"],self.size),
                pygame.transform.scale(
                ResourceManager.ResourceManager.intsLevels().currlevel.resources["background.png"],self.size),
             pygame.transform.scale(
                 ResourceManager.ResourceManager.intsLevels().currlevel.resources["ground_mask.png"],self.size)])
        ResourceManager.ResourceManager.playground = self.playGround

    def on_loop(self):
        ResourceManager.ResourceManager.instObjectManager().update(1 / self.fps)

    def on_render(self):
        self.screen.fill((0, 0, 0))
        self.playGround.render(self.screen)
        self.all_sprites.draw(self.screen)
        ResourceManager.ResourceManager.instObjectManager().renderGUIs(self.screen)
        self.exitButton.render()
        pygame.display.flip()
        pygame.display.update()

    def on_cleanup(self):
        pygame.quit()

    def run(self):
        if not ResourceManager.ResourceManager.intsLevels().currlevel: return None
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                self.exitButton.get_event(event)
                if not self.exitButton.show:
                    ResourceManager.ResourceManager.instObjectManager().get_event(event)
            self.clock.tick(self.fps)
            if not self.exitButton.show:
                self.on_loop()
            self.on_render()
        self.on_cleanup()
