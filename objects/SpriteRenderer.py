import pygame
from objects.Global import LEVELS
class SpriteRenderer(pygame.sprite.Sprite):
    def __init__(self,image,group):
        super().__init__(group)
        self.group = group
        self.load(image)
    def load(self,image):
        self.image = pygame.Surface([60,60])
        self.loadedImage = image
        self.maxIndex = self.loadedImage.get_rect().height // 60
        self.groundCollide = LEVELS.currlevel.resources["GROUNDMASK"]

    def selectImage(self,index):
        index = index % self.maxIndex
        self.image = pygame.Surface([60,60])
        self.image.blit(self.loadedImage, (0, 0), pygame.Rect(0, index * 60, 60, 60))
        self.image.set_colorkey((0,255,0,0))
        self.mask = pygame.mask.from_surface(self.image)

    def update(self,dt):

        offset_x, offset_y = self.rect.left,self.rect.top
        if (self.groundCollide.mask.overlap(self.mask, (offset_x, offset_y)) == None):
            self.rect = self.rect.move(1,1)
        else:
            self.rect = self.rect.move(-2, 0)

        # #if not pygame.sprite.collide_mask(self, self.groundCollide):
        # if len(pygame.sprite.spritecollide(self,self.group,False)) == 1:
        #     self.rect = self.rect.move(1, 1)
        # print(pygame.sprite.spritecollide(self,self.group,False))