import pygame
import ResourceManager
class GameObject:
    def __init__(self,*args):
        self.abilities = {}
        self.pos = [0,0]
        self.screen = None
        self.gui = None
        for e in args:
            self.AddAbility(e[0],e[1])
    def AddAbility(self,abilityName,ability):
        self.abilities[abilityName] = ability
    def GetAbility(self,name):
        return self.abilities[name]
    def get_event(self,event):
        i = 0
        while i < len(list(self.abilities.values())):
            ability = list(self.abilities.values())[i]
            get_event = getattr(ability,"get_event",None)
            if callable(get_event):
                ability.get_event(event)
            i+=1




        # for element in self.abilities.values():
        #     get_event = getattr(element, "get_event", None)
        #     if callable(get_event):
        #         element.get_event(event)
    def renderGUI(self,screen):
        if not self.gui: return None
        self.gui.render(screen)

    def update(self,dt):
        i = 0
        while i < len(list(self.abilities.values())):
            ability = list(self.abilities.values())[i]
            update = getattr(ability,"update",None)
            if callable(update):
                ability.update(dt)
            i+=1

        # for element in self.abilities.values():
        #     update = getattr(element, "update", None)
        #     if callable(update):
        #         element.update(dt)
    def destroy(self):
        self.abilities = {}
        self.pos = []

    def kill(self):
        ResourceManager.ResourceManager.instObjectManager().deleteObject(self)
        try:
            spriteRenderer=self.GetAbility("spriteRenderer")
            spriteRenderer.kill()
        except KeyError: pass
        self.destroy()