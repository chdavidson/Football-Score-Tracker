from db.run_sql import run_sql
from models.player import Player
from models.team import Team
import repositories.stadium_repo as stadium_repo


def save(player):
    sql = 'INSERT INTO players (surname, first_name, squad_number, position, goals, assists, own_goals, yellow_cards, red_cards, clean_sheets) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s) RETURNING id'
    values = [player.surname, player.first_name,
              player.squad_number, player.position,
              player.goals, player.assists,
              player.own_goals, player.y_cards,
              player.r_cards, player.clean_sheets]
    results = run_sql(sql, values)
    player.id = results[0]['id']


def select_all():
    players = []
    sql = 'SELECT * FROM players'
    results = run_sql(sql)
    for result in results:
        players.append(Player(result['surname'], result['first_name'], 
                              result['squad_number'], result['postion'],
                              result['goals'], result['assists'],
                              result['own_goals'], result['yellow_cards'],
                              result['red_cards'], result['clean_sheets'],
                              result['id']))


def select(id):
    player = None
    sql = 'SELECT * FROM players WHERE id = %s'
    result = run_sql(sql, [id])[0]
    if result is not None:
        player = Player(result['surname'], result['first_name'],
                        result['squad_number'], result['postion'],
                        result['goals'], result['assists'],
                        result['own_goals'], result['yellow_cards'],
                        result['red_cards'], result['clean_sheets'],
                        result['id'])
    return player


def get_teams(player):
    teams = []
    sql = 'SELECT teams.* FROM teams INNER JOIN signings ON signings.team_id = teams.id WHERE signings.player_id = %s'
    results = run_sql(sql, [player.id])
    for result in results:
        teams.append(Team(result['name'], result['year_founded'],
                          stadium_repo.select(result['stadium_id']), result['id']))
    return teams


def update(player):
    sql = 'UPDATE players SET (surname, first_name, squad_number, position, goals, assists, own_goals, yellow_cards, red_cards, clean_sheets) = (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s) WHERE id = %s'
    values = [player.surname, player.first_name,
              player.squad_number, player.postion,
              player.goals_scored, player.assists,
              player.own_goals, player.y_cards,
              player.r_cards, player.clean_sheets,
              player.id]
    run_sql(sql, values)
