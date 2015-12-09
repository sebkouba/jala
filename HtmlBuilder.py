# -*- coding: utf-8 -*-
__author__ = 'seb'
import os
import time

class HtmlBuilder:
    def __init__(self, table_data):
        self.table_data = table_data

        # create dir
        cwd = os.getcwd()
        dir_name = time.strftime("%Y%m%d_%H%M%S")
        target_dir = os.path.join(cwd, dir_name)
        os.mkdir(target_dir)

        # create JS file
        make_js(table_data, target_dir)
        # create html file


"""
mkdir with timestamp
create js file
create html file
"""


def make_js(table_data, target_dir):
    js_file = os.path.join(target_dir, "index.js")
    js_text = """
    angular.module('sortApp', [])

    .controller('mainController', function ($scope){
    $scope.sortType = 'name'; // set the default sort type
    $scope.sortReverse = false;  // set the default sort order
    $scope.searchFish = '';     // set the default search/filter term

    $scope.sushi = %s

    ;
    });
    """ % table_data
    with open(js_file, 'a') as the_file:
        the_file.write(js_text)
