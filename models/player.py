from enum import Enum, auto


class Position(Enum):
    GK = auto()
    DEF = auto()
    MID = auto()
    FWD = auto()


class Player:
    __surname__ = None
    __first_name__ = None
    __squad_number__ = None
    __position__ = None
    __goals_scored__ = None
    __assists__ = None
    __own_goals__ = None
    __y_cards__ = None
    __r_cards__ = None
    __clean_sheets__ = None

    def set_surname(self, surname):
        self.__surname__ = surname

    def get_surname(self):
        return self.__surname__

    def set_firstname(self, first_name):
        self.__first_name__ = first_name

    def get_firstname(self):
        return self.__first_name__

    def set_squad_numer(self, squad_number):
        self.__squad_number__ = squad_number

    def get_squad_number(self):
        return self.__squad_number__

    def set_postion(self, position):
        try:
            self.__position__ = Position(position)
        except Exception as e:
            print(e)

    def get_position(self):
        return self.__position__

    def increment_goals(self, goals_scored):
        self.__goals_scored__ += goals_scored

    def get_goals_scored(self):
        return self.__goals_scored__

    def increment_assists(self, assists):
        self.__assists__ += assists

    def get_assists(self):
        return self.__assists__

    def increment_own_goals(self, own_goals_scored):
        self.__own_goals__ += own_goals_scored

    def get_own_goals(self):
        return self.__own_goals__

    def increment_yellow_cards(self, yellow_cards):
        self.__y_cards__ += yellow_cards

    def get_yellow_cards(self):
        return self.__y_cards__

    def increment_red_cards(self):
        self.__r_cards__ += 1

    def get_red_cards(self):
        return self.__r_cards__

    def increment_clean_sheets(self):
        self.__clean_sheets__ += 1

    def get_clean_sheets(self):
        return self.__clean_sheets__


# player_1 = Player()
# player_1.set_postion(3)
# print(player_1.get_position())