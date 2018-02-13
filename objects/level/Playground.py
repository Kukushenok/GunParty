import pygame
from objects.engine.Global import RESOURCES
from objects.engine.Global import LEVELS
class Playground():
    def __init__(self, images):


        self.mask = images[0].convert_alpha()
        self.sky = images[1].convert_alpha()
        self.ground = images[2].convert_alpha()



        self.tmpsurface = pygame.transform.scale(RESOURCES["blowmask.png"].convert_alpha(),(300,300))
        self.mask.blit(self.tmpsurface,(300,280),None,pygame.BLEND_RGBA_SUB)
        LEVELS.currlevel.resources["GROUNDMASK"].image.blit(self.tmpsurface, (3001, 280), None, pygame.BLEND_RGBA_SUB)
        LEVELS.currlevel.resources["GROUNDMASK"].update()


    def render(self,screen):
        masked = self.ground.copy()
        masked.blit(self.mask, (0, 0), None, pygame.BLEND_RGBA_MULT)
        screen.blit(pygame.transform.scale(self.sky, (screen.get_rect()[2], screen.get_rect()[3])), screen.get_rect(),
                    screen.get_rect())
        screen.blit(pygame.transform.scale(masked, (screen.get_rect()[2], screen.get_rect()[3])), screen.get_rect(),
                    screen.get_rect())
