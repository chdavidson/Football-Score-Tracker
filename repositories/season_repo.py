from models.fixture import Fixture
from db.run_sql import run_sql
import repositories.league_repo as league_repo
import repositories.team_repo as team_repo
from models.season import Season


def save(season):
    sql = 'INSERT INTO seasons (year, league_id) VALUES (%s, %s) RETURNING id'
    values = [season.year, season.league.id]
    result = run_sql(sql, values)
    season.id = (result[0]['id'])


def select(id):
    sql = 'SELECT * FROM seasons WHERE id = %s'
    result = run_sql(sql, [id])[0]
    return Season(result['year'],
                  league_repo.select(result['league_id']), result['id'])
    
    
def select_by_league(id):
    seasons = []
    sql = 'SELECT * FROM seasons WHERE league_id = %s'
    results = run_sql(sql, [id])
    for result in results:
        seasons.append(Season(result['year'],
                              league_repo.select(result['league_id']),
                              result['id']))
    return seasons


def get_all_fixtures(season):
    fixtures = []
    sql = 'SELECT * FROM fixtures WHERE season_id = %s'
    results = run_sql(sql, [season.id])
    counter = 0
    for result in results:
        fixtures.append(Fixture(team_repo.select(result['home_id']),
                                team_repo.select(result['away_id']),
                                season, result['id']))
        fixtures[counter].set_score(result['home_score'], result['away_score'])
        counter += 1 
    return fixtures
