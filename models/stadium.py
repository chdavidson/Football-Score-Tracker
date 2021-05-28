class Stadium:

    __name__ = None
    __location__ = None
    __capacity__ = None
    __teams__ = []
    __id__ = None

    def __init__(self, name, location, capacity, teams, id):
        self.__name__ = name
        self.__location__ = location
        self.__capacity__ = capacity
        self.__id__ = id
        for team in teams:
            self.__teams__.append(team)
