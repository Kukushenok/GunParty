class State:
    def __init__(self,gameO):
        self.gameObject = gameO
        self.surfaces = {"u":None,"d":None,"n":None}
        self.currstate = None
        self.spd = 20
        self.loop = True
    def AddSurface(self,type,surface):
        self.surfaces[type] = surface
    def SetCurrentState(self,type):
        self.currstate = self.surfaces[type]
        try:
            if self == self.gameObject.GetAbility("stateMashine").CurrentState():
                self.gameObject.GetAbility("spriteRenderer").load(self.currstate,self.spd,self.loop)
        except Exception: pass