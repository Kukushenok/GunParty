import pygame
import objects.level.Resources
import tools.config
import os
import ResourceManager
class Level:
    def __init__(self, levelRoot, path):
        self.path = path
        self.levelRoot = levelRoot
    def load(self):
        self.resources = objects.level.Resources.Resources(self.path).resources
        self.config = tools.config.Config(self.levelRoot,self.path)

    def get_subnail(self,rect):
        self.load()
        self.resources["background.png"] = self.resources["background.png"].convert_alpha()
        self.resources["ground.png"] = self.resources["ground.png"].convert_alpha()
        self.resources["ground_mask.png"] = self.resources["ground_mask.png"].convert_alpha()
        masked = pygame.transform.scale(self.resources["ground.png"].copy(),(rect[2],rect[3]))
        masked.blit(pygame.transform.scale(self.resources["ground_mask.png"],(rect[2],rect[3])), (0, 0), None, pygame.BLEND_RGBA_MULT)
        res = pygame.transform.scale(self.resources["background.png"].copy(),(rect[2],rect[3]))
        res.blit(masked,(0,0))
        self.unload()
        return res

    def unload(self):
        self.resources = None

