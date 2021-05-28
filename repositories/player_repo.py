from db.run_sql import run_sql
from models.player import Player


def save(player):
    sql = 'INSERT INTO players (surname, first_name, squad_number, postion, goals, assists, own_goals, yellow_cards, red_cards, clean_sheets) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s) RETURNING id'
    values = [player.get_surname(), player.get_firstname(),
              player.get_squad_number(), player.get_position(),
              player.get_goals_scored(), player.get_assists(),
              player.get_yellow_cards(), player.get_red_cards(),
              player.get_clean_sheets()]
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