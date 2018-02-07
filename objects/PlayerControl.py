import pygame
class PlayerControl:
    def __init__(self,gameO,scheme):
        self.scheme = scheme
        self.gameObject= gameO
    def get_event(self,event):
        if event.type == pygame.KEYDOWN:
            if event.key == self.scheme["left"]:
                self.gameObject.GetAbility("stateMashine").current_state.SetCurrentState("u")
            elif event.key == self.scheme["right"]:
                self.gameObject.GetAbility("stateMashine").current_state.SetCurrentState("d")
