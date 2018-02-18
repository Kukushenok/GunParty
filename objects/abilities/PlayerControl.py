import pygame
import ResourceManager
import math
class PlayerControl:

    def __init__(self, gameO,scheme):
        self.scheme = scheme
        self.gameObject= gameO
        self.gui = self.gameObject.gui
        self.right_pressed = False
        self.left_pressed = False
        self.up_pressed = False
        self.down_pressed = False
        self.aim_up_pressed = False
        self.aim_down_pressed = False
        self.fire_pressed = False
        self.jump = 0
        self.left = False
        self.block_anim = False
        self.disable = False
        self.currweaponname = ""
        self.weapon = -1
        self.aim_speed = 10
        self.fire_speed = ResourceManager.ResourceManager.instGameCFG().fps
        self.armed = False
        self.frameCounter = 0

    def resetKeyButtons(self):
        self.right_pressed = False
        self.left_pressed = False
        self.up_pressed = False
        self.down_pressed = False
        self.aim_up_pressed = False
        self.aim_down_pressed = False
        self.fire_pressed = False
        self.jump = 0

    def WalkControl(self, event):
        if event.type == pygame.KEYDOWN:
            nextState = ""
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

            if (nextState!=""):
                self.LoadWeapon("",-1,nextState)

    def get_event(self,event):
        if self.disable:
            self.resetKeyButtons()
            return None
        self.WalkControl(event)
        if event.type == pygame.KEYDOWN:
            if event.key == self.scheme["up"]:
                if not self.block_anim:
                    self.gameObject.GetAbility("stateMashine").SetState("jumpl" if self.left else "jumpr")
                    self.block_anim = True
                    self.jump = 1

                self.up_pressed = True
            if event.key == self.scheme["down"]:
                self.down_pressed = True
            if event.key == self.scheme["aimup"]:
                self.aim_up_pressed = True
                if not self.jump and self.armed:
                    self.gameObject.GetAbility("stateMashine").SetState(self.currweaponname+("l" if self.left else "r"))

            if event.key == self.scheme["aimdown"]:
                self.aim_down_pressed = True
                if not self.jump and self.armed:
                    self.gameObject.GetAbility("stateMashine").SetState(self.currweaponname+("l" if self.left else "r"))
            if event.key == self.scheme["fire"]:
                if self.armed and not self.jump:
                    if self.gui.selected == 2:
                        angleIndex = self.gameObject.GetAbility("stateMashine").CurrentState().IndManControl
                        weaponObj = ResourceManager.ResourceManager.instFactory().get("bullet",
                                                                                      self.gameObject.pos[0],
                                                                                      self.gameObject.pos[1])
                        weaponControl = weaponObj.GetAbility("weaponControl")
                        angle = 5.625 * (angleIndex + 1)
                        forseVector = self.rotateVector([0, 1], angle * (1 if self.left else -1))
                        forseVector = [forseVector[0] * weaponControl.takeOFFCoeff*2,
                                       forseVector[1] * weaponControl.takeOFFCoeff*2]
                        weaponObj.GetAbility("physics").weaponFire(1 / 30, forseVector)
                self.fire_pressed = True

        if event.type == pygame.KEYUP:
            if event.key == self.scheme["left"]:
                if not self.block_anim:
                    if self.armed:
                        self.LoadWeapon(self.currweaponname,self.gui.selected,"")
                    else:
                        self.gameObject.GetAbility("stateMashine").SetState("blinkl")
                    self.left_pressed = False
            if event.key == self.scheme["right"]:
                if not self.block_anim:
                    if self.armed:
                        self.LoadWeapon(self.currweaponname,self.gui.selected,"")
                    else:
                        self.gameObject.GetAbility("stateMashine").SetState("blinkr")
                    self.right_pressed = False
            if event.key == self.scheme["up"]:
                self.up_pressed = False
            if event.key == self.scheme["down"]:
                self.down_pressed = False
            if event.key == self.scheme["switchweaponl"] or event.key == self.scheme["switchweaponr"]:
                if self.gui.selected == 0 and self.currweaponname != "baz" and not self.block_anim:
                    self.gui.forceInd.enabled = True
                    self.LoadWeapon("baz", self.gui.selected)
                if self.gui.selected == 1 and self.currweaponname != "grn" and not self.block_anim:
                    self.gui.forceInd.enabled = True
                    self.LoadWeapon("grn", self.gui.selected)
                if self.gui.selected == 2 and self.currweaponname != "shg" and not self.block_anim:
                    self.LoadWeapon("shg", self.gui.selected)
                    self.gui.forceInd.enabled = False
            if event.key == self.scheme["aimup"]:
                self.aim_up_pressed = False
            if event.key == self.scheme["aimdown"]:
                self.aim_down_pressed = False
            if event.key == self.scheme["fire"]:
                if (self.armed and not self.jump) and (self.gui.selected == 0 or self.gui.selected == 1):
                    angleIndex = self.gameObject.GetAbility("stateMashine").CurrentState().IndManControl
                    angle = 5.625 * (angleIndex + 1)
                    takeOffVector = self.rotateVector([0, -30], angle)

                    if self.gui.selected == 0:
                        weaponName = "missile"
                    else:
                        weaponName = "grenade"
                    if self.left:
                        weaponObj = ResourceManager.ResourceManager.instFactory().get(weaponName,
                                                                                      self.gameObject.pos[0] - takeOffVector[0],
                                                                                      self.gameObject.pos[1]- takeOffVector[1])
                    else:
                        weaponObj = ResourceManager.ResourceManager.instFactory().get(weaponName,
                                                                                      self.gameObject.pos[0] +
                                                                                      takeOffVector[0],
                                                                                      self.gameObject.pos[1] -
                                                                                      takeOffVector[1])
                    weaponControl = weaponObj.GetAbility("weaponControl")
                    forseVector = self.rotateVector([0, 1], angle * (1 if self.left else -1))
                    forseVector = [forseVector[0] * weaponControl.takeOFFCoeff * self.gameObject.gui.forceInd.coeff,
                                   forseVector[1] * weaponControl.takeOFFCoeff * self.gameObject.gui.forceInd.coeff]
                    weaponObj.GetAbility("physics").weaponFire(1 / 30, forseVector)
                self.fire_pressed = False

    def rotateVector(self, vector, angle):
        resultVector=[0,0]
        resultVector[0] = vector[0] * math.cos(angle * math.pi/180) - vector[1] * math.sin(angle * math.pi / 180);
        resultVector[1] = vector[1] * math.cos(angle * math.pi / 180) + vector[0] * math.sin(angle * math.pi / 180);
        return resultVector

    def LoadWeapon(self,name="",idx=-1, nextState=""):
        if self.weapon==-1 and self.currweaponname!="" and name!="":
            self.gameObject.GetAbility("stateMashine").BindStates(self.currweaponname + ("bakr" if self.left else "bakl"),
                                                                  name + ("lnkl" if self.left else "lnkr"))
            self.currweaponname = name
            self.gameObject.GetAbility("stateMashine").SetState(self.currweaponname + ("bakr" if self.left else "bakl"))
            self.weapon = self.gui.selected
        else:
            if idx==-1 or name=="":
                if nextState!="":
                    self.gameObject.GetAbility("stateMashine").BindStates(
                        self.currweaponname + ("bakr" if self.left else "bakl"),
                        nextState)
                    self.gameObject.GetAbility("stateMashine").SetState(
                        self.currweaponname + ("bakr" if self.left else "bakl"))
                self.currweaponname = ""
                self.weapon = -1
                self.armed = False
                return None
            self.currweaponname = name
            self.gameObject.GetAbility("stateMashine").SetState(self.currweaponname + ("lnkl" if self.left else "lnkr"))
        self.armed = True
        self.weapon = idx

    def update(self,dt):
        if self.disable:
            self.resetKeyButtons()
            return None
        # if self.weapon == 1 and self.gameObject.GetAbility("spriteRenderer").played:
        #     self.gameObject.GetAbility("stateMashine").SetState(self.currweaponname+"l" if self.left else self.currweaponname+"r")
        #     self.block = False
        if not self.jump and self.fire_pressed:
            self.frameCounter+=1
            if self.frameCounter % int(((1 / dt) / self.fire_speed)) == 0 and self.gameObject.gui.forceInd.coeff<100:
                self.gameObject.gui.forceInd.coeff += 1
        else:
            self.gameObject.gui.forceInd.coeff = 0

        if not self.jump and self.aim_up_pressed:
            self.frameCounter+= 1
            if self.frameCounter%int(((1/dt)/self.aim_speed))==0 and self.gameObject.GetAbility("stateMashine").CurrentState().IndManControl < 31:
                self.gameObject.GetAbility("stateMashine").CurrentState().IndManControl += 1
        elif not self.jump and self.aim_down_pressed:
            self.frameCounter+= 1
            if self.frameCounter%int(((1/dt)/self.aim_speed))==0 and self.gameObject.GetAbility("stateMashine").CurrentState().IndManControl > 0:
                self.gameObject.GetAbility("stateMashine").CurrentState().IndManControl -= 1
        if self.right_pressed and not self.jump: self.gameObject.GetAbility("physics").Walk(dt,True)
        if self.left_pressed and not self.jump: self.gameObject.GetAbility("physics").Walk(dt, False)
        if self.jump==1 and self.gameObject.GetAbility("spriteRenderer").played:
            dir="up"
            if self.left_pressed:
                dir="left"
            if self.right_pressed:
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
                if self.armed:
                    self.LoadWeapon(self.currweaponname, self.gui.selected, "")
                else:
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
