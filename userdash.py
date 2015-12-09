# -*- coding: utf-8 -*-
__author__ = 'sebastian.kouba'

__author__ = 'sebastian.kouba'
import re
import os
import pprint
import operator

line_re = re.compile(
    r'^([^\s]+)\s([^\s]+)\s([^\s]+)\s\[([^\]]+)\]\s\"(GET|POST)\s([^\s]+)\s([^\"]+)\"\s([^\s]+)\s([^\s]+)\s([^\s]+)\s\"([^\"]+)\"\s\"([^\"]+)\"\s\"([^\"]+)\"\s')

# target = os.path.join("/Users/seb/dev/jala/logs", "access_log.2015-11-26")
#target = os.path.join("C:\\", "dev", "access_log.2015-12-01")
target = os.path.join("C:\\", "dev", "access_log.2015-11-26")
result = {}
with open(target) as f:
    for line in f:
        tokens = line_re.match(line)
        if tokens:
            sourceip = tokens.group(1)
            request_id = tokens.group(2)
            request_user = tokens.group(3)
            timestamp = tokens.group(4)
            request_type = tokens.group(5)
            destination = tokens.group(6)
            protocol = tokens.group(7)
            return_code = tokens.group(8)
            size = tokens.group(9)
            duration = tokens.group(10)
            referrer = tokens.group(11)
            agent = tokens.group(12)
            session = tokens.group(13)

            if request_user not in result.keys():
                result[request_user] = {"user": request_user,
                                        "requests": 1, "duration": int(duration)}
            else:
                result[request_user]["requests"] += 1
                result[request_user]["duration"] += int(duration)

    print("Number of users: " + str(len(result)))
    print ("-----------------------------------------------------------------")
#    pprint.pprint(result)
    for user in result:
        print("{'username': '%s', 'duration': %s, 'requests': %s},"
              % (result[user]["user"], result[user]["duration"],
                 result[user]["requests"]))
    print ("done")
