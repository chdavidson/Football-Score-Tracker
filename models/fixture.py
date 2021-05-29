class Fixture():
    __home_team__ = None
    __away_team__ = None
    __id__ = None
    __season__ = None

    def __init__(self, home_team, away_team, season, id=None):
        self.__home_team__ = home_team
        self.__away_team__ = away_team
        self.__id__ = id
        self.__season__ = season

    def get_id(self):
        return self.__id__
    
    def set_id(self, id):
        self.__id__ = id
    
    def set_season(self, season):
        self.__season__ = season
    
    def get_season(self):
        return self.__season__

    def get_fixture(self):
        return [self.__home_team__, self.__away_team__]
    
    def set_fixture(self, home_team, away_team):
        self.__home_team__ = home_team
        self.__away_team__ = away_team
