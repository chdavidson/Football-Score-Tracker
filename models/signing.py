from datetime import date


class Signing:

    __id__ = None
    __player__ = None
    __team__ = None
    __date__ = None

    def __init__(self, player, team, signed_on=None, id=None):
        self.__player__ = player
        self.__team__ = team
        self.__date__ = signed_on
        if signed_on is None:
            self.__date__ = date.today()  # YYYY-MM-DD
        self.__id__ = id
        
    def get_player(self):
        return self.__player__

    def get_team(self):
        return self.__team__

    def get_date(self):
        return self.__date__
    
    def get_id(self):
        return self.__id__

    def set_id(self, id):
        self.__id__ = id
