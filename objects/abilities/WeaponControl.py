import pygame
import math
import ResourceManager
import random
class WeaponControl:
    def __init__(self,gameObject):
        self.gameObject = gameObject
        self.takeOFFCoeff = 20
        self.blastForce = 300
        self.killOnGround = True
        self.hp = -1

    def applyBlowInfluence(self, V, onGround):

        try:
            self.hp = self.gameObject.GetAbility("damagable").hp
        except Exception: pass

        if (onGround and self.killOnGround) or (self.hp != -1 and self.hp < 1):
            try:
                self.gameObject.GetAbility("audible").playSound("explode")
            except KeyError:pass

            blowd = int(self.blastForce * min(ResourceManager.ResourceManager.instGameCFG().GetScreenCoeff()))
            pos = self.gameObject.pos[0] - blowd // 2 + 30, self.gameObject.pos[1] - blowd // 2 + 30
            self.tmpsurface = pygame.transform.scale(
                ResourceManager.ResourceManager.instResources()["blowmask.png"].convert_alpha(), (blowd, blowd))
            ResourceManager.ResourceManager.playground.mask.blit(self.tmpsurface, (pos), None, pygame.BLEND_RGBA_SUB)

            ResourceManager.ResourceManager.intsLevels().currlevel.resources["GROUNDMASK"].image.blit(self.tmpsurface,
                                                                                                      pos, None,
                                                                                                      pygame.BLEND_RGBA_SUB)
            ResourceManager.ResourceManager.intsLevels().currlevel.resources["GROUNDMASK"].update()
            ResourceManager.ResourceManager.playground.update = True
            for e in range(5):
                ResourceManager.ResourceManager.instFactory().get("particle", self.gameObject.pos[0]+random.randint(-30,30),
                                                                  self.gameObject.pos[1] + random.randint(-30, 30),
                                                                  self.gameObject.GetAbility("physics").G)
            objects = ResourceManager.ResourceManager.instObjectManager().objects
            for e in objects:
                if e.__class__.__name__ == "GameObject":
                    if 'physics' in e.abilities:
                        screenCoeff = min(ResourceManager.ResourceManager.instGameCFG().GetScreenCoeff())
                        V = [e.pos[0] - self.gameObject.pos[0], e.pos[1] - self.gameObject.pos[1]]
                        len = math.sqrt(V[0] ** 2 + V[1] ** 2)
                        if len > 0:
                            forseCoeff = self.blastForce / (len ** 2 * screenCoeff ** 2)
                        else:
                            forseCoeff = self.blastForce
                        forseVector = [V[0] * forseCoeff * 15, V[1] * forseCoeff * 15]
                        lenForce = math.sqrt(forseVector[0] ** 2 + forseVector[1] ** 2)
                        e.GetAbility("physics").weaponFire(1 / 30, forseVector)
                        if 'damagable' in e.abilities:
                            e.GetAbility("damagable").applyDamage(lenForce)
            self.gameObject.kill()
        elif onGround:
            if V[0] < 0.1 or V[1] < 0.1:
                self.gameObject.GetAbility("spriteRenderer").stop = True


    def updatePhysics(self, V, onGround):
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
        self.applyBlowInfluence(V, onGround)


