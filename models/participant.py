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
    
    def get_team(self):
        return self.__team__
    
    def get_id(self):
        return self.__id__