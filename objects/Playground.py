import pygame
class Playground():
    def __init__(self,imagePaths):
        self.load(imagePaths)
    def load(self,imagePaths):
        self.mask = pygame.image.load(imagePaths[0]).convert_alpha()
        self.sky = pygame.image.load(imagePaths[1]).convert_alpha()
        self.ground = pygame.image.load(imagePaths[2]).convert_alpha()
    def render(self,screen):
        masked = self.ground.copy()
        masked.blit(self.mask, (0, 0), None, pygame.BLEND_RGBA_MULT)
        screen.blit(pygame.transform.scale(self.sky, (screen.get_rect()[2], screen.get_rect()[3])), screen.get_rect(),
                    screen.get_rect())
        screen.blit(pygame.transform.scale(masked, (screen.get_rect()[2], screen.get_rect()[3])), screen.get_rect(),
                    screen.get_rect())
