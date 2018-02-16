class Damagable():
    def __init__(self,gameObject):
        self.gameObject = gameObject
        self.hp = 100
        self.gui = gameObject.gui
        self.lifetime = -1
    def update(self,dt):
        if self.lifetime != -1:
            if self.lifetime >= 0:
                self.lifetime -=dt
                self.hp = int(self.lifetime)