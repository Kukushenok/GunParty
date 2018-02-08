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
            st.SetState("blinkl")
            cobject.AddAbility("stateMashine",st)

            cobject.AddAbility("spriteRenderer", spriteRenderer.SpriteRenderer(self.group,cobject))
            sp = cobject.GetAbility("spriteRenderer")
            sp.selectImage(0)
            sp.rect = sp.image.get_rect()
            sp.rect.x = x
            sp.rect.y = y
            cobject.AddAbility("playerControl",pControl.PlayerControl(cobject,args[0]))
        return cobject