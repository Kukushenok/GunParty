import objects.engine.GameCFG
import objects.level.Levels
import objects.level.Resources
import objects.engine.ObjectManager
import objects.engine.Factory
import os

#Синглтон для доступа к общим ресурсам игры
class ResourceManager(object):

    #Экземпляр класса, инкапсулирующий данные о настройках
    __gameCFGinstance = None

    #Экземпляр класса, инкапсулирующий данные об уровнях
    __levelsInstance = None

    #Экземпляр класса, инкапсулирующий ресурсы (картинки) игры
    __resourcesInstance = None

    #Экземпляр класса, инкапсулирующий звуковые ресурсы игры
    __SFXResourcesInstance = None

    #Экземпляр класса, инкапсулирующего дерево объектов игры
    __objectManagerInstance = None

    #Экземпляр класса фабрики объектов игры
    __factoryInstance = None

    playground = None

    @staticmethod
    def instGameCFG():
        if ResourceManager.__gameCFGinstance == None:
            ResourceManager.__gameCFGinstance = objects.engine.GameCFG.GameCFG()
        return ResourceManager.__gameCFGinstance

    @staticmethod
    def intsLevels():
        if ResourceManager.__levelsInstance == None:
            ResourceManager.__levelsInstance = objects.level.Levels.Levels()
        return ResourceManager.__levelsInstance

    @staticmethod
    def instResources():
        if ResourceManager.__resourcesInstance == None:
            ResourceManager.__resourcesInstance = objects.level.Resources.Resources(os.path.join(os.getcwd(), "resources", "images")).resources
        return ResourceManager.__resourcesInstance

    @staticmethod
    def instSFXResources():
        if ResourceManager.__SFXResourcesInstance == None:
            ResourceManager.__SFXResourcesInstance = objects.level.Resources.Resources(os.path.join(os.getcwd(), "resources", "sfx")).resources
        return ResourceManager.__SFXResourcesInstance

    @staticmethod
    def instObjectManager():
        if ResourceManager.__objectManagerInstance == None:
            ResourceManager.__objectManagerInstance = objects.engine.ObjectManager.ObjectManager()
        return ResourceManager.__objectManagerInstance

    @staticmethod
    def instFactory():
        if ResourceManager.__factoryInstance == None:
            ResourceManager.__factoryInstance = objects.engine.Factory.Factory()
        return ResourceManager.__factoryInstance
