# -*- coding: utf-8 -*-
__author__ = 'sebastian.kouba'
import re
import os
import pprint
import operator
"""
I'm just looking for the categories / regexp that make sense!

/s/ catches a lot -> static resources
/projects/
/images/
/download/resources
"""

# destination: /*/*/
slash_slash_re = re.compile(
    r'^[^\s]+\s[^\s]+\s[^\s]+\s\[[^\]]+\]\s\"(GET|POST)\s(/\w+/\w+[-]*\w+/)')
    # anything up to next slash, not just word with - like above
    # ouotputs too much
    # r'^[^\s]+\s[^\s]+\s[^\s]+\s\[[^\]]+\]\s\"(GET|POST)\s(/\w+/[^/]+/)')

create_issue_re = re.compile(
    r'^[^\s]+\s[^\s]+\s[^\s]+\s\[[^\]]+\]\s\"(GET|POST)\s(/\w+/[\w]*CreateIssue)')
    #r'^([^\s]+)\s([^\s]+)\s([^\s]+)\s\[([^\]]+)\]\s\"(GET|POST)\s([^\s]+)\s([^\"]+)\"\s([^\s]+)\s([^\s]+)\s([^\s]+)\s\"([^\"]+)\"\s\"([^\"]+)\"\s\"([^\"]+)\"\s')
#target = os.path.join("/Users/seb/dev/jala/logs", "access_log.2015-11-25")
target = os.path.join("C:\\", "dev", "access_log.2015-12-01")

result = {}
result["others"] = 0
with open(target) as f:
    for line in f:
        slash_tokens = slash_slash_re.match(line)
        create_issue_tokens = create_issue_re.match(line)
        # check for slash_slahs
        if slash_tokens:
            if slash_tokens.group(2) in result.keys():
                result[slash_tokens.group(2)] += 1
            else:
                result[slash_tokens.group(2)] = 1
        # check for issue create
        elif create_issue_tokens:
            if create_issue_tokens.group(2) in result.keys():
                result[create_issue_tokens.group(2)] += 1
            else:
                result[create_issue_tokens.group(2)] = 1
        """else:
            print(line)
            result["others"] += 1
        """

sorted_x = sorted(result.items(), key=operator.itemgetter(1))
pprint.pprint(sorted_x)
print("done")

"""
missing: /secure/Create
"""