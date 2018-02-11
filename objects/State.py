class State:
    def __init__(self,gameO):
        self.gameObject = gameO
        self.surfaces = {"u":None,"d":None,"n":None}
        self.currOption = ""
        self.currSurface = None
        self.speed = 20
        self.loop = True

    def AddSurface(self,type,surface):
        self.surfaces[type] = surface

    def SetCurrentOption(self, type, start):
        if start:
            try:
                self.currSurface = self.surfaces[type]
                self.currOption = type
                self.gameObject.GetAbility("spriteRenderer").load(self.currSurface, self.speed, self.loop)
            except Exception:
                pass
        else:
            if(self.currOption!= type):
                self.currSurface = self.surfaces[type]
                self.currOption = type
                try:
                    self.gameObject.GetAbility("spriteRenderer").loadOption(self.currSurface,self.speed, self.loop)
                except Exception:
                    pass
