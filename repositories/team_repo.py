from db.run_sql import run_sql
from models.team import Team
import repositories.stadium_repo as stadium_repo


def save(team):
    sql = 'INSERT INTO teams (name, year_founded, stadium_id) VALUES (%s, %s, %s) RETURNING id'
    values = [team.get_name(), team.get_founding_year(),
              team.get_stadium().get_id()]
    results = run_sql(sql, values)
    team.set_id(results[0]['id'])


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
    values = [team.get_name(), team.get_founding_year(),
              team.get_stadium().get_id(), team.get_id()]
    run_sql(sql, values)