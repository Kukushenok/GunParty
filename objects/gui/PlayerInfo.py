import pygame
import ResourceManager
class PlayerInfo():
    def __init__(self,gameObject):
        self.gameObject = gameObject
        self.frame = ResourceManager.ResourceManager.instResources()["rame.png"]
        self.font = pygame.font.SysFont("comicsansms", 12,True)
        self.text = self.font.render(str(self.gameObject.GetAbility("damagable").hp),True,pygame.Color("red"))
        self.framerect = self.text.get_rect()


    def render(self,screen):
        #self.image = pygame.transform.scale(self.frame.copy(), (self.framerect[2], self.framerect[3]))
        self.text = self.font.render(str(self.gameObject.GetAbility("damagable").hp),True,pygame.Color("red"))
        self.framerect = self.text.get_rect()
        #screen.blit(self.image,(self.gameObject.pos[0]+self.framerect.width,self.gameObject.pos[1]-10))
        screen.blit(self.text,(self.gameObject.pos[0]+self.framerect.width,self.gameObject.pos[1]-10))

