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
        self.dir_name = dir_name
        target_dir = os.path.join(cwd, dir_name)
        os.mkdir(target_dir)

        # create JS file
        make_js(table_data, target_dir)
        # create html file
        make_html(target_dir)

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

        $scope.sushi =  %s
        ;
    });
    """ % table_data
    with open(js_file, 'a') as the_file:
        the_file.write(js_text)


def make_html(target_dir):
    # user version for now
    html_file = os.path.join(target_dir, "index.html")
    html_text = """
<!DOCTYPE html>
<html>
<head>
    <style>
        body { padding-top:50px; }
    </style>
    <meta charset="UTF-8">
    <title>Sort and Filter a Table Using Angular</title>
    <link rel='stylesheet prefetch'
          href='http://maxcdn.bootstrapcdn.com/bootswatch/3.2.0/sandstone/bootstrap.min.css'>
    <link rel='stylesheet prefetch'
          href='http://maxcdn.bootstrapcdn.com/font-awesome/4.2.0/css/font-awesome.min.css'>
</head>

<body>

<div class="container" ng-app="sortApp" ng-controller="mainController">
    <!-- search box -->
    <form>
        <div class="form-group">
            <div class="input-group">
                <div class="input-group-addon"><i class="fa fa-search"></i></div>
                <input type="text" class="form-control" placeholder="Search Username"
                       ng-model="searchFish">
            </div>
        </div>
    </form>

    <!-- Tabelle -->
    <table class="table table-bordered table-striped">

        <thead>
        <tr>
            <td>
                <a href="#" ng-click="sortType = 'username'; sortReverse = !sortReverse">
                    Username
                    <span ng-show="sortType == 'username' && !sortReverse"
                          class="fa fa-caret-down"></span>
                    <span ng-show="sortType == 'username' && sortReverse"
                          class="fa fa-caret-up"></span>
                </a>
            </td>
            <td>
                <a href="#" ng-click="sortType = 'duration'; sortReverse = !sortReverse">
                    Duration
                    <span ng-show="sortType == 'duration' && !sortReverse"
                          class="fa fa-caret-down"></span>
                    <span ng-show="sortType == 'duration' && sortReverse"
                          class="fa fa-caret-up"></span>
                </a>
            </td>
            <td>
                <a href="#"
                   ng-click="sortType = 'requests'; sortReverse = !sortReverse">
                    Nr of Requests
                    <span ng-show="sortType == 'requests' && !sortReverse"
                          class="fa fa-caret-down"></span>
                    <span ng-show="sortType == 'requests' && sortReverse"
                          class="fa fa-caret-up"></span>
                </a>
            </td>
        </tr>
        </thead>

        <tbody>
        <tr ng-repeat="roll in sushi | orderBy:sortType:sortReverse | filter:searchFish">
            <td>{{ roll.username }}</td>
            <td>{{ roll.duration }}</td>
            <td>{{ roll.requests }}</td>
        </tr>
        </tbody>

    </table>

</div>
<script src='http://ajax.googleapis.com/ajax/libs/angularjs/1.3.2/angular.min.js'></script>

<script src="index.js"></script>

</body>
</html>
        """
    with open(html_file, 'a') as the_file:
        the_file.write(html_text)
