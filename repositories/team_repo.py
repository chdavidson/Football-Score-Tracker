from db.run_sql import run_sql
from models.team import Team
from models.fixture import Fixture
from models.player import Player
import repositories.stadium_repo as stadium_repo
import repositories.season_repo as season_repo


def save(team):
    sql = 'INSERT INTO teams (name, year_founded, stadium_id) VALUES (%s, %s, %s) RETURNING id'
    values = [team.name, team.year_founded,
              team.stadium.id]
    results = run_sql(sql, values)
    team.id = results[0]['id']


def select_all():
    teams = []
    results = run_sql('SELECT * FROM teams')
    for result in results:
        teams.append(Team(result['name'], result['year_founded'],
                          stadium_repo.select(result['stadium_id']),
                          result['id']))
    return teams


def select(id):
    sql = 'SELECT * FROM teams WHERE id = %s'
    result = run_sql(sql, [id])[0]
    return Team(result['name'], result['year_founded'],
                stadium_repo.select(result['stadium_id']), result['id'])
   

def update(team):
    sql = 'UPDATE teams SET (name, year_founded, stadium_id) = (%s, %s, %s) WHERE id = %s'
    values = [team.name, team.year_founded,
              team.stadium.id, team.id]
    run_sql(sql, values)


def find_fixtures(team_id):
    fixtures = []
    sql = 'SELECT * FROM fixtures WHERE home_id = %s OR away_id = %s'
    values = [team_id, team_id]
    results = run_sql(sql, values)
    counter = 0
    for result in results:
        fixtures.append(Fixture(select(result['home_id']), select(result['away_id']),
                                season_repo.select(result['season_id']), result['id']))
        fixtures[counter].set_score(result['home_score'], result['away_score'])
        counter += 1
    return fixtures


def find_players(team_id):
    players = []
    sql = 'SELECT players.* FROM players INNER JOIN signings ON signings.player_id = players.id WHERE team_id = %s'
    results = run_sql(sql, [team_id])
    for result in results:
        players.append(Player(result['surname'], result['first_name'],
                              result['squad_number'], result['position'],
                              result['goals'], result['assists'],
                              result['own_goals'], result['yellow_cards'],
                              result['red_cards'], result['clean_sheets'],
                              result['id']))
    return players