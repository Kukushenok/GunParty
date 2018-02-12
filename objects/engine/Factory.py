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
                                                                                #Оружия.Базука
            s = state.State(cobject)
            s.AddSurface("n", self.resources["wbazbak.png"])
            s.AddSurface("u", self.resources["wbazbaku.png"])
            s.AddSurface("d", self.resources["wbazbakd.png"])
            s.SetCurrentOption("n", True)
            s.speed = 20
            s.loop = False
            st.AddState("bazbakr",s)

            s =state.State(cobject)
            s.AddSurface("n", pygame.transform.flip(self.resources["wbazbak.png"], True, False))
            s.AddSurface("u", pygame.transform.flip(self.resources["wbazbaku.png"], True, False))
            s.AddSurface("d", pygame.transform.flip(self.resources["wbazbakd.png"], True, False))
            s.speed = 20
            s.loop = False
            st.AddState("bazbakl", s)

            s = state.State(cobject)
            s.AddSurface("n", self.resources["wbazlnk.png"])
            s.AddSurface("u", self.resources["wbazlnku.png"])
            s.AddSurface("d", self.resources["wbazlnkd.png"])
            s.SetCurrentOption("n", True)
            s.speed = 20
            s.loop = False
            st.AddState("bazlnkr",s)

            s =state.State(cobject)
            s.AddSurface("n", pygame.transform.flip(self.resources["wbazlnk.png"], True, False))
            s.AddSurface("u", pygame.transform.flip(self.resources["wbazlnku.png"], True, False))
            s.AddSurface("d", pygame.transform.flip(self.resources["wbazlnkd.png"], True, False))
            s.speed = 20
            s.loop = False
            st.AddState("bazlnkl", s)

            s = state.State(cobject)
            s.AddSurface("n", self.resources["wbaz.png"])
            s.AddSurface("u", self.resources["wbazu.png"])
            s.AddSurface("d", self.resources["wbazd.png"])
            s.SetCurrentOption("n", True)
            s.speed = 20
            s.loop = False
            st.AddState("bazr",s)

            s =state.State(cobject)
            s.AddSurface("n", pygame.transform.flip(self.resources["wbaz.png"], True, False))
            s.AddSurface("u", pygame.transform.flip(self.resources["wbazu.png"], True, False))
            s.AddSurface("d", pygame.transform.flip(self.resources["wbazd.png"], True, False))
            s.speed = 20
            s.loop = False
            st.AddState("bazl", s)
                                                                    # Оружия.Граната
            s = state.State(cobject)
            s.AddSurface("n", self.resources["wgrnbak.png"])
            s.AddSurface("u", self.resources["wgrnbaku.png"])
            s.AddSurface("d", self.resources["wgrnbakd.png"])
            s.SetCurrentOption("n", True)
            s.speed = 20
            s.loop = False
            st.AddState("grnbakr", s)

            s = state.State(cobject)
            s.AddSurface("n", pygame.transform.flip(self.resources["wgrnbak.png"], True, False))
            s.AddSurface("u", pygame.transform.flip(self.resources["wgrnbaku.png"], True, False))
            s.AddSurface("d", pygame.transform.flip(self.resources["wgrnbakd.png"], True, False))
            s.speed = 20
            s.loop = False
            st.AddState("grnbakl", s)

            s = state.State(cobject)
            s.AddSurface("n", self.resources["wgrnlnk.png"])
            s.AddSurface("u", self.resources["wgrnlnku.png"])
            s.AddSurface("d", self.resources["wgrnlnkd.png"])
            s.SetCurrentOption("n", True)
            s.speed = 20
            s.loop = False
            st.AddState("grnlnkr", s)

            s = state.State(cobject)
            s.AddSurface("n", pygame.transform.flip(self.resources["wgrnlnk.png"], True, False))
            s.AddSurface("u", pygame.transform.flip(self.resources["wgrnlnku.png"], True, False))
            s.AddSurface("d", pygame.transform.flip(self.resources["wgrnlnkd.png"], True, False))
            s.speed = 20
            s.loop = False
            st.AddState("grnlnkl", s)

            s = state.State(cobject)
            s.AddSurface("n", self.resources["wthrgrn.png"])
            s.AddSurface("u", self.resources["wthrgrnu.png"])
            s.AddSurface("d", self.resources["wthrgrnd.png"])
            s.SetCurrentOption("n", True)
            s.speed = 20
            s.loop = False
            st.AddState("grnr", s)

            s = state.State(cobject)
            s.AddSurface("n", pygame.transform.flip(self.resources["wthrgrn.png"], True, False))
            s.AddSurface("u", pygame.transform.flip(self.resources["wthrgrnu.png"], True, False))
            s.AddSurface("d", pygame.transform.flip(self.resources["wthrgrnd.png"], True, False))
            s.speed = 20
            s.loop = False
            st.AddState("grnl", s)

                                                                    # Оружия.Ружьё
            s = state.State(cobject)
            s.AddSurface("n", self.resources["wshgbak.png"])
            s.AddSurface("u", self.resources["wshgbaku.png"])
            s.AddSurface("d", self.resources["wshgbakd.png"])
            s.SetCurrentOption("n", True)
            s.speed = 20
            s.loop = False
            st.AddState("shgbakr", s)

            s = state.State(cobject)
            s.AddSurface("n", pygame.transform.flip(self.resources["wshgbak.png"], True, False))
            s.AddSurface("u", pygame.transform.flip(self.resources["wshgbaku.png"], True, False))
            s.AddSurface("d", pygame.transform.flip(self.resources["wshgbakd.png"], True, False))
            s.speed = 20
            s.loop = False
            st.AddState("shgbakl", s)

            s = state.State(cobject)
            s.AddSurface("n", self.resources["wshglnk.png"])
            s.AddSurface("u", self.resources["wshglnku.png"])
            s.AddSurface("d", self.resources["wshglnkd.png"])
            s.SetCurrentOption("n", True)
            s.speed = 20
            s.loop = False
            st.AddState("shglnkr", s)

            s = state.State(cobject)
            s.AddSurface("n", pygame.transform.flip(self.resources["wshglnk.png"], True, False))
            s.AddSurface("u", pygame.transform.flip(self.resources["wshglnku.png"], True, False))
            s.AddSurface("d", pygame.transform.flip(self.resources["wshglnkd.png"], True, False))
            s.speed = 20
            s.loop = False
            st.AddState("shglnkl", s)

            s = state.State(cobject)
            s.AddSurface("n", self.resources["wshotg.png"])
            s.AddSurface("u", self.resources["wshotgu.png"])
            s.AddSurface("d", self.resources["wshotgd.png"])
            s.SetCurrentOption("n", True)
            s.speed = 20
            s.loop = False
            st.AddState("shgr", s)

            s = state.State(cobject)
            s.AddSurface("n", pygame.transform.flip(self.resources["wshotg.png"], True, False))
            s.AddSurface("u", pygame.transform.flip(self.resources["wshotgu.png"], True, False))
            s.AddSurface("d", pygame.transform.flip(self.resources["wshotgd.png"], True, False))
            s.speed = 20
            s.loop = False
            st.AddState("shgl", s)

            s = state.State(cobject)
            s.AddSurface("n", self.resources["wshotf.png"])
            s.AddSurface("u", self.resources["wshotfu.png"])
            s.AddSurface("d", self.resources["wshotfd.png"])
            s.SetCurrentOption("n", True)
            s.speed = 20
            s.loop = False
            st.AddState("shgfr", s)

            s = state.State(cobject)
            s.AddSurface("n", pygame.transform.flip(self.resources["wshotf.png"], True, False))
            s.AddSurface("u", pygame.transform.flip(self.resources["wshotfu.png"], True, False))
            s.AddSurface("d", pygame.transform.flip(self.resources["wshotfd.png"], True, False))
            s.speed = 20
            s.loop = False
            st.AddState("shgfl", s)
                                                                                    # Оружия.Стоп
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
            weapons = ["bazookaIcon.png","grenadeIcon.png","shotgunIcon.png"]
            for i in range(len(weapons)):
                slt = slot.Slot(cobject,weapons[i])
                slt.pos[0]+=i*(self.resources["guislot.png"].get_rect()[3]*GAMECFG.GetScreenCoeff()[0]+3)
        OBJECTMANAGER.AddObject(cobject)
        return cobject