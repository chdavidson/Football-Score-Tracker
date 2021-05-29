class League():
    __name__ = None
    __teams__ = []
    __fixtures__ = []
    __results__ = []
    __association__ = None
    __id__ = None

    def __init__(self, name, association, id=None):
        self.__name__ = name
        self.__association__ = association
        self.__id__ = id

    def get_id(self):
        return self.__id__
    
    def set_id(self, id):
        self.__id__ = id

    def get_association(self):
        return self.__association__

    def add_teams(self, teams):
        for team in teams:
            self.__teams__.append(team)

    def get_teams(self):
        return self.__teams__

    def add_fixtures(self, fixtures):
        # [[team_home, team_away]]
        for fixture in fixtures:
            self.__fixtures__.append(fixture)
 
    def add_result(self, fixture, home_goals, away_goals):
    # {team_home, team_away, goals_home, goals_away}
        result = {'home': fixture.get_fixture()[0],
                  'away': fixture.get_fixture()[1],
                  'home_score': home_goals,
                  'away_score': away_goals}
        self.__results__.append(result)

    def get_name(self):
        return self.__name__

    # def generate_table(self):
