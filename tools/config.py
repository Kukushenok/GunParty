import configparser
class Config():
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read('config.ini')
    def get(self,item):
        return self.config["SCREENSETTINGS"][item]
