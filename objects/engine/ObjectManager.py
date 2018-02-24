import objects.gui.GUI
class ObjectManager:
    def __init__(self):
        self.objects = []
    def AddObject(self,obj):
        self.objects.append(obj)
    def update(self,dt):
        for e in self.objects: e.update(dt)
    def get_event(self,event):
        for e in self.objects: e.get_event(event)
    def renderGUIs(self,screen):
        for e in self.objects:
            if not isinstance(e,objects.gui.GUI.GUI):
                e.renderGUI(screen)
    def deleteObject(self,object):
        for i in range(len(self.objects)):
            if self.objects[i] == object:
                self.objects.pop(i)
                return None
    def clear(self):
        for e in self.objects:
            e.destroy()
        self.objects = []