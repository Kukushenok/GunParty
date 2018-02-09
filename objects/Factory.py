import objects.GameObject as gameObject
import objects.SpriteRenderer as spriteRenderer
import objects.StateMashine as stateMashine
import objects.State as state
import objects.PlayerControl as pControl
import objects.Physics as physics
from objects.Global import OBJECTMANAGER
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
            s.SetCurrentState("n")
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
            s.SetCurrentState("n")
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
            s.SetCurrentState("n")
            s.spd = 30
            st.AddState("flyl",s)

            s =state.State(cobject)
            s.AddSurface("n", pygame.transform.flip(self.resources["wflylnk.png"], True, False))
            s.spd = 30
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
        OBJECTMANAGER.AddObject(cobject)
        return cobject