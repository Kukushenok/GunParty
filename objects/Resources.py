import os
import pygame
class Resources():
    groundsPath = os.path.join(os.getcwd(), "resources", "images","grounds")
    masksPath = os.path.join(os.getcwd(), "resources", "images","masks")
    skiesPath = os.path.join(os.getcwd(), "resources", "images","skies")
    spritesPath = os.path.join(os.getcwd(), "resources", "images","sprites")
    resourcesPath = [groundsPath,masksPath,skiesPath,spritesPath]
    resources = {}
    def __init__(self):
        for e in self.resourcesPath:
            for d,dirs,files in os.walk(e):
                for i in files:
                    self.resources[i] = pygame.image.load(os.path.join(d,i))