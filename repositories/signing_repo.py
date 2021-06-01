from db.run_sql import run_sql
from models.signing import Signing
import repositories.player_repo as player_repo
import repositories.team_repo as team_repo


def save(signing):
    sql = "INSERT INTO signings (team_id, player_id, signed_on) VALUES (%s, %s, %s) RETURNING id"
    values = [signing.team.id, signing.player.id, signing.date]
    results = run_sql(sql, values)
    signing.id = (results[0]['id'])


def select(id):
    sql = 'SELECT * FROM signings WHERE id = %s'
    result = run_sql(sql, [id])
    return Signing(player_repo.select(result['player_id']), team_repo.select(result['team_id']), result['signed_on'], result['id'])


def delete(id):
    sql = 'DELETE FROM signings WHERE id = %s'
    run_sql(sql, [id])