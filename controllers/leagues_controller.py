
from flask import Flask, Blueprint, render_template, redirect
from operator import itemgetter, le
from flask.templating import render_template_string
from models.league_table import League_Table
import repositories.league_repo as league_repo
import repositories.participant_repo as participant_repo
import repositories.season_repo as season_repo

leagues_blueprint = Blueprint('leagues', __name__)


# ADMINISTATOR ROUTES
@leagues_blueprint.route('/admin/leagues')
def admin_leagues():
    leagues = league_repo.select_all()
    return render_template('leagues/admin/index.html', leagues=leagues)


@leagues_blueprint.route('/admin/leagues/<id>')
def league_detail(id):
    teams = league_repo.find_participants(id)
    return render_template('leagues/admin/edit_league.html', teams=teams,
                           league=league_repo.select(id))


@leagues_blueprint.route('/admin/leagues/<league_id>/remove/<team_id>')
def remove_team_from_league(league_id, team_id):
    participant_repo.delete_team_from_league(league_id, team_id)
    # should fixtures from this league also be removed? Probably.
    return redirect('/admin/leagues/'+league_id)


# USER ROUTES
@leagues_blueprint.route('/leagues')
def user_leagues():
    leagues = league_repo.select_all()
    return render_template('leagues/user/index.html', leagues=leagues)


@leagues_blueprint.route('/leagues/<league_id>')
def user_league_detail(league_id):
    seasons = season_repo.select_by_league(league_id)
    return render_template('leagues/user/season_index.html', seasons=seasons, current_league=league_id)


@leagues_blueprint.route('/leagues/<league_id>/<season_id>')
def user_league_summary(league_id, season_id):
    teams = league_repo.find_participants(league_id)
    fixtures = season_repo.get_all_fixtures(season_repo.select(season_id))
    
    league_table = League_Table(teams, fixtures)
    table = league_table.generate_table()
    for t in table:
        print(t)
    
    table = sorted(table, key=itemgetter('points'), reverse=True)
    return render_template('leagues/user/league_table.html',
                           table=table,
                           season=season_repo.select(season_id),
                           league=league_repo.select(league_id))
    

