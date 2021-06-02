from flask import Flask, Blueprint, render_template, redirect, request

import repositories.player_repo as player_repo
from models.player import Player

player_blueprint = Blueprint('player', __name__)


#USER ROUTES
@player_blueprint.route('/players')
def user_player_index():
    players = player_repo.select_all()
    return render_template('players/user/index.html', players)