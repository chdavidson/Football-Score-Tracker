from flask import Flask, Blueprint, render_template, redirect, request

from models.team import Team
import repositories.team_repo as team_repo
import repositories.stadium_repo as stadium_repo

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
    return render_template('teams/admin/new_team.html', stadiums=stadiums)

@teams_blueprint.route('/admin/teams', methods=['POST'])
def found_team():
    name = request.form['name']
    year = request.form['year']
    stadium = request.form['stadium']
    new_team = Team(name, year, stadium_repo.select(stadium))
    team_repo.save(new_team)
    return redirect('/admin/teams')


@teams_blueprint.route('/admin/teams/<id>', methods=['POST'])
def update_team(id):
    name = request.form['name']
    year = request.form['year']
    stadium = request.form['stadium']
    team_repo.update(Team(name, year, stadium_repo.select(stadium), id))
    return redirect('/admin/teams')
