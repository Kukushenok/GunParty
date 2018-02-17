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

    #Расчёт ущерба. На вход подаётся длина вектора приложенной силы
    def applyDamage(self,forceDamage):
        isDamage = forceDamage-self.damageLimit
        if isDamage>0:
            self.hp = (int)(self.hp - min(forceDamage,self.maxForce)/(self.maxForce/self.maxDamage))

    def update(self,dt):
        if self.lifetime != -1:
            if self.lifetime >= 0:
                self.lifetime -=dt
                self.hp = int(self.lifetime)