import pygame
from objects.engine.Global import LEVELS
from objects.engine.Global import GAMECFG
class SpriteRenderer(pygame.sprite.Sprite):

    def __init__(self,group,gameObject):
        super().__init__(group)
        self.group = group
        self.gameObject = gameObject
        self.image = pygame.Surface([60, 60])
        self.load(gameObject.GetAbility("stateMashine").CurrentState())

    def load(self, state, animationStart=True):
        self.selectedState = state
        self.selectedOption = state.currentOption
        if animationStart :
            self.played = False
            self.frameCounter = 0
            self.frameIndex = 0
        self.loadedImage = state.currentSurface
        self.maxIndex = self.loadedImage.get_rect().height // 60


    def selectImage(self,index):
        if self.selectedState.loop: index = index % self.maxIndex
        elif index >= self.maxIndex:
            if(self.selectedState.nextState):
                self.gameObject.GetAbility("stateMashine").SetStateAsIs(self.selectedState.nextState, self.selectedState.currentOption)
                tmpState = self.selectedState
                self.load(self.selectedState.nextState)
                tmpState.nextState = None
            else:
                index = self.maxIndex-1
                self.played = True
        else: self.played = False
        self.image = pygame.Surface([60, 60])
        self.image.blit(self.loadedImage, (0, 0), pygame.Rect(0, index * 60, 60, 60))
        self.image.set_colorkey((0,255,0,0))
        self.mask = pygame.mask.from_surface(self.image)

    def update(self,dt):
        currentState = self.gameObject.GetAbility("stateMashine").CurrentState()
        if currentState!=self.selectedState:
            self.load(currentState);
        elif self.selectedOption != currentState.currentOption:
            self.load(currentState, False);

        self.rect.x ,self.rect.y = self.gameObject.pos
        if self.selectedState.ManualControl:
            self.selectImage(self.selectedState.IndManControl)
        else:
            self.frameCounter+= 1
            if self.frameCounter%(int)((1/dt)/self.selectedState.speed)==0:
                self.frameIndex +=1
            self.selectImage(self.frameIndex)

