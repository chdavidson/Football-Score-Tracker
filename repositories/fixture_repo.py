# home, away, season, id
from db.run_sql import run_sql
from models.fixture import Fixture
import repositories.team_repo as team_repo
import repositories.season_repo as season_repo


def save(fixture):
    sql = 'INSERT INTO fixtures (home_id, away_id, season_id) VALUES (%s, %s, %s) RETURNING id'
    values = [fixture.get_fixture()[0].get_id(),
              fixture.get_fixture()[1].get_id(),
              fixture.get_season().get_id()]
    result = run_sql(sql, values)
    fixture.set_id(result[0]['id'])


def select(id):
    sql = 'SELECT * FROM fixtures WHERE id = %s'
    result = run_sql(sql, [id])
    return Fixture(team_repo.select(result['home_id']),
                   team_repo.select(result['away_id']),
                   season_repo.select(result['season_id']))

