from flask import Flask, render_template

# import blueprints #
from controllers.teams_controller import teams_blueprint

app = Flask(__name__)


# register blueprints #
app.register_blueprint(teams_blueprint)

@app.route('/')
def main():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
