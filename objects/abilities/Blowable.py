class Blowable:
    def __init__(self,gameObject):
        self.gameObject = gameObject
        self.blowMask = None
        self.blowOnTimer = None
        self.blowOnTouch = False
    def update(self):
        if self.gameObject.GetAbility("physics").OnGround(): pass