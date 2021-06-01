from db.run_sql import run_sql
from models.association import Football_Association
import repositories.association_repo as association_repo


def save(association):
    sql = 'INSERT INTO associations (name) VALUES (%s) RETURNING id'
    results = run_sql(sql, [association.name])
    association.id = results[0]['id']


def select_all():
    associations = []
    results = run_sql('SELECT * FROM associations')
    for result in results:
        associations.append(Football_Association(result['name'], result['id']))
    return associations


def select(id):
    association = None
    sql = 'SELECT * FROM associations WHERE id = %s'
    result = run_sql(sql, [id])[0]
    if result is not None:
        association = Football_Association(result['name'], result['id'])
    return association


def get_leagues(association):
    sql = 'SELECT * FROM leagues WHERE association_id = %s'
    return run_sql(sql, association.id)
