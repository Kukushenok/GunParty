import pygame
from objects.engine.Global import LEVELS
from objects.engine.Global import GAMECFG
class SpriteRenderer(pygame.sprite.Sprite):

    def __init__(self,group,gameO):
        super().__init__(group)
        self.group = group
        self.gameObject = gameO
        self.speed = 20
        self.image = pygame.Surface([60, 60])
        self.load(gameO.GetAbility("stateMashine").CurrentState().currSurface,gameO.GetAbility("stateMashine").current_state.speed,True)
        self.frameCounter = 0
        self.frameIndex = 0
        self.loop = True
        self.played=False

    def load(self,image,speed,loop):
        self.loop = loop
        self.speed = speed
        self.played = False
        self.frameCounter = 0
        self.frameIndex = 0
        self.loadedImage = image
        self.maxIndex = self.loadedImage.get_rect().height // 60

    def loadOption(self,image, speed, loop):
        self.loop = loop
        self.speed = speed
        self.played = False
        self.loadedImage = image
        self.maxIndex = self.loadedImage.get_rect().height // 60


    def selectImage(self,index):
        if self.loop: index = index % self.maxIndex
        elif index >= self.maxIndex:
            index = self.maxIndex-1
            self.played = True
        else: self.played = False
        self.image = pygame.Surface([60, 60])
        self.image.blit(self.loadedImage, (0, 0), pygame.Rect(0, index * 60, 60, 60))
        self.image.set_colorkey((0,255,0,0))
        self.mask = pygame.mask.from_surface(self.image)

    def update(self,dt):
        self.rect.x ,self.rect.y = self.gameObject.pos
        self.frameCounter+= 1
        if self.frameCounter%(int)((1/dt)/self.speed)==0:
            self.frameIndex +=1
        self.selectImage(self.frameIndex)

