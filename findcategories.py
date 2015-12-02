# -*- coding: utf-8 -*-
__author__ = 'sebastian.kouba'
import re
import os
import pprint

line_re = re.compile(
    r'^[^\s]+\s[^\s]+\s[^\s]+\s\[[^\]]+\]\s\"(GET|POST)\s(/\w+/\w+/)')

    #r'^([^\s]+)\s([^\s]+)\s([^\s]+)\s\[([^\]]+)\]\s\"(GET|POST)\s([^\s]+)\s([^\"]+)\"\s([^\s]+)\s([^\s]+)\s([^\s]+)\s\"([^\"]+)\"\s\"([^\"]+)\"\s\"([^\"]+)\"\s')
#target = os.path.join("/Users/seb/dev/jala/logs", "access_log.2015-11-25")
target = os.path.join("C:\\", "dev", "access_log.2015-12-01")

result = {}
with open(target) as f:
    for line in f:
        tokens = line_re.match(line)
        if tokens:
            if tokens.group(2) in result.keys():
                result[tokens.group(2)] += 1
            else:
                result[tokens.group(2)] = 1
pprint.pprint(result)
print("done")