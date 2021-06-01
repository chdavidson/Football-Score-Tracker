from datetime import date


class Signing:

    def __init__(self, player, team, signed_on=None, id=None):
        self.player = player
        self.team = team
        self.date = signed_on
        if signed_on is None:
            self.date = date.today()  # YYYY-MM-DD
        self.id = id

