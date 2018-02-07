import objects.GameObject as gameObject
import objects.SpriteRenderer as spriteRenderer
import objects.StateMashine as stateMashine
import objects.State as state
import objects.PlayerControl as pControl
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
            s.AddSurface("u",self.resources["wjumpu.png"])
            s.AddSurface("d", self.resources["wjumpd.png"])
            s.AddSurface("n", self.resources["wjump.png"])
            s.SetCurrentState("n")
            st.AddState("accuse",s)
            st.SetState("accuse")
            cobject.AddAbility("stateMashine",st)

            cobject.AddAbility("spriteRenderer", spriteRenderer.SpriteRenderer(self.group,cobject))
            sp = cobject.GetAbility("spriteRenderer")
            sp.selectImage(0)
            sp.rect = sp.image.get_rect()
            sp.rect.x = x
            sp.rect.y = y
            cobject.AddAbility("playerControl",pControl.PlayerControl(cobject,args[0]))
        return cobject