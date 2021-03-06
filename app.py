from flask import Flask, render_template

# import blueprints #
from controllers.teams_controller import teams_blueprint
from controllers.leagues_controller import leagues_blueprint
from controllers.fixtures_controller import fixture_blueprint

app = Flask(__name__)


# register blueprints #
app.register_blueprint(teams_blueprint)
app.register_blueprint(leagues_blueprint)
app.register_blueprint(fixture_blueprint)

@app.route('/')
def main():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
