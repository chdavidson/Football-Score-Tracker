class Fixture():
    __home_team__ = None
    __away_team__ = None
    __id__ = None
    __league__ = None

    def __init__(self, home_team, away_team, league, id=None):
        self.__home_team__ = home_team
        self.__away_team__ = away_team
        self.__id__ = id
        self.__league__ = league

    def get_id(self):
        return self.__id__
    
    def get_league(self):
        return self.__league__

    def get_fixture(self):
        return [self.__home_team__, self.__away_team__]


class Leagues():
    __name__ = None
    __teams__ = []
    __fixtures__ = []
    __results__ = []
    __association__ = None
    __id__ = None

    def __init__(self, name, association, teams=None, fixtures=None, id=None):
        self.__name__ = name
        self.__association__ = association
        self.__id__ = id
        for team in teams:
            self.__teams__.append(team)
        for fixture in fixtures:
            self.__fixtures__.append(fixture)

    def get_id(self):
        return self.__id__

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
