class Football_Association:
    __name__ = None
    __leagues__ = []
    __id__ = None

    def __init__(self, name, id=None):
        self.__name__ = name
        self.__id__ = id
        
    def get_id(self):
        return self.__id__

    def add_leagues(self, leagues):
        for league in leagues:
            self.__leagues__.append(league)

    def get_leagues(self):
        return self.__leagues__
   
    def change_name(self, new_name):
        self.__name__ = new_name
 
    def get_name(self):
        return self.__name__
