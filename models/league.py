class League():

    def __init__(self, name, association, id=None):
        self.name = name
        self.association = association
        self.id = id


    def generate_table(list_of_teams, list_of_fixtures):    
        league_table = []
        for team in list_of_teams:
            points = 0
            goals_for = 0
            goals_against = 0
            games_played = 0
            won = 0
            draw = 0
            for fixture in list_of_fixtures:
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
