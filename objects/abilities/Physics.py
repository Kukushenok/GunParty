from objects.engine.Global import LEVELS
from objects.engine.Global import GAMECFG
class Physics:

    def __init__(self,gameO):
        self.gameObject = gameO
        self.groundCollide = LEVELS.currlevel.resources["GROUNDMASK"]
        self.M = 5
        self.G = 9.8
        self.coeff = 0.5
        self.AirRo = 1.2
        self.Sx = 1
        self.Sy = 3
        self.KFriction = 0.95
        self.GRNDFriction = [0,0]
        self.CurrForce = [0,0]
        self.V = [0,0]
        self.ScaleMx = GAMECFG.screenwidth/20
        self.ScaleMy = GAMECFG.screenheight/10
        self.onGround = False
        self.walkSpeed = 1
        self.xborders = [0, GAMECFG.screenwidth]
        self.yborder = [0, GAMECFG.screenheight]

    def SetGravity(self,gr):
        if gr: self.CurrForce = [0,self.M*self.G]
        else: self.CurrForce = [0,0]

    def TouchBorders(self,futpos):
        if futpos[0]+60 >= self.xborders[1] or futpos[0] <= self.xborders[0] or futpos[1]<=self.yborder[0] or \
                        futpos[1]+60 >= self.yborder[1]:
            if all([futpos[0]+60 >= self.xborders[1] or futpos[0] <= self.xborders[0],futpos[1]<=self.yborder[0] or
                            futpos[1]+60 >= self.yborder[1]]):
                return "xy"
            return "x" if futpos[0]+60 >= self.xborders[1] or futpos[0] <= self.xborders[0] else "y"
        return ""

    def update(self,dt):
        self.AirForse = [0.5 * self.coeff * self.AirRo * self.Sy * self.V[0] ** 2 * (-1 if self.V[0] > 0 else 1),
                         0.5 * self.coeff * self.AirRo * self.Sx * self.V[1] ** 2 * (-1 if self.V[1] > 0 else 1)]
        self.GRNDFriction = [abs(self.GRNDFriction[0]) * (-1 if self.V[0] > 0 else 1),
                             abs(self.GRNDFriction[1]) * (-1 if self.V[1] > 0 else 1)]
        dsx = self.V[0]*dt*self.ScaleMx
        dsy = self.V[1]*dt*self.ScaleMy
        self.V[1] = ((self.CurrForce[1] + self.AirForse[1]+ self.GRNDFriction[1]) / self.M) * dt + self.V[1]
        self.V[0] = ((self.CurrForce[0] + self.AirForse[0]+ self.GRNDFriction[0]) / self.M) * dt + self.V[0]
        self.gameObject.pos[0] += dsx
        self.gameObject.pos[1] += dsy
        if self.TouchBorders([self.gameObject.pos[0],self.gameObject.pos[1]]):
            self.TouchingBorders = self.TouchBorders(self.gameObject.pos)
            if "x" in self.TouchingBorders:
                self.V[0]*=-1
                self.gameObject.pos[0] -= dsx
            if "y" in self.TouchingBorders:
                self.V[1]*=-1
                self.gameObject.pos[1] -= dsy
        else:
            self.TouchingBorders = ""

        if self.GroundCollide(self.gameObject.pos):
            self.SetOnGround(True)
            self.gameObject.pos[0] -= dsx
            self.gameObject.pos[1] -= dsy
            self.V = [0,0]

    def SetOnGround(self, ground ):
        self.onGround = ground
        if self.onGround:
            self.GRNDFriction = [self.M * self.G * self.KFriction, self.M * self.G*0.1]
        else:
            self.GRNDFriction = [0, 0]

    def CheckTail(self):
        try:
            check = [self.groundCollide.mask.get_at((int(self.gameObject.pos[0]+20), int(self.gameObject.pos[1] + 50))),
                 self.groundCollide.mask.get_at((int(self.gameObject.pos[0]+30), int(self.gameObject.pos[1] + 50))),
                 self.groundCollide.mask.get_at((int(self.gameObject.pos[0]+40), int(self.gameObject.pos[1] + 50)))]
        except:
            return [0,0,0]
        return check

    def GroundCollide(self,futpos):
        offset_x, offset_y = futpos
        if (self.groundCollide.mask.overlap(self.gameObject.GetAbility("spriteRenderer").mask, (int(offset_x), int(offset_y))) != None):
            return True
        return False

    def WalkCheck(self,futpos):
        if self.GroundCollide(futpos) or self.TouchBorders([futpos[0],futpos[1]]): return True
        return False

    def AddForce(self,forse,dt,grnNeed = False):
        if not grnNeed or (self.onGround and grnNeed):
            self.V[0] += (forse[0] /self.M) * dt
            self.V[1] += (forse[1] / self.M) * dt

    def Walk(self,dt,right = True):
        tryWalkPos = [self.gameObject.pos[0] +self.walkSpeed*self.ScaleMx*dt if right else self.gameObject.pos[0]-self.walkSpeed*self.ScaleMx*dt,self.gameObject.pos[1]]
        if self.WalkCheck(tryWalkPos): tryWalkPos[1]-=1
        if self.WalkCheck(tryWalkPos): tryWalkPos[1]-=1
        if self.WalkCheck(tryWalkPos): tryWalkPos[1]-=1
        if self.WalkCheck(tryWalkPos): return None
        self.gameObject.pos = tryWalkPos

    def Jump(self, dt, dir="up"):
        xForse = 0
        if dir=="right":
            xForse = 450
        elif dir=="left":
            xForse = -450
        self.AddForce([xForse, -700], 1 / 30, True)
        self.SetOnGround(False)