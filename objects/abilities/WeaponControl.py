import pygame
import math
class WeaponControl:
    def __init__(self,gameObject):
        self.gameObject = gameObject
        self.takeOFFCoeff = 20
        self.blastForce = 1000
        self.killOnGround = True

    def updatePhisics(self, V, onGround):
        len = math.sqrt(V[0]**2+V[1]**2)
        if len>0:
            Vnorm=[V[0]/len,V[1]/len]
            cosAlpha = -Vnorm[1]
            alpha = math.acos(cosAlpha)*(180/math.pi)
            if V[0]>0:
                self.gameObject.GetAbility("stateMashine").CurrentState().IndManControl = (int)((alpha/360)*32)
                pass
            elif V[0]<0:
                self.gameObject.GetAbility("stateMashine").CurrentState().IndManControl =32-(int)((alpha / 360) * 32)
                pass
        if onGround and  self.killOnGround:
            self.gameObject.kill()
        elif onGround:
            if V[0]<0.1 or V[1]<0.1 :
                self.gameObject.GetAbility("spriteRenderer").stop = True
