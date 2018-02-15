import pygame
import math
class WeaponControl:
    def __init__(self,gameObject):
        self.gameObject = gameObject

    def updatePhisics(self, V, onGround):
        len = math.sqrt(V[0]**2+V[1]**2)
        if len>0:
            Vnorm=[V[0]/len,V[1]/len]
            cosAlpha = -Vnorm[1];
            alpha = math.acos(cosAlpha)*(180/math.pi)
            if alpha>180:
                alpha=alpha-180
            if V[0]>0:
                self.gameObject.GetAbility("stateMashine").CurrentState().IndManControl = 32-(int)((alpha/180)*32)
                pass
            elif V[0]<0:
                self.gameObject.GetAbility("stateMashine").CurrentState().IndManControl = 32-(int)((alpha / 180) * 32)
                pass