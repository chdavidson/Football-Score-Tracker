
from flask import Flask, Blueprint, render_template, redirect
from models.league import League
import repositories.league_repo as league_repo
import repositories.participant_repo as participant_repo

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