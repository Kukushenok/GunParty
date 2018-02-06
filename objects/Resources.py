import os
import pygame
import objects.Ground as ground
import objects.Global
class Resources():
    def __init__(self,rootdir):
        self.resources={}
        for d,dirs,files in os.walk(rootdir):
            for i in files:
                self.resources[i] = pygame.image.load(os.path.join(d,i))
        if self.resources.get("soil.png"):self.resources["GROUNDMASK"] = ground.Ground(
            pygame.transform.scale(self.resources["soil.png"], (objects.Global.GAMECFG.screenwidth,
                                                                objects.Global.GAMECFG.screenheight)))