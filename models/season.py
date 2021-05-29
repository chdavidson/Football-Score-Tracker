class Season:
    __id__ = None
    __year__ = None
    __league__ = None
    
    def __init__(self, year, league, id=None):
        self.__year__ = year
        self.__league__ = league
        self.__id__ = id

    def get_id(self):
        return self.__id__

    def set_id(self, id):
        self.__id__ = id

    def get_league(self):
        return self.__league__

    def set_league(self, league):
        self.__league__ = league

    def set_year(self, year):
        self.__year__ = year

    def get_year(self):
        return self.__year__
