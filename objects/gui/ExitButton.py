import pygame
import objects.gui.StartScreen as startScreen
from objects.engine.Global import RESOURCES
class ExitButton():
    def __init__(self,holder,rect):
        self.holder = holder
        self.rect = rect
        if isinstance(holder,startScreen.StartScreen):
            self.image = pygame.transform.scale(RESOURCES["exit.png"],(rect[2],rect[3]))
            self.type = "SS"
        else:
            self.image = pygame.transform.scale(RESOURCES["back.png"], (rect[2], rect[3]))
            self.type = "GE"
    def render(self):
        self.holder.screen.blit(self.image, (self.rect[0], self.rect[1]))
    def get_event(self,event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and self.rect.collidepoint(event.pos):
                if self.type == "SS":
                    self.holder.running = False
                    self.holder.gameEngine.running = False
                else:
                    self.holder.run_start_screen()