class Fixture():

    def __init__(self, home_team, away_team, season, id=None):
        self.home_team = home_team
        self.away_team = away_team
        self.id = id
        self.season = season
        self.home_score = None
        self.away_score = None

    def set_score(self, home_score, away_score):
        self.home_score = home_score
        self.away_score = away_score
