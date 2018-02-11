import objects.engine.GameObject as gameObject
import objects.abilities.SpriteRenderer as spriteRenderer
import objects.abilities.StateMashine as stateMashine
import objects.abilities.State as state
import objects.abilities.PlayerControl as pControl
import objects.abilities.Physics as physics
import objects.gui.GUI as gui
import objects.gui.Slot as slot
from objects.engine.Global import GAMECFG
from objects.engine.Global import OBJECTMANAGER
import pygame
class Factory:
    def __init__(self,resources,group):
        self.resources = resources
        self.group = group

    def Get(self,type,x,y,*args):
        cobject = None
        if type == "player":
            cobject = gameObject.GameObject()
            st = stateMashine.StateMashine(cobject)
            s =state.State(cobject)
            s.AddSurface("u",self.resources["wwalku.png"])
            s.AddSurface("d", self.resources["wwalkd.png"])
            s.AddSurface("n", self.resources["wwalk.png"])
            st.AddState("movel", s)

            s =state.State(cobject)
            s.AddSurface("u",pygame.transform.flip(self.resources["wwalku.png"], True, False))
            s.AddSurface("d", pygame.transform.flip(self.resources["wwalkd.png"], True, False))
            s.AddSurface("n", pygame.transform.flip(self.resources["wwalk.png"], True, False))
            st.AddState("mover", s)

            s = state.State(cobject)
            s.AddSurface("u",self.resources["wblink1u.png"])
            s.AddSurface("d", self.resources["wblink1d.png"])
            s.AddSurface("n", self.resources["wblink1.png"])
            s.SetCurrentOption("n",True)
            st.AddState("blinkl",s)

            s =state.State(cobject)
            s.AddSurface("u",pygame.transform.flip(self.resources["wblink1u.png"], True, False))
            s.AddSurface("d", pygame.transform.flip(self.resources["wblink1d.png"], True, False))
            s.AddSurface("n", pygame.transform.flip(self.resources["wblink1.png"], True, False))

            st.AddState("blinkr", s)

            s = state.State(cobject)
            s.AddSurface("u",self.resources["wjumpu.png"])
            s.AddSurface("d", self.resources["wjumpd.png"])
            s.AddSurface("n", self.resources["wjump.png"])
            s.SetCurrentOption("n", True)
            s.loop = False
            st.AddState("jumpl",s)

            s =state.State(cobject)
            s.AddSurface("u",pygame.transform.flip(self.resources["wjumpu.png"], True, False))
            s.AddSurface("d", pygame.transform.flip(self.resources["wjumpd.png"], True, False))
            s.AddSurface("n", pygame.transform.flip(self.resources["wjump.png"], True, False))
            s.loop = False
            st.AddState("jumpr", s)
            s = state.State(cobject)
            s.AddSurface("n", self.resources["wflylnk.png"])
            s.AddSurface("u", self.resources["wflylnk.png"])
            s.AddSurface("d", self.resources["wflylnk.png"])
            s.SetCurrentOption("n", True)
            s.speed = 10
            s.loop = False
            st.AddState("flyl",s)

            s =state.State(cobject)
            s.AddSurface("n", pygame.transform.flip(self.resources["wflylnk.png"], True, False))
            s.AddSurface("u", pygame.transform.flip(self.resources["wflylnk.png"], True, False))
            s.AddSurface("d", pygame.transform.flip(self.resources["wflylnk.png"], True, False))
            s.speed = 10
            s.loop = False
            st.AddState("flyr", s)

            st.SetState("blinkl")
            cobject.AddAbility("stateMashine",st)

            cobject.AddAbility("spriteRenderer", spriteRenderer.SpriteRenderer(self.group,cobject))
            sp = cobject.GetAbility("spriteRenderer")
            sp.selectImage(0)
            sp.rect = sp.image.get_rect()
            cobject.pos = [x,y]
            cobject.AddAbility("playerControl",pControl.PlayerControl(cobject,args[0]))
            ph = physics.Physics(cobject)
            ph.SetGravity(True)
            cobject.AddAbility("physics",ph)
        elif type == "gui":
            cobject = gui.GUI(args[0])
            for i in range(3):
                slt = slot.Slot(cobject)
                slt.pos[0]+=i*(self.resources["guislot.png"].get_rect()[3]*GAMECFG.GetScreenCoeff()[0]+3)
        OBJECTMANAGER.AddObject(cobject)
        return cobject