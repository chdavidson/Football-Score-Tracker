from flask import Flask, Blueprint, render_template, redirect, request
from models.fixture import Fixture
import repositories.fixture_repo as fixture_repo
import repositories.season_repo as season_repo
import repositories.team_repo as team_repo
import repositories.league_repo as league_repo

fixture_blueprint = Blueprint('fixtures', __name__)

# ADMINISTRATOR ROUTES
@fixture_blueprint.route('/admin/fixtures')
def admin_fixtures():
    leagues = league_repo.select_all()
    return render_template('fixtures/admin/index.html', leagues=leagues)


@fixture_blueprint.route('/admin/fixtures/<league_id>')
def admin_fixtures_of_league(league_id):
    seasons = season_repo.select_by_league(league_id)
    return render_template('fixtures/admin/seasons_index.html',
                           seasons=seasons, league=league_repo.select(league_id))


@fixture_blueprint.route('/admin/fixtures/<league_id>/<season_id>')
def show_fixtures_of_season(league_id, season_id):
    fixtures = season_repo.get_all_fixtures(season_repo.select(season_id))
    return render_template('fixtures/admin/fixtures_index.html',
                           fixtures=fixtures, season=season_repo.select(season_id),
                           league=league_repo.select(league_id))


@fixture_blueprint.route('/admin/fixtures/<league_id>/<season_id>/new')
def create_fixture(league_id, season_id):
    return render_template('fixtures/admin/new_fixture.html',
                           participants=league_repo.find_participants(league_id),
                           season=season_repo.select(season_id),
                           league=league_repo.select(league_id))


@fixture_blueprint.route('/admin/fixtures/<league_id>/<season_id>', methods=['POST'])
def save_fixture(league_id, season_id):
    home_team = team_repo.select(request.form['home_team'])
    away_team = team_repo.select(request.form['away_team'])
    season = season_repo.select(season_id)
    fixture_repo.save(Fixture(home_team, away_team, season))
    return redirect('/admin/fixtures/'+league_id+'/'+season_id)


@fixture_blueprint.route('/admin/fixtures/<league_id>/<season_id>/<fixture_id>')
def record_score(league_id, season_id, fixture_id):
    fixture = fixture_repo.select(fixture_id)
    return render_template('fixtures/admin/record_score.html',
                           home_team=fixture.home_team,
                           away_team=fixture.away_team,
                           league_id=league_id, season_id=season_id, fixture_id=fixture_id)
    
    
@fixture_blueprint.route('/admin/fixtures/<league_id>/<season_id>/<fixture_id>', methods=['POST'])
def save_score(league_id, season_id, fixture_id):
    fixture = fixture_repo.select(fixture_id)
    fixture.set_score(int(request.form['home_team_score']), int(request.form['away_team_score']))
    fixture_repo.update(fixture)
    return redirect('/admin/fixtures/'+league_id+'/'+season_id)