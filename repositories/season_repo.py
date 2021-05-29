from models.fixture import Fixture
from db.run_sql import run_sql
import repositories.league_repo as league_repo
from models.season import Season


def save(season):
    sql = 'INSERT INTO seasons (year, league_id) VALUES (%s, %s) RETURNING id'
    values = [season.get_year(), season.get_league().get_id()]
    result = run_sql(sql, values)
    season.set_id(result[0]['id'])


def select(id):
    sql = 'SELECT * FROM seasons WHERE id = %s'
    result = run_sql(sql, [id])
    return Season(result['year'],
                  league_repo.select(result['league_id']), result['id'])


def get_all_fixtures(season):
    fixtures = []
    sql = 'SELECT * fixtures WHERE season_id = %s'
    results = run_sql(sql, [season.get_id()])
    for result in results:
        fixtures.append(Fixture(result['home_team'], result['away_team'],
                                season, result['id']))
    return fixtures
