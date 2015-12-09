# -*- coding: utf-8 -*-
__author__ = 'sebastian.kouba'

import re
import os
import pprint
import operator
from CategoryParser import CategoryParser


line_re = re.compile(
    r'^([^\s]+)\s([^\s]+)\s([^\s]+)\s\[([^\]]+)\]\s\"(GET|POST)\s([^\s]+)\s([^\"]+)\"\s([^\s]+)\s([^\s]+)\s([^\s]+)\s\"([^\"]+)\"\s\"([^\"]+)\"\s\"([^\"]+)\"\s')

#target = os.path.join("/Users/seb/dev/jala/logs", "access_log.2015-11-26")
target = os.path.join("C:\\", "dev", "access_log.2015-12-01")
#target = os.path.join("C:\\", "dev", "access_log.2015-11-26")
result = {}
cp = CategoryParser()

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

            cp.add_values(destination, duration, size)

    print ("-----------------------------------------------------------------")
    #pprint.pprint(cp.result)
    for cat in cp.result:
        print("{'category': '%s', 'duration': %s, 'size': %s, 'requests': %s},"
              % (cat, cp.result[cat]["duration"],
                 cp.result[cat]["size"], cp.result[cat]["count"]))
    print ("done")




