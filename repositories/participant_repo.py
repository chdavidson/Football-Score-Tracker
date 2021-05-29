from db.run_sql import run_sql
from models.participant import Participant
import repositories.team_repo as team_repo
import repositories.league_repo as league_repo


def save(participant):
    sql = 'INSERT INTO participants (league_id, team_id) VALUES (%s, %s) RETURNING id'
    values = [participant.get_league().get_id(), participant.get_team().get_id()]
    result = run_sql(sql, values)
    participant.set_id(result[0]['id'])


def select(id):
    sql = 'SELECT * FROM participants WHERE id = %s'
    result = run_sql(sql, [id])
    return Participant(league_repo.select(result['league_id']),
                       team_repo.select(result['team_id']),
                       result['id'])


def delete(id):
    sql = "DELETE FROM participants WHERE id = %s"
    run_sql(sql, [id])