import ResourceManager
class Damagable():
    def __init__(self,gameObject):
        self.gameObject = gameObject
        self.hp = 100
        self.gui = gameObject.gui
        self.lifetime = -1
        #Предел приложенной силы, после чего начинаются повреждения объекта
        self.damageLimit = 200
        #Максимально возможные повреждения за раз
        self.maxDamage = 50
        #Сила максимального повреждения
        self.maxForce = 500
        self.kill = False

    #Расчёт ущерба. На вход подаётся длина вектора приложенной силы
    def applyDamage(self,forceDamage):
        isDamage = forceDamage-self.damageLimit
        if isDamage>0:
            self.hp = int(self.hp - min(forceDamage,self.maxForce)/(self.maxForce/self.maxDamage))
        if self.hp<=0:
            try:
                self.gameObject.GetAbility("stateMashine").SetState("died")
                self.gameObject.GetAbility("playerControl").disable = True
                objects = ResourceManager.ResourceManager.instObjectManager().objects
                activePlayers = []
                for e in objects:
                    if e.__class__.__name__ == "GameObject" and e != self.gameObject:
                        if 'playerControl' in e.abilities:
                            if e.GetAbility("damagable").hp >0:
                                activePlayers.append(e)
                if len(activePlayers)==1:
                    activePlayers[0].GetAbility("stateMashine").SetState("win")
                    activePlayers[0].GetAbility("playerControl").disable = True
                    activePlayers[0].GetAbility("audible").playSound("victory")
            except Exception: pass

    def update(self,dt):
        if self.lifetime != -1:
            if self.lifetime >= 0:
                self.lifetime -=dt
                self.hp = int(self.lifetime)
        if self.hp == 0 and self.kill:
            self.gameObject.kill()