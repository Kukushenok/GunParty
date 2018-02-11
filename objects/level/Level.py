import pygame
import objects.level.Resources as resources
class Level:
    def __init__(self, path):
        self.path = path
    def load(self):
        self.resources = resources.Resources(self.path).resources
    def unload(self):
        self.resources = None

