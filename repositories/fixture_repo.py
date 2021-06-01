# home, away, season, id
from db.run_sql import run_sql
from models.fixture import Fixture
import repositories.team_repo as team_repo
import repositories.season_repo as season_repo


def save(fixture):
    sql = 'INSERT INTO fixtures (home_id, away_id, season_id, home_score, away_score) VALUES (%s, %s, %s, %s, %s) RETURNING id'
    values = [fixture.home_team.id, fixture.away_team.id,
              fixture.season.id, fixture.home_score, fixture.away_score]
    result = run_sql(sql, values)
    fixture.id = result[0]['id']


def select(id):
    sql = 'SELECT * FROM fixtures WHERE id = %s'
    result = run_sql(sql, [id])[0]
    fixture = Fixture(team_repo.select(result['home_id']),
                      team_repo.select(result['away_id']),
                      season_repo.select(result['season_id']),
                      result['id'])
    fixture.set_score(result['home_score'], result['away_score'])
    return fixture


def update(fixture):
    sql = 'UPDATE fixtures SET (home_score, away_score) = (%s, %s) WHERE id = %s'
    values = [fixture.home_score, fixture.away_score, fixture.id]
    run_sql(sql, values)


def select_all_upcoming_fixtures():
    fixtures = []
    results = run_sql('SELECT * FROM fixtures WHERE home_score IS NULL')
    for result in results:
        fixtures.append(Fixture(team_repo.select(result['home_id']),
                                team_repo.select(result['away_id']),
                                season_repo.select(result['season_id']),
                                result['id']))
    return fixtures

