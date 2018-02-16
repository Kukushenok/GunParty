import ResourceManager

class Physics:

    def __init__(self,gameO):
        self.gameObject = gameO
        self.groundCollide = ResourceManager.ResourceManager.intsLevels().currlevel.resources["GROUNDMASK"]
        #Масса объекта
        self.M = 5
        #Гравитационная постоянная
        self.G = 9.8
        #Коэффициент обтекаемости
        self.coeff = 0.5
        #Плотность воздуха
        self.AirRo = 1.2
        #Горизонтальная площадь поверхности тела
        self.Sx = 1
        #Вертикальная площадь поверхности тела
        self.Sy = 3
        #Коэффициент упругости 0 - не упругое 1 - полностью упругое
        self.elasticity=0
        #Коэффициент трения
        self.KFriction = 0.95
        self.GRNDFriction = [0,0]
        self.CurrForce = [0,0]
        self.V = [0,0]
        self.ScaleMx = ResourceManager.ResourceManager.instGameCFG().screenwidth / 20
        self.ScaleMy = ResourceManager.ResourceManager.instGameCFG().screenheight / 10
        self.onGround = False
        self.walkSpeed = 1
        self.xborders = [0, ResourceManager.ResourceManager.instGameCFG().screenwidth]
        self.yborder = [0, ResourceManager.ResourceManager.instGameCFG().screenheight]
        self.subscribers = []

    def addSubscriber(self, subscriber):
        self.subscribers.append(subscriber)

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
            self.V = [self.V[0]*self.elasticity*-1,0]
            if self.V[1]>=0:
                self.onGround=True
        #Обновляем состояние наблюдателей
        for e in self.subscribers:
            e.updatePhisics(self.V, self.onGround)

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


    def weaponFire(self, dt, forceVector):
        xForse = 0
        self.AddForce(forceVector, 1 / 30)
        self.SetOnGround(False)