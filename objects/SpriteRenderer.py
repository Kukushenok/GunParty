import pygame
class SpriteRenderer(pygame.sprite.Sprite):
    def __init__(self,path,group):
        super().__init__(group)
        self.image = pygame.Surface([60,60])
        self.load(path)
        self.maxIndex = self.loaded_image.get_rect().height // 60

    def selectImage(self,index):
        index = index % self.maxIndex
        self.image.blit(self.loaded_image, (0, 0), pygame.Rect(0, index*60, 60, 60))
        self.image.set_colorkey(self.image.get_at((0, 0)))

    def load(self,path):
        self.loaded_image = pygame.image.load(path)
        self.loaded_image.set_colorkey(self.loaded_image.get_at((0,0)))



    def update(self):
        self.rect = self.rect.move(0,0)

