from models.team import Team
from models.fixture import Fixture


class League_Table():
    
    def __init__(self, list_of_teams, list_of_fixtures):
        self.list_of_teams = list_of_teams
        self.list_of_fixtures = list_of_fixtures
        
    def generate_table(self):
        league_table = []
        for team in self.list_of_teams:
            points = 0
            goals_for = 0
            goals_against = 0
            games_played = 0
            won = 0
            draw = 0
            for fixture in self.list_of_fixtures:
                if fixture.home_score is not None:
                    # Check home results:
                    if team.id == fixture.home_team.id:
                        games_played += 1
                        goals_for += fixture.home_score
                        goals_against += fixture.away_score
                        if fixture.home_score > fixture.away_score:
                            points += 3
                            won += 1
                        if fixture.home_score == fixture.away_score:
                            points += 1
                            draw += 1
                    # Check away results:
                    if team.id == fixture.away_team.id:
                        games_played += 1
                        goals_for += fixture.away_score
                        goals_against += fixture.home_score
                        if fixture.away_score > fixture.home_score:
                            points += 3
                            won += 1
                        if fixture.home_score == fixture.away_score:
                            points += 1
                            draw += 1
            league_table.append({'team': team.name,
                                 'games_played': games_played,
                                 'won': won,
                                 'draw': draw,
                                 'lost': (games_played-won-draw),
                                 'goals_for': goals_for,
                                 'goals_against': goals_against,
                                 'points': points})
        return league_table
