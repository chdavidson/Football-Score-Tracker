from db.run_sql import run_sql
from models.player import Player
from models.team import Team
import repositories.stadium_repo as stadium_repo


def save(player):
    sql = 'INSERT INTO players (surname, first_name, squad_number, position, goals, assists, own_goals, yellow_cards, red_cards, clean_sheets) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s) RETURNING id'
    values = [player.get_surname(), player.get_firstname(),
              player.get_squad_number(), player.get_position(),
              player.get_goals_scored(), player.get_assists(),
              player.get_own_goals(), player.get_yellow_cards(),
              player.get_red_cards(), player.get_clean_sheets()]
    results = run_sql(sql, values)
    player.set_id(results[0]['id'])


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
    results = run_sql(sql, [player.get_id()])
    for result in results:
        teams.append(Team(result['name'], result['year_founded'],
                          stadium_repo.select(result['stadium_id']), result['id']))
    return teams


def update(player):
    sql = 'UPDATE players SET (surname, first_name, squad_number, position, goals, assists, own_goals, yellow_cards, red_cards, clean_sheets) = (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s) WHERE id = %s'
    values = [player.get_surname(), player.get_firstname(),
              player.get_squad_number(), player.get_position(),
              player.get_goals_scored(), player.get_assists(),
              player.get_own_goals(), player.get_yellow_cards(),
              player.get_red_cards(), player.get_clean_sheets(),
              player.get_id()]
    run_sql(sql, values)
