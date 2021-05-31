from db.run_sql import run_sql
from models.league import League
from models.team import Team
import repositories.association_repo as association_repo
import repositories.stadium_repo as stadium_repo


def save(league):
    sql = 'INSERT INTO leagues (name, association_id) VALUES (%s, %s) RETURNING id'
    values = [league.get_name(), league.get_association().get_id()]
    results = run_sql(sql, values)
    league.set_id(results[0]['id'])


def select_all():
    leagues = []
    sql = "SELECT * FROM leagues"
    results = run_sql(sql)
    for result in results:
        leagues.append(League(result['name'],
                              association_repo.select(result['association_id']),
                              result['id']))
    return leagues


def select(id):
    sql = 'SELECT * FROM leagues WHERE id = %s'
    result = run_sql(sql, [id])[0]
    return League(result['name'],
                  association_repo.select(result['association_id']),
                  result['id'])


def select_by_association(association):
    leagues = []
    sql = 'SELECT * FROM leagues WHERE association_id = %s'
    results = run_sql(sql, [association.get_id()])
    for result in results:
        leagues.append(League(result['name'], result['association_id'],
                              result['id']))
    return leagues


def find_participants(league_id):
    teams = []
    sql = 'SELECT teams.* FROM teams INNER JOIN participants ON participants.team_id = teams.id WHERE league_id = %s'
    results = run_sql(sql, [league_id])
    for result in results:
        teams.append(Team(result['name'], result['year_founded'],
                          stadium_repo.select(result['stadium_id']),
                          result['id']))
    return teams