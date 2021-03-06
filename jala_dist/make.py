# -*- coding: utf-8 -*-
import re
import os
import pprint
import operator
import HtmlBuilder as hb
import csv


def write_csv(data, target_dir):
    target = os.path.join(target_dir, 'user_data.csv')
    with open(target, 'wb') as fw:
        w = csv.writer(fw)
        #w.writerow(data.keys())
        for line in data:
            w.writerow(data[line].values())
            """w.writerow(str(data[line]["user"]) + ";" +
                       str(data[line]["duration"]) + ";" +
                       str(data[line]["requests"]))
            """


def get_files_from_cwd():
    """
    Searches current dir for access_log files
    :return:
    """
    file_list = []
    cwd = os.getcwd()
    #for root, dirs, files in os.walk(cwd):
    a_files = [name for name in os.listdir('.') if os.path.isfile(name)]
    for name in a_files:
        if name.startswith("access_log"):
            file_list.append(name)
    return file_list


def create_user_raw_data(in_files):
    """
    :param in_files: list of file paths to analyse
    :return: dict with user as key, user, request, durations as values
    """
    line_re = re.compile(
        r'^([^\s]+)\s([^\s]+)\s([^\s]+)\s\[([^\]]+)\]\s\"(GET|POST)\s([^\s]+)\s([^\"]+)\"\s([^\s]+)\s([^\s]+)\s([^\s]+)\s\"([^\"]+)\"\s\"([^\"]+)\"\s\"([^\"]+)\"\s')

    #target = os.path.join("/Users/seb/dev/jala/logs", "access_log.2015-11-26")
    #target = os.path.join("C:\\", "dev", "access_log.2015-11-26")
    #target = os.path.join("C:\\", "dev", "access_log.2015-12-01")
    #target = os.path.join("C:\\", "dev", "access_log.2015-12-10")

    user_raw_data = {}

    # user_data = []
    cat_data = []

    for target in in_files:

        with open(target) as f:
            for line in f:
                # split lines into tokens using regexp
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

                    # cat_parser.add_values(destination, duration, size)

                    if request_user not in user_raw_data.keys():
                        user_raw_data[request_user] = {"user": request_user,
                                                "requests": 1, "duration": int(duration)}
                    else:
                        user_raw_data[request_user]["requests"] += 1
                        user_raw_data[request_user]["duration"] += int(duration)

            #pprint.pprint(cp.result)
            # not doing the request categories for now
            """for cat in cat_parser.result:
                cat_data.append("{'category': '%s', "
                                "'duration': %s, "
                                "'size': %s, "
                                "'requests': %s},"
                                % (cat,
                                   cat_parser.result[cat]["duration"],
                                   cat_parser.result[cat]["size"],
                                   cat_parser.result[cat]["count"]))
            """
    return user_raw_data


def write_raw_to_html_csv(user_raw_data):
    """
    :param user_raw_data: data['username'][username,duration,requests]
    :return: creates csv and html files in timestamped directory
    """
    user_data = "["
    for user in user_raw_data:
        #user_data.append("{'username': '%s', 'duration': %s, 'requests': %s},"
        user_data += ("{'username': '%s', 'duration': %s, 'requests': %s},"
                         % (user_raw_data[user]["user"],
                            user_raw_data[user]["duration"],
                            user_raw_data[user]["requests"]))
    user_data += "]"
    builder = hb.HtmlBuilder(user_data)

    write_csv(user_raw_data, builder.dir_name)


files = get_files_from_cwd()

raw_data = create_user_raw_data(files)

write_raw_to_html_csv(raw_data)

print("done")