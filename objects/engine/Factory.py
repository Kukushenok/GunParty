import pygame

import ResourceManager
import objects.abilities.Physics
import objects.abilities.PlayerControl
import objects.abilities.SpriteRenderer
import objects.abilities.State
import objects.abilities.StateMashine
import objects.abilities.WeaponControl
import objects.engine.GameObject
import objects.gui.ForceIndicator
import objects.gui.GUI
import objects.gui.Slot
import objects.abilities.Audible
import objects.abilities.Damagable
import objects.gui.PlayerInfo

class Factory:

    def __init__(self):
        self.resources = None
        self.group = None

    def initFactory(self, group ):
        self.resources = ResourceManager.ResourceManager.instResources()
        self.group = group
    #Метод для получения обьектов нужного типа
    def get(self,type,x,y,*args):
        cobject = None
        if type == "player":
            cobject = self.createPlayer(x, y, *args)
        elif type == "gui":
            cobject = self.createGUI(x, y, *args)
        elif type == "missile":
            cobject = self.createBazMissile(x, y, *args)
        elif type =="grenade":
            cobject = self.createGrenade(x, y, *args)
        elif type == "bullet":
            cobject = self.createBullet(x, y, *args)
        ResourceManager.ResourceManager.instObjectManager().AddObject(cobject)
        return cobject

    #Создание объекта игрока
    def createPlayer(self, x, y, *args):

        cobject = objects.engine.GameObject.GameObject()
        cobject.AddAbility("damagable",objects.abilities.Damagable.Damagable(cobject))
        #cobject.GetAbility("damagable").lifetime = 5
        st = objects.abilities.StateMashine.StateMashine(cobject)
        audible = objects.abilities.Audible.Audible(cobject)
        st.AddSubscriber(audible)
        cobject.AddAbility("audible",audible)
        s = objects.abilities.State.State(cobject)
        s.AddSurface("u", self.resources["wwalku.png"])
        s.AddSurface("d", self.resources["wwalkd.png"])
        s.AddSurface("n", self.resources["wwalk.png"])
        s.sound = ResourceManager.ResourceManager.instSFXResources()["walk.wav"]
        st.AddState("movel", s)

        s = objects.abilities.State.State(cobject)
        s.AddSurface("u", pygame.transform.flip(self.resources["wwalku.png"], True, False))
        s.AddSurface("d", pygame.transform.flip(self.resources["wwalkd.png"], True, False))
        s.AddSurface("n", pygame.transform.flip(self.resources["wwalk.png"], True, False))
        s.sound = ResourceManager.ResourceManager.instSFXResources()["walk.wav"]
        st.AddState("mover", s)

        s = objects.abilities.State.State(cobject)
        s.AddSurface("u", self.resources["wblink1u.png"])
        s.AddSurface("d", self.resources["wblink1d.png"])
        s.AddSurface("n", self.resources["wblink1.png"])
        s.SetCurrentOption("n")
        st.AddState("blinkl", s)

        s = objects.abilities.State.State(cobject)
        s.AddSurface("u", pygame.transform.flip(self.resources["wblink1u.png"], True, False))
        s.AddSurface("d", pygame.transform.flip(self.resources["wblink1d.png"], True, False))
        s.AddSurface("n", pygame.transform.flip(self.resources["wblink1.png"], True, False))

        st.AddState("blinkr", s)

        # Прыжок
        s = objects.abilities.State.State(cobject)
        s.AddSurface("n", self.resources["wflylnk.png"])
        s.AddSurface("u", self.resources["wflylnk.png"])
        s.AddSurface("d", self.resources["wflylnk.png"])
        s.SetCurrentOption("n")
        s.speed = 10
        s.loop = False
        s.sound = ResourceManager.ResourceManager.instSFXResources()["jump.wav"]
        st.AddState("flyl", s)

        s = objects.abilities.State.State(cobject)
        s.AddSurface("n", pygame.transform.flip(self.resources["wflylnk.png"], True, False))
        s.AddSurface("u", pygame.transform.flip(self.resources["wflylnk.png"], True, False))
        s.AddSurface("d", pygame.transform.flip(self.resources["wflylnk.png"], True, False))
        s.speed = 10
        s.loop = False
        s.sound = ResourceManager.ResourceManager.instSFXResources()["jump.wav"]
        st.AddState("flyr", s)

        # Приседание
        s = objects.abilities.State.State(cobject)
        s.AddSurface("u", self.resources["wjumpu.png"])
        s.AddSurface("d", self.resources["wjumpd.png"])
        s.AddSurface("n", self.resources["wjump.png"])
        s.SetCurrentOption("n")
        s.loop = False
        st.AddState("jumpl", s)

        s = objects.abilities.State.State(cobject)
        s.AddSurface("u", pygame.transform.flip(self.resources["wjumpu.png"], True, False))
        s.AddSurface("d", pygame.transform.flip(self.resources["wjumpd.png"], True, False))
        s.AddSurface("n", pygame.transform.flip(self.resources["wjump.png"], True, False))
        s.loop = False
        st.AddState("jumpr", s)

        # Оружия.Базука
        s = objects.abilities.State.State(cobject)
        s.AddSurface("n", self.resources["wbazbak.png"])
        s.AddSurface("u", self.resources["wbazbaku.png"])
        s.AddSurface("d", self.resources["wbazbakd.png"])
        s.SetCurrentOption("n")
        s.speed = 20
        s.loop = False
        st.AddState("bazbakl", s)

        s = objects.abilities.State.State(cobject)
        s.AddSurface("n", pygame.transform.flip(self.resources["wbazbak.png"], True, False))
        s.AddSurface("u", pygame.transform.flip(self.resources["wbazbaku.png"], True, False))
        s.AddSurface("d", pygame.transform.flip(self.resources["wbazbakd.png"], True, False))
        s.speed = 20
        s.loop = False
        st.AddState("bazbakr", s)

        s = objects.abilities.State.State(cobject)
        s.AddSurface("n", self.resources["wbazlnk.png"])
        s.AddSurface("u", self.resources["wbazlnku.png"])
        s.AddSurface("d", self.resources["wbazlnkd.png"])
        s.SetCurrentOption("n")
        s.speed = 20
        s.loop = False
        st.AddState("bazlnkl", s)

        s = objects.abilities.State.State(cobject)
        s.AddSurface("n", pygame.transform.flip(self.resources["wbazlnk.png"], True, False))
        s.AddSurface("u", pygame.transform.flip(self.resources["wbazlnku.png"], True, False))
        s.AddSurface("d", pygame.transform.flip(self.resources["wbazlnkd.png"], True, False))
        s.speed = 20
        s.loop = False
        st.AddState("bazlnkr", s)

        s = objects.abilities.State.State(cobject)
        s.AddSurface("n", self.resources["wbaz.png"])
        s.AddSurface("u", self.resources["wbazu.png"])
        s.AddSurface("d", self.resources["wbazd.png"])
        s.SetCurrentOption("n")
        s.speed = 20
        s.loop = False
        s.ManualControl = True
        st.AddState("bazl", s)

        s = objects.abilities.State.State(cobject)
        s.AddSurface("n", pygame.transform.flip(self.resources["wbaz.png"], True, False))
        s.AddSurface("u", pygame.transform.flip(self.resources["wbazu.png"], True, False))
        s.AddSurface("d", pygame.transform.flip(self.resources["wbazd.png"], True, False))
        s.speed = 20
        s.loop = False
        s.ManualControl = True
        st.AddState("bazr", s)
        # Оружия.Граната
        s = objects.abilities.State.State(cobject)
        s.AddSurface("n", self.resources["wgrnbak.png"])
        s.AddSurface("u", self.resources["wgrnbaku.png"])
        s.AddSurface("d", self.resources["wgrnbakd.png"])
        s.SetCurrentOption("n")
        s.speed = 20
        s.loop = False
        st.AddState("grnbakl", s)

        s = objects.abilities.State.State(cobject)
        s.AddSurface("n", pygame.transform.flip(self.resources["wgrnbak.png"], True, False))
        s.AddSurface("u", pygame.transform.flip(self.resources["wgrnbaku.png"], True, False))
        s.AddSurface("d", pygame.transform.flip(self.resources["wgrnbakd.png"], True, False))
        s.speed = 20
        s.loop = False
        st.AddState("grnbakr", s)

        s = objects.abilities.State.State(cobject)
        s.AddSurface("n", self.resources["wgrnlnk.png"])
        s.AddSurface("u", self.resources["wgrnlnku.png"])
        s.AddSurface("d", self.resources["wgrnlnkd.png"])
        s.SetCurrentOption("n")
        s.speed = 20
        s.loop = False
        st.AddState("grnlnkl", s)

        s = objects.abilities.State.State(cobject)
        s.AddSurface("n", pygame.transform.flip(self.resources["wgrnlnk.png"], True, False))
        s.AddSurface("u", pygame.transform.flip(self.resources["wgrnlnku.png"], True, False))
        s.AddSurface("d", pygame.transform.flip(self.resources["wgrnlnkd.png"], True, False))
        s.speed = 20
        s.loop = False
        st.AddState("grnlnkr", s)

        s = objects.abilities.State.State(cobject)
        s.AddSurface("n", self.resources["wthrgrn.png"])
        s.AddSurface("u", self.resources["wthrgrnu.png"])
        s.AddSurface("d", self.resources["wthrgrnd.png"])
        s.SetCurrentOption("n")
        s.speed = 20
        s.loop = False
        s.ManualControl = True
        st.AddState("grnl", s)

        s = objects.abilities.State.State(cobject)
        s.AddSurface("n", pygame.transform.flip(self.resources["wthrgrn.png"], True, False))
        s.AddSurface("u", pygame.transform.flip(self.resources["wthrgrnu.png"], True, False))
        s.AddSurface("d", pygame.transform.flip(self.resources["wthrgrnd.png"], True, False))
        s.speed = 20
        s.loop = False
        s.ManualControl = True
        st.AddState("grnr", s)

        # Оружия.Ружьё
        s = objects.abilities.State.State(cobject)
        s.AddSurface("n", self.resources["wshgbak.png"])
        s.AddSurface("u", self.resources["wshgbaku.png"])
        s.AddSurface("d", self.resources["wshgbakd.png"])
        s.SetCurrentOption("n")
        s.speed = 20
        s.loop = False
        st.AddState("shgbakl", s)

        s = objects.abilities.State.State(cobject)
        s.AddSurface("n", pygame.transform.flip(self.resources["wshgbak.png"], True, False))
        s.AddSurface("u", pygame.transform.flip(self.resources["wshgbaku.png"], True, False))
        s.AddSurface("d", pygame.transform.flip(self.resources["wshgbakd.png"], True, False))
        s.speed = 20
        s.loop = False
        st.AddState("shgbakr", s)

        s = objects.abilities.State.State(cobject)
        s.AddSurface("n", self.resources["wshglnk.png"])
        s.AddSurface("u", self.resources["wshglnku.png"])
        s.AddSurface("d", self.resources["wshglnkd.png"])
        s.SetCurrentOption("n")
        s.speed = 20
        s.loop = False
        st.AddState("shglnkl", s)

        s = objects.abilities.State.State(cobject)
        s.AddSurface("n", pygame.transform.flip(self.resources["wshglnk.png"], True, False))
        s.AddSurface("u", pygame.transform.flip(self.resources["wshglnku.png"], True, False))
        s.AddSurface("d", pygame.transform.flip(self.resources["wshglnkd.png"], True, False))
        s.speed = 20
        s.loop = False
        st.AddState("shglnkr", s)

        s = objects.abilities.State.State(cobject)
        s.AddSurface("n", self.resources["wshotg.png"])
        s.AddSurface("u", self.resources["wshotgu.png"])
        s.AddSurface("d", self.resources["wshotgd.png"])
        s.SetCurrentOption("n")
        s.speed = 20
        s.loop = False
        s.ManualControl = True
        st.AddState("shgl", s)

        s = objects.abilities.State.State(cobject)
        s.AddSurface("n", pygame.transform.flip(self.resources["wshotg.png"], True, False))
        s.AddSurface("u", pygame.transform.flip(self.resources["wshotgu.png"], True, False))
        s.AddSurface("d", pygame.transform.flip(self.resources["wshotgd.png"], True, False))
        s.speed = 20
        s.loop = False
        s.ManualControl = True
        st.AddState("shgr", s)

        s = objects.abilities.State.State(cobject)
        s.AddSurface("n", self.resources["wshotf.png"])
        s.AddSurface("u", self.resources["wshotfu.png"])
        s.AddSurface("d", self.resources["wshotfd.png"])
        s.SetCurrentOption("n")
        s.speed = 20
        s.loop = False
        s.ManualControl = True
        st.AddState("shgfl", s)

        s = objects.abilities.State.State(cobject)
        s.AddSurface("n", pygame.transform.flip(self.resources["wshotf.png"], True, False))
        s.AddSurface("u", pygame.transform.flip(self.resources["wshotfu.png"], True, False))
        s.AddSurface("d", pygame.transform.flip(self.resources["wshotfd.png"], True, False))
        s.speed = 20
        s.loop = False
        s.ManualControl = True
        st.AddState("shgfr", s)
        # Оружия.Стоп
        st.SetState("blinkl")
        cobject.AddAbility("stateMashine", st)

        cobject.AddAbility("spriteRenderer", objects.abilities.SpriteRenderer.SpriteRenderer(self.group, cobject))
        sp = cobject.GetAbility("spriteRenderer")
        sp.selectImage(0)
        sp.rect = sp.image.get_rect()
        cobject.pos = [x, y]
        cobject.gui = self.get("gui", args[1][0], args[1][1], args[0])
        cobject.gui.AddObject(objects.gui.PlayerInfo.PlayerInfo(cobject))
        cobject.AddAbility("playerControl", objects.abilities.PlayerControl.PlayerControl(cobject, args[0]))
        ph = objects.abilities.Physics.Physics(cobject)
        ph.elasticity=0.3
        ph.SetGravity(True)
        cobject.AddAbility("physics", ph)
        return cobject


    def createGUI(self, x, y, *args ):
        cobject = objects.gui.GUI.GUI(args[0])
        weapons = ["bazookaIcon.png", "grenadeIcon.png", "shotgunIcon.png"]
        for i in range(len(weapons)):
            slt = objects.gui.Slot.Slot(cobject, weapons[i])
            slt.pos[0] += i * (self.resources["guislot.png"].get_rect()[3] * ResourceManager.ResourceManager.instGameCFG().GetScreenCoeff()[0] + 3)
        cobject.AddObject(objects.gui.ForceIndicator.ForceIndicator(
            pygame.Rect(x, 1020 * ResourceManager.ResourceManager.instGameCFG().GetScreenCoeff()[1], 600 *
                        ResourceManager.ResourceManager.instGameCFG().GetScreenCoeff()[0],
                        60 * ResourceManager.ResourceManager.instGameCFG().GetScreenCoeff()[1])))
        return cobject

    def createBazMissile(self, x, y, *args):
        cobject = objects.engine.GameObject.GameObject()
        st = objects.abilities.StateMashine.StateMashine(cobject)
        s = objects.abilities.State.State(cobject)
        s.AddSurface("n", self.resources["missile.png"])
        s.AddSurface("u", self.resources["missile.png"])
        s.AddSurface("d", self.resources["missile.png"])
        s.loop = False
        s.ManualControl = True
        st.AddState("normal", s)
        st.SetState("normal")
        cobject.AddAbility("stateMashine", st)
        missPhys = objects.abilities.Physics.Physics(cobject)
        missPhys.M = 2
        missPhys.coeff = 0.2
        missPhys.Sx = 0.2
        missPhys.Sy = 0.2
        missPhys.SetGravity(True)
        wc = objects.abilities.WeaponControl.WeaponControl(cobject)
        cobject.AddAbility("weaponControl", wc)
        missPhys.addSubscriber(wc)
        cobject.AddAbility("physics", missPhys)
        cobject.AddAbility("spriteRenderer", objects.abilities.SpriteRenderer.SpriteRenderer(self.group, cobject))
        sp = cobject.GetAbility("spriteRenderer")
        sp.selectImage(0)
        sp.rect = sp.image.get_rect()
        cobject.pos = [x, y]
        return cobject


    def createGrenade(self, x, y, *args):
        cobject = objects.engine.GameObject.GameObject()
        st = objects.abilities.StateMashine.StateMashine(cobject)
        s = objects.abilities.State.State(cobject)
        s.AddSurface("n", self.resources["grenade.png"])
        s.AddSurface("u", self.resources["grenade.png"])
        s.AddSurface("d", self.resources["grenade.png"])
        s.loop = True
        s.ManualControl = False
        st.AddState("normal", s)
        st.SetState("normal")
        cobject.AddAbility("stateMashine", st)
        grenagePhys = objects.abilities.Physics.Physics(cobject)
        grenagePhys.M = 1
        grenagePhys.coeff = 0.1
        grenagePhys.Sx = 0.1
        grenagePhys.Sy = 0.1
        grenagePhys.SetGravity(True)
        grenagePhys.elasticity=0.5
        wc = objects.abilities.WeaponControl.WeaponControl(cobject)
        wc.killOnGround = False
        cobject.AddAbility("weaponControl", wc)
        grenagePhys.addSubscriber(wc)
        cobject.AddAbility("physics", grenagePhys)
        cobject.AddAbility("spriteRenderer", objects.abilities.SpriteRenderer.SpriteRenderer(self.group, cobject))
        sp = cobject.GetAbility("spriteRenderer")
        sp.selectImage(0)
        sp.rect = sp.image.get_rect()
        cobject.pos = [x, y]
        damagable = objects.abilities.Damagable.Damagable(cobject)
        damagable.lifetime = 6
        cobject.AddAbility("damagable",damagable)
        cobject.gui = objects.gui.GUI.GUI(None)
        cobject.gui.AddObject(objects.gui.PlayerInfo.PlayerInfo(cobject))
        return cobject

    def createBullet(self, x, y, *args):
        cobject = objects.engine.GameObject.GameObject()
        st = objects.abilities.StateMashine.StateMashine(cobject)
        s = objects.abilities.State.State(cobject)
        s.AddSurface("n", self.resources["bullet.png"])
        s.AddSurface("u", self.resources["bullet.png"])
        s.AddSurface("d", self.resources["bullet.png"])
        s.loop = False
        s.ManualControl = False
        st.AddState("normal", s)
        st.SetState("normal")
        cobject.AddAbility("stateMashine", st)
        bulletPhys = objects.abilities.Physics.Physics(cobject)
        bulletPhys.M = 0.1
        bulletPhys.coeff = 0.01
        bulletPhys.Sx = 0.01
        bulletPhys.Sy = 0.01
        bulletPhys.SetGravity(True)
        bulletPhys.elasticity=0
        wc = objects.abilities.WeaponControl.WeaponControl(cobject)
        wc.takeOFFCoeff = 40
        cobject.AddAbility("weaponControl", wc)
        bulletPhys.addSubscriber(wc)
        cobject.AddAbility("physics", bulletPhys)
        cobject.AddAbility("spriteRenderer", objects.abilities.SpriteRenderer.SpriteRenderer(self.group, cobject))
        sp = cobject.GetAbility("spriteRenderer")
        sp.selectImage(0)
        sp.rect = sp.image.get_rect()
        cobject.pos = [x, y]
        return cobject
