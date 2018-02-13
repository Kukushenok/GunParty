import pygame
class PlayerControl:

    def __init__(self,gameO,scheme):
        self.scheme = scheme
        self.gameObject= gameO
        self.gui = None
        self.right_pressed = False
        self.left_pressed = False
        self.up_pressed = False
        self.down_pressed = False
        self.jump = 0
        self.left = False
        self.block_anim = False
        self.block = False
        self.currweaponname = None
        self.weapon = 0

    def get_event(self,event):
        if self.block:
            self.right_pressed=False
            self.left_pressed=False
            self.up_pressed = False
            self.down_pressed = False
            return None
        if event.type == pygame.KEYDOWN:
            if event.key == self.scheme["left"] and not self.right_pressed:
                self.left = True
                if not self.block_anim:
                    self.gameObject.GetAbility("stateMashine").SetState("movel")
                self.left_pressed = True
            if event.key == self.scheme["right"] and not self.left_pressed:
                if not self.block_anim:
                    self.gameObject.GetAbility("stateMashine").SetState("mover")
                self.right_pressed = True
                self.left = False
            if event.key == self.scheme["up"]:
                if not self.block_anim:
                    self.gameObject.GetAbility("stateMashine").SetState("jumpl" if self.left else "jumpr")
                    self.block_anim = True
                    self.jump = 1
                self.up_pressed = True

            if event.key == self.scheme["down"]:
                self.down_pressed = True

        if event.type == pygame.KEYUP:
            if event.key == self.scheme["left"]:
                if not self.block_anim:
                    self.gameObject.GetAbility("stateMashine").SetState("blinkl")
                    self.left_pressed = False
            if event.key == self.scheme["right"]:
                if not self.block_anim:
                    self.gameObject.GetAbility("stateMashine").SetState("blinkr")
                    self.right_pressed = False
            if event.key == self.scheme["up"]:
                self.up_pressed = False
            if event.key == self.scheme["down"]:
                self.down_pressed = False
    def LoadWeapon(self,name):
        if self.currweaponname:
            self.gameObject.GetAbility("stateMashine").SetState(self.currweaponname + ("bakr" if self.left else "bakl"))
            return None
        self.block = True
        try:
            self.gameObject.GetAbility("stateMashine").SetState("bazlnkl" if self.left else "bazlnkr")
            self.weapon = 1
        except Exception:pass
        self.currweaponname = name
    def update(self,dt):
        if self.gui.selected == 0 and self.currweaponname != "baz" and not self.jump:
            self.LoadWeapon("baz")
        if self.gui.selected == 1 and self.currweaponname != "grn" and not self.jump:
            self.LoadWeapon("grn")
        if self.gui.selected == 2 and self.currweaponname != "shg" and not self.jump:
            self.LoadWeapon("shg")
        if self.weapon == 1 and self.gameObject.GetAbility("spriteRenderer").played:
            self.gameObject.GetAbility("stateMashine").SetState(self.currweaponname+"l" if self.left else self.currweaponname+"r")
            self.block = False
        if self.right_pressed and not self.jump: self.gameObject.GetAbility("physics").Walk(dt,True)
        if self.left_pressed and not self.jump: self.gameObject.GetAbility("physics").Walk(dt, False)
        if self.jump==1 and self.gameObject.GetAbility("spriteRenderer").played:
            dir="up"
            if(self.left_pressed):
                dir="left"
            if(self.right_pressed):
                dir="right"
            self.gameObject.GetAbility("physics").Jump(1 / 30, dir)
            self.jump = 2
            self.gameObject.pos[1]-=10
            self.gameObject.GetAbility("stateMashine").SetState("flyl" if self.left else "flyr")
            self.right_pressed = False
            self.left_pressed = False
            self.wasOn = True
        if self.jump ==2 and self.gameObject.GetAbility("physics").onGround:
            if not self.wasOn:
                self.gameObject.GetAbility("stateMashine").SetState("blinkl" if self.left else "blinkr")
                self.jump = 0
                self.block_anim = False
        elif self.jump == 2: self.wasOn = False

        check = self.gameObject.GetAbility("physics").CheckTail()
        if check == [0,0,0] or check == [1,1,1]: self.gameObject.GetAbility("stateMashine").current_state.SetCurrentOption("n")
        elif check[0] == 0:
            self.gameObject.GetAbility("stateMashine").current_state.SetCurrentOption("d" if self.left else "u")
        elif check[2] == 0:
            self.gameObject.GetAbility("stateMashine").current_state.SetCurrentOption("u" if self.left else "d")
