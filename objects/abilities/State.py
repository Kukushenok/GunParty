class State:
    def __init__(self,gameO):
        self.gameObject = gameO
        self.surfaces = {"u":None,"d":None,"n":None}
        self.currentOption = ""
        self.currentSurface = None
        self.speed = 20
        self.loop = True
        self.nextState = None
        self.ManualControl = False
        self.IndManControl = 15

    def AddSurface(self, option, surface):
        self.surfaces[option] = surface

    def SetCurrentOption(self, option):
        self.currentSurface = self.surfaces[option]
        self.currentOption = option

