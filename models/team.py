class Team:
    __name__ = None
    __year_founded__ = None
    __players__ = []
    __stadium__ = []
    __id__ = None

    def __init__(self, name, year_founded, stadium, id=None):
        self.__name__ = name
        self.__year_founded__ = year_founded
        self.__stadium__ = stadium
        self.__id__ = id
        # for player in players:
        #     self.__players__.append(player)

    # def get_players(self):
    #     return self.__players__

    # def add_players(self, players):
    #     for player in players:
    #         self.__players__.append(player)

    def get_name(self):
        return self.__name__

    def get_founding_year(self):
        return self.__year_founded__

    def set_id(self, id):
        self.__id__ = id

    def get_id(self):
        return self.__id__

    def get_stadium(self):
        return self.__stadium__
