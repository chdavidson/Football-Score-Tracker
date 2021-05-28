class Team:
    __name__ = None
    __year_founded__ = None
    __players__ = []
    __stadium__ = []
    __id__ = None

    def __init__(self, name, year_founded, stadium, players=None, id=None):
        self.name = name
        self.__year_founded__ = year_founded
        self.__stadium__ = stadium
        self.__id__ = id
        for player in players:
            self.__players__.append(player)

    def get_players(self):
        return self.__players__
    
    def add_players(self, players):
        for player in players:
            self.__players__.append(player)