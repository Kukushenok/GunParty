import pygame

import ResourceManager


class Playground():
    def __init__(self, images):

        self.mask = images[0].convert_alpha()
        self.sky = images[1].convert_alpha()
        self.ground = images[2].convert_alpha()
        self.composition = None
        self.update = True


    def render(self,screen):
        if self.composition==None or self.update:
            masked = self.ground.copy()
            masked.blit(self.mask, (0, 0), None, pygame.BLEND_RGBA_MULT)
            screen.blit(pygame.transform.scale(self.sky, (screen.get_rect()[2], screen.get_rect()[3])), screen.get_rect(),
                        screen.get_rect())
            screen.blit(pygame.transform.scale(masked, (screen.get_rect()[2], screen.get_rect()[3])), screen.get_rect(),
                        screen.get_rect())
            self.composition = screen.copy()
            self.update = False
        else:
            screen.blit(self.composition,(0,0), None)
