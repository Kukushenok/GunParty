import pygame
class PlayerControl:
    def __init__(self,gameO,scheme):
        self.scheme = scheme
        self.gameObject= gameO
        self.right_pressed = False
        self.left_pressed = False
        self.up_pressed = False
        self.down_pressed = False
        self.jump = 0
        self.left = False
    def get_event(self,event):
        if self.jump: return None
        if event.type == pygame.KEYDOWN:
            if event.key == self.scheme["left"] and not self.right_pressed:
                self.gameObject.GetAbility("stateMashine").SetState("movel")
                self.gameObject.GetAbility("stateMashine").current_state.SetCurrentState("n")
                self.left_pressed = True
                self.left = True
            if event.key == self.scheme["right"] and not self.left_pressed:
                self.gameObject.GetAbility("stateMashine").SetState("mover")
                self.gameObject.GetAbility("stateMashine").current_state.SetCurrentState("n")
                self.right_pressed = True
                self.left = False
            if event.key == self.scheme["up"]:
                self.jump = 1
                self.gameObject.GetAbility("stateMashine").SetState("jumpl" if self.left else "jumpr")
                self.gameObject.GetAbility("stateMashine").current_state.SetCurrentState("n")
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
        if self.right_pressed and not self.jump: self.gameObject.GetAbility("physics").Walk(dt,True)
        if self.left_pressed and not self.jump: self.gameObject.GetAbility("physics").Walk(dt, False)
        if self.jump==1 and self.gameObject.GetAbility("spriteRenderer").played:
            xForse = 0
            if self.right_pressed: xForse = 450
            elif self.left_pressed: xForse = -450
            self.gameObject.GetAbility("physics").AddForce([xForse, -700], 1 / 30, True)
            self.jump = 2
            self.gameObject.pos[1]-=5
            self.gameObject.GetAbility("stateMashine").SetState("flyl" if self.left else "flyr")
            self.gameObject.GetAbility("stateMashine").current_state.SetCurrentState("n")
            self.right_pressed = False
            self.left_pressed = False
            self.wasOn = True
        if self.jump ==2 and self.gameObject.GetAbility("physics").onGround:
            if not self.wasOn:
                self.gameObject.GetAbility("stateMashine").SetState("blinkl" if self.left else "blinkr")
                self.gameObject.GetAbility("stateMashine").current_state.SetCurrentState("n")
                self.jump = 0
        elif self.jump == 2: self.wasOn = False

