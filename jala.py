import json

from flask import Flask, render_template, jsonify
from createdb import db_session, create_db, requests_by_type
from models import init_db
import jira_parser

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
def dash(chartID='chart_ID', chart_type='pie', chart_height=500):
    subtitleText = 'TestSubtitle'
    dataSet = jira_parser.requests_by_type()
    pageType = 'graph'
    result = "[" + jsonify(data=dataSet).data + "]"
    series = [{'data': [{"name": 'Issues', "y": 3}, {'name': 'Boards', 'y': 6}]}]
    # series = [{'data': [json.dumps(dataSet)]}]
    title = {"text": 'My Title'}
    xAxis = {"categories": ['xAxis Data1', 'xAxis Data2', 'xAxis Data3']}
    yAxis = {"title": {"text": 'yAxis Label'}}
    chart = {"renderTo": chartID, "type": chart_type, "height": chart_height,}

    # res = requests_by_type()
    return render_template('dashboard.html', pageType=pageType,
                           subtitleText=subtitleText, dataSet=dataSet,
                           series=result, data=dataSet, chartID=chartID,
                           title=title,yAxis=yAxis, xAxis=xAxis,
                           chart_type=chart_type, chart=chart)

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


if __name__ == '__main__':
    app.run(debug=True)
