import pygame
class PlayerControl:
    def __init__(self,gameO,scheme):
        self.scheme = scheme
        self.gameObject= gameO
        self.right_pressed = False
        self.left_pressed = False
        self.up_pressed = False
        self.down_pressed = False

    def get_event(self,event):
        if event.type == pygame.KEYDOWN:
            if event.key == self.scheme["left"] and not self.right_pressed:
                self.gameObject.GetAbility("stateMashine").SetState("movel")
                self.gameObject.GetAbility("stateMashine").current_state.SetCurrentState("n")
                self.left_pressed = True
            if event.key == self.scheme["right"] and not self.left_pressed:
                self.gameObject.GetAbility("stateMashine").SetState("mover")
                self.gameObject.GetAbility("stateMashine").current_state.SetCurrentState("n")
                self.right_pressed = True
            if event.key == self.scheme["up"]:

                self.up_pressed = True
            if event.key == self.scheme["down"]:
                self.down_pressed = True

        if event.type == pygame.KEYUP:
            if event.key == self.scheme["left"]:
                self.gameObject.GetAbility("stateMashine").SetState("blinkl")
                self.gameObject.GetAbility("stateMashine").current_state.SetCurrentState("n")
                self.left_pressed = False
            if event.key == self.scheme["right"]:
                self.gameObject.GetAbility("stateMashine").SetState("blinkr")
                self.gameObject.GetAbility("stateMashine").current_state.SetCurrentState("n")
                self.right_pressed = False
            if event.key == self.scheme["up"]:
                self.up_pressed = False
            if event.key == self.scheme["down"]:
                self.down_pressed = False
    def update(self,dt):
        if self.right_pressed: self.gameObject.GetAbility("physics").Walk(dt,True)
        if self.left_pressed: self.gameObject.GetAbility("physics").Walk(dt, False)
        if self.up_pressed:
            xForse = 0
            if self.right_pressed: xForse = 450
            elif self.left_pressed: xForse = -450
            self.gameObject.GetAbility("physics").AddForce([xForse, -700], 1 / 30, True)

