# -*- coding: utf-8 -*-
__author__ = 'seb'
from models import LogEntry, db_session
import json


def requests_by_type():
    issues = get_count_like("/browse/")
    """
    big_pics = LogEntry.query.filter(LogEntry.referrer.like("%-bigpicture/%")).count()
    structures = LogEntry.query.filter(LogEntry.referrer.like("%StructureBoard/%")).count()
    # structures = LogEntry.query.filter(LogEntry.referrer.like("%structure:widget%")).count()
    agile = LogEntry.query.filter(LogEntry.referrer.like("%RapidBoard%")).count()
    dashboards = LogEntry.query.filter(LogEntry.referrer.like("%Dashboard%")).count()
    """
    big_pics = get_count_like("-bigpicture")
    structures = get_count_like("StructureBoard/")
    agile = get_count_like("RapidBoard")
    dashboards = get_count_like("Dashboard")

    result = {'issues': issues, 'big_pics': big_pics, 'structures': structures,
              'agile': agile, 'dashboards': dashboards}
    mylist = [
        {'name': 'Issues', 'y': issues},
        {'name': 'Dashboards', 'y': dashboards},
        {'name': 'Agile', 'y': agile},

    ]
    json_result = json.dumps(result)
    return mylist


def get_count_like(keyword):
    count = LogEntry.query.filter(LogEntry.referrer == "%" + keyword + "%").count()
    return count

















"""
class that connects to the db and categorizes the requests
and referrer according to criteria defined here
I don't see how this would make any sense at all if it were a class
"""

"""
class JiraParser():

    def __init__(self):
        pass

    def requests_by_type(self):
        issues = LogEntry.query.filter(LogEntry.referrer.like("%/browse/%")).count()
        big_pics = LogEntry.query.filter(LogEntry.referrer.like("%-bigpicture/%")).count()
        structures = LogEntry.query.filter(LogEntry.referrer.like("%StructureBoard/%")).count()
        # structures = LogEntry.query.filter(LogEntry.referrer.like("%structure:widget%")).count()
        agile = LogEntry.query.filter(LogEntry.referrer.like("%RapidBoard%")).count()
        dashboards = LogEntry.query.filter(LogEntry.referrer.like("%Dashboard%")).count()
        result = {'issues': issues, 'big_pics': big_pics, 'structures': structures,
                  'agile': agile, 'dashboards': dashboards}
        mylist = [
            {'name': 'Issues', 'y': issues},
            {'name': 'Dashboards', 'y': dashboards},
            {'name': 'Agile', 'y': agile},

        ]
        json_result = json.dumps(result)
        return mylist
"""
