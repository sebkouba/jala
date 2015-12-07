angular.module('sortApp', [])

    .controller('mainController', function ($scope) {
        $scope.sortType = 'name'; // set the default sort type
        $scope.sortReverse = false;  // set the default sort order
        $scope.searchFish = '';     // set the default search/filter term


        $scope.cats = [
           {'category': 'EditComment', 'duration': 29172, 'size': 617430, 'requests': 141},
{'category': 'STATIC_RESOURCE', 'duration': 71, 'size': 261999, 'requests': 50},
{'category': 'REST_Agile_rapidview', 'duration': 296559, 'size': 91938447, 'requests': 497},
{'category': 'Other', 'duration': 3628481, 'size': 712988942, 'requests': 38130},
{'category': 'AddComment', 'duration': 2764, 'size': 27289, 'requests': 7},
{'category': 'OpenSearch', 'duration': 660, 'size': 52540, 'requests': 71},
{'category': 'SearchRequest_RSS', 'duration': 111134, 'size': 58269721, 'requests': 744},
{'category': 'Agile', 'duration': 78758, 'size': 8466383, 'requests': 188},
{'category': 'Charts', 'duration': 3, 'size': 10650, 'requests': 1},
{'category': 'PLUGINS_SERVLET', 'duration': 1860142, 'size': 155189965, 'requests': 455},
{'category': 'MyJiraHome', 'duration': 13157, 'size': 0, 'requests': 1072},
{'category': 'EditLabels', 'duration': 520, 'size': 27202, 'requests': 8},
{'category': 'ManageFilters', 'duration': 34223, 'size': 21436244, 'requests': 89},
{'category': 'static', 'duration': 2174145, 'size': 8441381122, 'requests': 193969},
{'category': 'REST_API_SHORTCUTS', 'duration': 64373, 'size': 13511703, 'requests': 3939},
{'category': 'Dashboard', 'duration': 829316, 'size': 167185970, 'requests': 3198},
{'category': 'images', 'duration': 30672, 'size': 2630504, 'requests': 22046},
{'category': 'EditIssue', 'duration': 216123, 'size': 35743402, 'requests': 496},
{'category': 'ACTIVITY_STREAMS', 'duration': 1390513, 'size': 56604589, 'requests': 1329},
{'category': 'REST_Agile', 'duration': 30964, 'size': 633098, 'requests': 73},
{'category': 'Thumbnail', 'duration': 16064, 'size': 8164026, 'requests': 880},
{'category': 'SearchRequest_XML', 'duration': 657782, 'size': 53874230, 'requests': 4817},
{'category': 'REST_API_FILTER', 'duration': 2085288, 'size': 125023205, 'requests': 6996},
{'category': 'QuickSearch', 'duration': 99066, 'size': 37382990, 'requests': 488},
{'category': 'MoveIssue', 'duration': 26425, 'size': 3115166, 'requests': 104},
{'category': 'UpdateUserPreferences', 'duration': 2397, 'size': 803290, 'requests': 22},
{'category': 'QuickCreateIssue', 'duration': 328732, 'size': 24446325, 'requests': 179},
{'category': 'REST_GADGET', 'duration': 5549023, 'size': 604770647, 'requests': 19641},
{'category': 'QueryComponent', 'duration': 217798, 'size': 91022490, 'requests': 1279},
{'category': 'REST_ACTIVITY_STREAM', 'duration': 2369, 'size': 150164, 'requests': 531},
{'category': 'Issue Link', 'duration': 12936956, 'size': 13053664, 'requests': 90565},
{'category': 'ProjectAvatar', 'duration': 13851, 'size': 15391197, 'requests': 7095},
{'category': 'Tempo_Rest', 'duration': 2086189, 'size': 10128721, 'requests': 12665},
{'category': 'REST_ISSUE_NAV', 'duration': 618576, 'size': 137076998, 'requests': 4642},
{'category': 'REST_bamboo', 'duration': 409, 'size': 2688, 'requests': 224},
{'category': 'BrowseProjects', 'duration': 6578, 'size': 1649542, 'requests': 18},
{'category': 'LinkJiraIssue', 'duration': 174848, 'size': 1238631, 'requests': 231},
{'category': 'Logout', 'duration': 12106, 'size': 5326339, 'requests': 432},
{'category': 'projects', 'duration': 97546, 'size': 7855122, 'requests': 186},
{'category': 'DeleteIssue', 'duration': 8716, 'size': 110950, 'requests': 44},
{'category': 'Structure', 'duration': 2299753, 'size': 273808161, 'requests': 124548},
{'category': 'REST_HELP_TIPS', 'duration': 1844427, 'size': 7578113, 'requests': 12652},
{'category': 'REST_onresolveBehaviours', 'duration': 236546, 'size': 13311698, 'requests': 25708},
{'category': 'REST_API', 'duration': 120228, 'size': 11285606, 'requests': 3456},
{'category': 'USER_AVATAR', 'duration': 46482, 'size': 33168359, 'requests': 16471},
{'category': 'REST_ANALYTICS', 'duration': 173911, 'size': 97526, 'requests': 32722},
{'category': 'CreateIssue', 'duration': 215050, 'size': 47286425, 'requests': 329},
{'category': 'ADMIN', 'duration': 130769, 'size': 23186330, 'requests': 260},
{'category': 'REST Status', 'duration': 12638, 'size': 506031, 'requests': 989},
{'category': 'Tempo_misc', 'duration': 7523142, 'size': 1660685028, 'requests': 6849},
{'category': 'INCLUDES', 'duration': 174, 'size': 24220, 'requests': 50},
{'category': 'JJupin', 'duration': 195703, 'size': 919250, 'requests': 24202},
{'category': 'REST_dashboards', 'duration': 7429, 'size': 150379, 'requests': 234},
{'category': 'SetSelectedIssue', 'duration': 1822, 'size': 0, 'requests': 18},
{'category': 'REST_MENU', 'duration': 41077, 'size': 9382088, 'requests': 15676},
{'category': 'Tempo Timesheet', 'duration': 365032, 'size': 13841696, 'requests': 1133},
{'category': 'REST_API_SEARCH', 'duration': 8727156, 'size': 1640031330, 'requests': 3569},
{'category': 'SearchRequest_Excel', 'duration': 16238, 'size': 2023467, 'requests': 12},
{'category': 'Login', 'duration': 291519, 'size': 26349353, 'requests': 16917},
{'category': 'REST_scriptrunner', 'duration': 277273, 'size': 35192880, 'requests': 168784},
{'category': 'BulkOperation', 'duration': 219616, 'size': 12555326, 'requests': 209},
{'category': 'AjaxIssueAction', 'duration': 5666579, 'size': 649557421, 'requests': 10529},
{'category': 'ProjectAdmin', 'duration': 580, 'size': 405494, 'requests': 1},
{'category': 'ATTACHMENTS', 'duration': 34440, 'size': 94156070, 'requests': 581},
{'category': 'IssueNavigator', 'duration': 2993, 'size': 0, 'requests': 246},
{'category': 'IssueXml', 'duration': 1227, 'size': 17773, 'requests': 1},
{'category': 'RPC', 'duration': 9423, 'size': 289396, 'requests': 65},
{'category': 'WorkflowTransition', 'duration': 1248884, 'size': 15149769, 'requests': 3911},
{'category': 'ViewUserHover', 'duration': 18117, 'size': 1839954, 'requests': 593},
{'category': 'ViewProfile', 'duration': 9716, 'size': 1800376, 'requests': 38},
{'category': 'GADGETS', 'duration': 32167, 'size': 161585627, 'requests': 7808},
{'category': 'User info', 'duration': 517287, 'size': 42237669, 'requests': 15842},
{'category': 'REST_Agile_xboard', 'duration': 4019647, 'size': 97480340, 'requests': 3203},
{'category': 'AjaxIssueEditAction', 'duration': 4743707, 'size': 1347936967, 'requests': 11947},
{'category': 'AssignIssue', 'duration': 62574, 'size': 373521, 'requests': 145},
{'category': 'Home', 'duration': 414, 'size': 0, 'requests': 167},
{'category': 'REST_CAPABILITIES', 'duration': 876, 'size': 428256, 'requests': 288},
{'category': 'REST_OTHER', 'duration': 7101351, 'size': 15653352, 'requests': 4967},
{'category': 'REST_COLLECTORS', 'duration': 10202, 'size': 884412, 'requests': 5172},
{'category': 'Issues', 'duration': 2643876, 'size': 2488753738, 'requests': 31174},
{'category': 'TempoIssuePanel', 'duration': 1119882, 'size': 38028501, 'requests': 11866},
        ];

    });