# -*- coding: utf-8 -*-
__author__ = 'seb'
"""
iterate over log
create value array for user & category in one loop
create html out files
"""

# -*- coding: utf-8 -*-
__author__ = 'sebastian.kouba'

import re
import os
import pprint
import operator
from CategoryParser import CategoryParser


line_re = re.compile(
    r'^([^\s]+)\s([^\s]+)\s([^\s]+)\s\[([^\]]+)\]\s\"(GET|POST)\s([^\s]+)\s([^\"]+)\"\s([^\s]+)\s([^\s]+)\s([^\s]+)\s\"([^\"]+)\"\s\"([^\"]+)\"\s\"([^\"]+)\"\s')

target = os.path.join("/Users/seb/dev/jala/logs", "access_log.2015-11-26")
#target = os.path.join("C:\\", "dev", "access_log.2015-12-01")
#target = os.path.join("C:\\", "dev", "access_log.2015-11-26")

user_raw_data = {}
cat_parser = CategoryParser()

user_data = []
cat_data = []

with open(target) as f:
    case_dict = {

    }
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

            cat_parser.add_values(destination, duration, size)

            if request_user not in user_raw_data.keys():
                user_raw_data[request_user] = {"user": request_user,
                                        "requests": 1, "duration": int(duration)}
            else:
                user_raw_data[request_user]["requests"] += 1
                user_raw_data[request_user]["duration"] += int(duration)

    print ("-----------------------------------------------------------------")
    #pprint.pprint(cp.result)
    for cat in cat_parser.result:
        cat_data.append("{'category': '%s', "
                        "'duration': %s, "
                        "'size': %s, "
                        "'requests': %s},"
                        % (cat,
                           cat_parser.result[cat]["duration"],
                           cat_parser.result[cat]["size"],
                           cat_parser.result[cat]["count"]))

    for user in user_raw_data:
        user_data.append("{'username': '%s', 'duration': %s, 'requests': %s},"
                         % (user_raw_data[user]["user"],
                            user_raw_data[user]["duration"],
                            user_raw_data[user]["requests"]))
    print("done")


