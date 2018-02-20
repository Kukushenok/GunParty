import pygame

import ResourceManager
import objects.gui.StartScreen


class ExitDialog():
    def __init__(self,holder,rect,log):
        self.log = log
        self.holder = holder
        self.rect = rect
        self.yesRect = pygame.Rect(self.rect[0],self.rect[1]+self.rect[3]//2,self.rect[2]//2,self.rect[3]//2)
        self.noRect = pygame.Rect(self.rect[0]+self.rect[2]//2, self.rect[1]+self.rect[3] // 2, self.rect[2] // 2, self.rect[3] // 2)
        self.image = pygame.transform.scale(ResourceManager.ResourceManager.instResources()["dialog.png"],(rect[2], rect[3]))
        self.font = pygame.font.SysFont("comicsansms", self.rect[3]//10)
        self.text = self.font.render(log, True,pygame.Color("black"))
        self.show = False
        if isinstance(holder, objects.gui.StartScreen.StartScreen):
            self.type = "SS"
        else:
            self.type = "GE"
    def exit(self):
        self.show = False
        if self.type == "SS":
            self.holder.running = False
            self.holder.gameEngine.running = False
        else:
            self.holder.run_start_screen()
    def render(self):
        if not self.show: return False
        self.holder.screen.blit(self.image, (self.rect[0], self.rect[1]))
        self.holder.screen.blit(self.text,(self.rect[0]+self.rect[2]//2-self.text.get_rect()[2]//2,self.rect[1]+self.text.get_rect()[3]))
    def get_event(self,event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and self.yesRect.collidepoint(event.pos):
                self.exit()
            if event.button == 1 and self.noRect.collidepoint(event.pos):
                self.show = False
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                self.show = not self.show
            if event.key == pygame.K_KP_ENTER and self.show:
                self.exit()