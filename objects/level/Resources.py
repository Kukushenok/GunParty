import os

import pygame

import ResourceManager
import objects.level.Ground

pygame.init()
class Resources():
    def __init__(self,rootdir):
        self.resources={}
        for d,dirs,files in os.walk(rootdir):
            for i in files:
                if i.split(".")[-1] in ["png","jpg"]:
                    self.resources[i] = pygame.image.load(os.path.join(d,i))
                elif i.split(".")[-1] == "wav":
                    self.resources[i] = pygame.mixer.Sound(os.path.join(d,i))
        if self.resources.get("ground_mask.png"): self.resources["GROUNDMASK"] = \
            objects.level.Ground.Ground(pygame.transform.scale(self.resources["ground_mask.png"],
                                                               (ResourceManager.ResourceManager.instGameCFG().screenwidth,
                                                                ResourceManager.ResourceManager.instGameCFG().screenheight)))