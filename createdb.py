# -*- coding: utf-8 -*-
import json

__author__ = 'seb'
from models import LogEntry, db_session
from sqlalchemy import func
import os
import re


def create_db():
    #
    try:
        # load file into dictionary
        # data = open('example.log')

        line_re = re.compile(r'^([^\s]+)\s([^\s]+)\s([^\s]+)\s\[([^\]]+)\]\s\"(GET|POST)\s([^\s]+)\s([^\"]+)\"\s([^\s]+)\s([^\s]+)\s([^\s]+)\s\"([^\"]+)\"\s\"([^\"]+)\"\s\"([^\"]+)\"\s')
        # target = os.path.join("/Users/seb/dev/jala/logs",
         #                     "access_log.2015-11-25")
        target = os.path.join("C:\\", "dev",
                              "access_log.2015-11-27")
        with open(target) as f:
            for line in f:
                tokens = line_re.match(line)
                if tokens:
                    e = LogEntry(
                        sourceip=tokens.group(1),
                        request_id=tokens.group(2),
                        request_user=tokens.group(3),
                        timestamp=tokens.group(4),
                        request_type=tokens.group(5),
                        destination=tokens.group(6),
                        protocol=tokens.group(7),
                        return_code=tokens.group(8),
                        size=tokens.group(9),
                        duration=tokens.group(10),
                        referrer=tokens.group(11),
                        agent=tokens.group(12),
                        session=tokens.group(13)
                    )
                    db_session.add(e)
            #db_session.commit()

            db_session.commit()
    except Exception as ex:
        print(ex)
        db_session.rollback() #Rollback the changes on error
    finally:
        db_session.close() #Close the connection


def requests_by_type():
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
