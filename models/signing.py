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
