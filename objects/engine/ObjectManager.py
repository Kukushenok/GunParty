class ObjectManager:
    def __init__(self):
        self.objects = []
    def AddObject(self,obj):
        self.objects.append(obj)
    def update(self,dt):
        for e in self.objects: e.update(dt)
    def get_event(self,event):
        for e in self.objects: e.get_event(event)
    def clear(self):
        for e in self.objects:
            e.destroy()
        self.objects = []