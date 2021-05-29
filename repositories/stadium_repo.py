from db.run_sql import run_sql
from models.stadium import Stadium


def save(stadium):
    sql = 'INSERT INTO stadiums (name, location, capacity) VALUES (%s, %s, %s) RETURNING id'
    values = [stadium.get_name(), stadium.get_location(),
              stadium.get_capacity()]
    results = run_sql(sql, values)
    stadium.set_id(results[0]['id'])


def select(id):
    sql = 'SELECT * FROM stadiums WHERE id = %s'
    result = run_sql(sql, [id])[0]
    return Stadium(result['name'], result['location'],
                   result['capacity'], result['id'])

