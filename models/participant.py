class Participant:
    __id__ = None
    __league__ = None
    __team__ = None
    
    
    def __init__(self, league, team, id=None):
        self.__league__ = league
        self.__team__ = team
        self.__id__ = id
        
    def get_league(self):
        return self.__league__
    
    def set_league(self, league):
        self.__league__ = league
    
    def get_team(self):
        return self.__team__

    def set_team(self, team):
        self.__team__ = team

    def get_id(self):
        return self.__id__

    def set_id(self, id):
        self.__id__ = id
