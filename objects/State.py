class State:
    def __init__(self,gameO):
        self.gameObject = gameO
        self.surfaces = {"u":None,"d":None,"n":None}
        self.currstate = None
    def AddSurface(self,type,surface):
        self.surfaces[type] = surface
    def SetCurrentState(self,type):
        self.currstate = self.surfaces[type]
        try:
            if self == self.gameObject.GetAbility("stateMashine").CurrentState():
                self.gameObject.GetAbility("spriteRenderer").load(self.currstate)
        except Exception: pass