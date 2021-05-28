class Football_Association:
    __name__ = None
    __leagues__ = []

    def __init__(self, name):
        self.__name__ = name

    def add_leagues(self, leagues):
        for league in leagues:
            self.__leagues__.append(league)

    def get_leagues(self):
        return self.__leagues__
   
    def change_name(self, new_name):
        self.__name__ = new_name
 
    def get_name(self):
        return self.__name__
