class Stadium:

    __name__ = None
    __location__ = None
    __capacity__ = None
    # __teams__ = []
    __id__ = None

    def __init__(self, name, location, capacity, id=None):
        self.__name__ = name
        self.__location__ = location
        self.__capacity__ = capacity
        self.__id__ = id
        # for team in teams:
        #     self.__teams__.append(team)

    def get_name(self):
        return self.__name__
    
    def get_location(self):
        return self.__location__
    
    def get_capacity(self):
        return self.__capacity__
    
    def set_id(self, id):
        self.__id__ = id
    
    def get_id(self):
        return self.__id__
