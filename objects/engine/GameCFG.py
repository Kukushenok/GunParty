class GameCFG:
    def __init__(self):
        self.screenheight = None
        self.screenwidth = None
        self.fullscreen = None
        self.fps = None
    def GetScreenCoeff(self):
        return self.screenwidth/1920, self.screenheight/1080