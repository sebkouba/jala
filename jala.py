from flask import Flask, render_template
from createdb import db_session, create_db, requests_by_type
from models import init_db

app = Flask(__name__)
init_db()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/createdb')
def createdb():
    create_db()
    return "creating db"
    # open file
    # populate db


@app.route('/dash')
def dash():
    res = requests_by_type()
    return render_template('dashboard.html', data=res)

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


if __name__ == '__main__':
    app.run(debug=True)
