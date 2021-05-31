from flask import Flask, Blueprint, render_template, redirect, request

from models.team import Team
from models.participant import Participant
import repositories.team_repo as team_repo
import repositories.stadium_repo as stadium_repo
import repositories.league_repo as league_repo
import repositories.participant_repo as participant_repo

teams_blueprint = Blueprint('teams', __name__)


# ADMINISTATOR ROUTES
@teams_blueprint.route('/admin/teams')
def admin_teams():
    teams = team_repo.select_all()
    return render_template('teams/admin/index.html', teams=teams)

@teams_blueprint.route('/admin/teams/edit/<id>')
def edit_team(id):
    return render_template('teams/admin/edit_team.html',
                           team=team_repo.select(id),
                           stadiums=stadium_repo.select_all())

@teams_blueprint.route('/admin/teams/new')
def add_team():
    stadiums = stadium_repo.select_all()
    leagues = league_repo.select_all()
    return render_template('teams/admin/new_team.html', stadiums=stadiums,
                           leagues=leagues)

@teams_blueprint.route('/admin/teams', methods=['POST'])
def found_team():
    name = request.form['name']
    year = request.form['year']
    stadium = request.form['stadium']
    league = request.form['league']
    new_team = Team(name, year, stadium_repo.select(stadium))
    team_repo.save(new_team)
    participant_repo.save(Participant(league_repo.select(league), new_team))
    return redirect('/admin/teams')


@teams_blueprint.route('/admin/teams/<id>', methods=['POST'])
def update_team(id):
    name = request.form['name']
    year = request.form['year']
    stadium = request.form['stadium']
    team_repo.update(Team(name, year, stadium_repo.select(stadium), id))
    return redirect('/admin/teams')

# User Routes
@teams_blueprint.route('/teams')
def user_teams():
    teams = team_repo.select_all()
    return render_template('teams/user/index.html', teams=teams)

@teams_blueprint.route('/teams/<team_id>')
def view_team(team_id):
    team = team_repo.select(team_id)
    fixtures = team_repo.find_fixtures(team_id)
    return render_template('teams/user/view_team.html', team=team, fixtures=fixtures)