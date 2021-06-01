from enum import Enum


class Position(Enum):
    GK = 1
    DEF = 2
    MID = 3
    FWD = 4


class Player:

    def __init__(self, surname, first_name, squad_number, position,
                 goals=0, assists=0, own_goals=0,
                 yellow_cards=0, red_cards=0, clean_sheets=0,
                 id=None):
        self.surname = surname
        self.first_name = first_name
        self.squad_number = squad_number
        self.position = position
        self.goals_scored = goals
        self.assists = assists
        self.own_goals = own_goals
        self.y_cards = yellow_cards
        self.r_cards = red_cards
        self.clean_sheets = clean_sheets
        self.id = id