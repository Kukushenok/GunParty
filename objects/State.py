class State:
    def __init__(self,gameO):
        self.gameObject = gameO
        self.surfaces = {"u":None,"d":None,"n":None}
        self.currOption = ""
        self.currSurface = None
        self.spd = 20
        self.loop = True
    def AddSurface(self,type,surface):
        self.surfaces[type] = surface
    def SetCurrentOption(self, type):
        if(self.currOption!= type or  self != self.gameObject.GetAbility("stateMashine").CurrentState()):
            self.currSurface = self.surfaces[type]
            self.currOption = type
            try:
                if(self == self.gameObject.GetAbility("stateMashine").CurrentState()):
                    index = self.gameObject.GetAbility("spriteRenderer").frameIndex
                    self.gameObject.GetAbility("spriteRenderer").load(self.currSurface, self.spd, self.loop)
                    self.gameObject.GetAbility("spriteRenderer").selectFrame(index)
                    self.gameObject.GetAbility("spriteRenderer").frameIndex = index
            except Exception: pass