# -*- coding: utf-8 -*-
import re

__author__ = 'sebastian.kouba'


def get_category(dest):
    if dest.startswith("/s/") or dest.startswith("/download/resources"):
        return "static"

    if dest.startswith("/images"):
        return "images"
    if dest.startswith("/rest/tempo-timesheets/"):
        return "Tempo Timesheet"

    if dest.startswith("/rest/structure/"):
        return "Structure"

    if dest.startswith("/rest/keplerrominfo/"):
        return "JJupin"

    if dest.startswith("/projects/"):
        return "projects"

    if dest.startswith("/?") or dest == "/secure/" or dest.startswith(
            "/secure/default.jsp"):
        return 'Home'

    if dest.startswith("/default.jsp?clicked=footer") or (dest == ""):
        return 'Home'

    if dest.startswith("/secure/IssueNavigator.jspa") or dest.startswith(
            "/secure/IssueNavigator!"):
        return 'IssueNavigator'

    if dest.startswith("/issues/"):
        return 'Issues'

    if dest == "/i":
        return 'Issues'

    if dest.startswith("/rest/api/2/user/viewissue/search"):
        return "Issues"

    if dest.startswith("/rest/api/2/issue"):
        return "Issues"

    if dest.startswith("/secure/BrowseProjects.jspa"):
        return 'BrowseProjects'

    if dest.startswith("/secure/BrowseProject.jspa"):
        return 'BrowseProject'

    if dest == "/browse/" or dest == "/browse":
        return 'BrowseProject'

    if dest == "/includes/jira/issue/searchIssueTypes.js":
        return 'INCLUDES'

    if dest.startswith("/includes/blank.html?"):
        return 'INCLUDES'

    if dest == "/includes/deployJava.js":
        return 'INCLUDES'

    if dest.startswith("/includes/js"):
        return 'INCLUDES'

    if dest.startswith("/rpc/soap"):
        return 'RPC'

    if dest.startswith("/rpc/xmlrpc"):
        return 'RPC'

    if dest.startswith("/rpc/json-rpc"):
        return 'RPC'

    if dest.startswith("/secure/WikiRendererHelpAction.jspa"):
        return 'WikiRendererHelp'

    if dest.startswith("/secure/ViewUserHover!default.jspa"):
        return 'ViewUserHover'

    if dest.startswith("/secure/popups/UserPickerBrowser.jspa"):
        return 'UserPickerBrowser'

    if dest.startswith("/secure/UpdateUserPreferences.jspa") or dest.startswith(
            "/secure/UpdateUserPreferences!"):
        return 'UpdateUserPreferences'

    if dest.startswith("/secure/Dashboard.jspa") or dest.startswith(
            "Dashboard.jspa"):
        return 'Dashboard'

    if dest.startswith("/secure/ViewProfile.jspa"):
        return 'ViewProfile'

    if dest.startswith("/sr/jira.issueviews:searchrequest-xml/"):
        return 'SearchRequest_XML'

    if dest.startswith(
            "/sr/jira.issueviews:searchrequest-rss") or dest.startswith(
        "/sr/jira.issueviews%3Asearchrequest-rss"):
        return 'SearchRequest_RSS'

    if dest.startswith("/sr/jira.issueviews:searchrequest-comments-rss/"):
        return 'SearchRequest_RSS'

    if dest.startswith(
            "/sr/jira.issueviews:searchrequest-excel-current-fields"):
        return 'SearchRequest_Excel'

    if dest.startswith("/secure/CreateIssue.jspa") or dest.startswith(
            "/secure/CreateIssue!") or dest.startswith(
        "/secure/CreateIssueDetails!") or dest.startswith(
        "/secure/CreateIssueDetails.jspa") or dest.startswith(
        "/secure/CreateSubTaskIssueDetails.jspa") or dest.startswith(
        "/secure/CreateSubTaskIssue.jspa") or dest.startswith(
        "/secure/CreateSubTaskIssue!"):
        return 'CreateIssue'

    if dest.startswith("/secure/QuickCreateIssue!default.jspa"):
        return 'CreateIssue'

    if dest.startswith("/secure/ReleaseNote.jspa"):
        return 'ReleaseNote'

    if dest.startswith("/secure/QuickSearch.jspa"):
        return 'QuickSearch'

    if dest.startswith("/rest/activity-stream"):
        return 'REST_ACTIVITY_STREAM'

    if dest.startswith("/rest/greenhopper/1.0/xboard"):
        return 'REST_Agile_xboard'

    if dest.startswith("/rest/greenhopper/1.0/rapidview"):
        return 'REST_Agile_rapidview'

    if dest.startswith("/rest/greenhopper"):
        return 'REST_Agile'

    if dest.startswith("/rest/crm/"):
        return 'REST_CRM'

    if dest.startswith("/rest/myrestresource/"):
        return 'REST_myrestresource'

    if dest.startswith("/rest/whoslooking/"):
        return 'REST_whoslooking'

    if dest.startswith("/rest/dashboards/"):
        return 'REST_dashboards'

    if dest.startswith("/login.jsp") or dest.startswith("/loginsso.jsp"):
        return 'Login'

    if dest.startswith("/rest/auth/1/session"):
        return "Login"

    if dest.startswith("/secure/Logout!") or dest.startswith("/logout"):
        return 'Logout'

    if dest.startswith("/secure/attachment/"):
        return 'ATTACHMENTS'

    if dest.startswith("/secure/attachmentzip/unzip/"):
        return 'ATTACHMENTS'

    if dest.startswith("/secure/ManageAttachments.jspa") or dest.startswith(
            "/secure/ManageAttachments!") or dest.startswith(
        "/secure/AttachFile"):
        return 'ATTACHMENTS'

    if dest.startswith("/secure/DeleteAttachment.jspa") or dest.startswith(
            "/secure/DeleteAttachment!") or dest.startswith(
        "/secure/AttachFile"):
        return 'ATTACHMENTS'

    if dest.startswith("/secure/AttachTemporaryFile.jspa"):
        return 'ATTACHMENTS'

    if dest.startswith("/plugins/servlet/streams"):
        return 'ACTIVITY_STREAMS'

    if dest.startswith("/activity?"):
        return 'ACTIVITY_STREAMS'

    if dest.startswith("/plugins/servlet/gadgets/"):
        return 'GADGETS'

    if dest.startswith("/rest/gadgets"):
        return 'GADGETS'

    if dest.startswith("/secure/RunPortlet.jspa"):
        return 'RunPortlet'

    if dest.startswith("/secure/useravatar"):
        return 'USER_AVATAR'

    if (dest == "/osd.jsp"):
        return 'OpenSearch'

    if dest.startswith("/secure/WorkflowUIDispatcher.jspa"):
        return 'WorkflowTransition'

    if dest.startswith("/secure/CommentAssignIssue!default.jspa") or \
            dest.startswith("/secure/CommentAssignIssue.jspa"):
        return 'WorkflowTransition'

    if dest.startswith("/secure/SaveAsFilter!") or dest.startswith(
            "/secure/SaveAsFilter.jspa"):
        return 'SaveAsFilter'

    if dest.startswith("/secure/ManageFilters!") or dest.startswith(
            "/secure/ManageFilters.jspa"):
        return 'ManageFilters'

    if dest.startswith("/secure/RapidBoard.jspa") or (
                dest == "/secure/GreenHopper.jspa"):
        return 'Agile'

    if dest.startswith("/secure/EditAction"):
        return 'EditAction'

    if dest.startswith("/secure/ViewIssue.jspa"):
        return 'ViewIssue'

    if dest.startswith("/secure/AjaxIssueAction.jspa") or dest.startswith(
            "/secure/AjaxIssueAction!"):
        return 'AjaxIssueAction'

    if dest.startswith("/secure/AjaxIssueEditAction.jspa") or dest.startswith(
            "/secure/AjaxIssueEditAction!"):
        return 'AjaxIssueEditAction'

    if dest.startswith("/si/jira.issueviews:issue-xml/"):
        return 'IssueXml'

    if dest.startswith("/secure/EditIssue") or dest.startswith(
            "/secure/EditSubTaskIssue"):
        return 'EditIssue'

    if dest.startswith("/secure/DeleteIssue"):
        return 'DeleteIssue'

    if dest.startswith(
            "/secure/QuickEditIssue!default.jspa") or dest.startswith(
            "/secure/QuickEditIssue.jspa"):
        return 'EditIssue'

    if dest.startswith("/secure/MoveIssue"):
        return 'MoveIssue'

    if dest.startswith("/secure/AddComment.jspa") or dest.startswith(
            "/secure/AddComment!"):
        return 'AddComment'

    if dest.startswith("/secure/CreateWorklog.jspa") or dest.startswith(
            "/secure/CreateWorklog!"):
        return 'CreateWorklog'

    if dest.startswith("/secure/EditComment"):
        return 'EditComment'

    if dest.startswith("/secure/QuickCreateIssue"):
        return 'QuickCreateIssue'

    """
        if ((requestMethod == RequestMethod.GET) & & dest.startswith(
                "/secure/IssueAction!default.jspa"):
            return 'INLINE_EDIT_REFRESH'

        if ((requestMethod == RequestMethod.POST) & & dest.startswith(
                "/secure/IssueAction!default.jspa"):
            return 'INLINE_EDIT_POST'

        if ((requestMethod == RequestMethod.POST) & & dest.startswith(
                "/secure/IssueAction.jspa"):
            return 'INLINE_EDIT_POST'
    """

    if dest.startswith("/secure/views/bulkedit/"):
        return 'BulkOperation'

    if dest.startswith("/secure/EditLabels!") or dest.startswith(
            "/secure/EditLabels.jspa"):
        return 'EditLabels'

    if dest.startswith("/charts?filename="):
        return 'Charts'

    if dest.startswith("/secure/QueryComponent"):
        return 'QueryComponent'

    if dest.startswith("/secure/VoteOrWatchIssue.jspa"):
        return 'VoteOrWatchIssue'

    if dest.startswith("/secure/projectavatar"):
        return 'ProjectAvatar'

    if dest.startswith("/secure/AssignIssue"):
        return 'AssignIssue'

    if dest.startswith("/rest/gadget"):
        return 'REST_GADGET'

    if dest.startswith("/secure/RankTop.jspa") or dest.startswith(
            "/secure/RankBottom.jspa") or dest.startswith(
        "/secure/GHGoToBoard.jspa") or dest.startswith(
        "/secure/GHLocateIssueOnBoard.jspa") or dest.startswith(
        "/secure/GHLocateSprintOnBoard.jspa"):
        return 'Agile'

    if dest.startswith("/secure/VersionBoard.jspa") or dest.startswith(
            "/secure/VersionBoard!"):
        return 'Agile'

    if dest.startswith("/secure/TaskBoard.jspa") or dest.startswith(
            "/secure/TaskBoard!"):
        return 'Agile'

    if dest.startswith("/secure/VBRefreshBoard.jspa") or dest.startswith(
            "/secure/VBRefreshBoard!"):
        return 'Agile'

    if dest.startswith("/secure/VBRefreshBreadcrumbs.jspa") or dest.startswith(
            "/secure/VBRefreshBreadcrumbs!"):
        return 'Agile'

    if dest.startswith("/secure/BoardOptions.jspa") or dest.startswith(
            "/secure/BoardOptions!"):
        return 'Agile'

    if dest.startswith("/secure/SearchBoard.jspa") or dest.startswith(
            "/secure/SearchBoard!"):
        return 'Agile'

    if dest.startswith("/secure/ChartBoard.jspa") or dest.startswith(
            "/secure/ChartBoard!"):
        return 'Agile'

    if dest.startswith("/secure/GetBoardForIssue2.jspa") or dest.startswith(
            "/secure/GetBoardForIssue2!"):
        return 'Agile'

    if dest.startswith("/secure/GHCreateNewIssue.jspa") or dest.startswith(
            "/secure/GHCreateNewIssue!"):
        return 'Agile'

    if dest.startswith("/secure/GHAddIssue.jspa") or dest.startswith(
            "/secure/GHAddIssue!"):
        return 'Agile'

    if dest.startswith("/secure/GreenHopperClassic.jspa") or dest.startswith(
            "/secure/GreenHopperClassic!"):
        return 'Agile'

    if dest.startswith("/secure/RapidView.jspa") or dest.startswith(
            "/secure/RapidView!"):
        return 'Agile'

    if dest.startswith("/secure/ManageRapidViews.jspa") or dest.startswith(
            "/secure/ManageRapidViews!"):
        return 'Agile'

    if dest.startswith("/secure/MyJiraHome.jspa"):
        return 'MyJiraHome'

    if dest.startswith("/secure/thumbnail"):
        return 'Thumbnail'

    if dest.startswith("/plugins/servlet"):
        return 'PLUGINS_SERVLET'

    if dest.startswith("/secure/LinkJiraIssue.jspa") or dest.startswith(
            "/secure/LinkJiraIssue!"):
        return 'LinkJiraIssue'

    if dest.startswith("/download/resources/"):
        return 'PLUGIN_RESOURCES'

    if dest.startswith("/lazyLoader"):
        return 'LazyPortletLoader'

    if dest.startswith("/dwr/"):
        return 'DWR'

    if dest.startswith("/s/"):
        return 'STATIC_RESOURCE'

    if dest.startswith("/images/"):
        return 'STATIC_RESOURCE'

    if dest == "/styles/combined.css" or dest == "/styles/global.css":
        return 'STATIC_RESOURCE'

    if dest == "/favicon.ico" or dest == "/robots.txt":
        return 'STATIC_RESOURCE'

    if dest.startswith("/images/throbber/") or dest.startswith(
            "/download/batch/com.atlassian.upm.atlassian-universal-plugin"
            "-manager"
            "-plugin:upgrade-notification/com.atlassian.upm.atlassian-universal"
            "-plugin-manager-plugin:upgrade-notification.js"):
        return 'STATIC_RESOURCE'

    if dest.startswith("/secure/project/"):
        return 'ProjectAdmin'

    if dest.startswith("/secure/admin") or dest.startswith(
            "/secure/AdminSummary.jspa"):
        return 'ADMIN'

    if dest.startswith("/secure/SetSelectedIssue.jspa"):
        return 'SetSelectedIssue'

    if dest.startswith("/rest/collectors/"):
        return 'REST_COLLECTORS'

    if dest.startswith("/rest/analytics/"):
        return 'REST_ANALYTICS'

    if dest.startswith("/rest/capabilities"):
        return 'REST_CAPABILITIES'

    if dest.startswith("/rest/menu/"):
        return 'REST_MENU'

    if dest.startswith("/rest/nav-links-analytics-data/"):
        return 'REST_NAV_LINKS_ANALYTICS_DATA'

    if dest.startswith("/rest/mobile/"):
        return 'REST_MOBILE'

    if dest.startswith("/rest/issueNav/"):
        return 'REST_ISSUE_NAV'

    if dest.startswith("/rest/helptips/"):
        return 'REST_HELP_TIPS'

    if dest.startswith("/rest/viewIssue/"):
        return 'REST_HELP_TIPS'

    if dest.startswith("/rest/lasso/"):
        return 'REST_LASSO'

    if dest.startswith("/rest/api/2/search"):
        return 'REST_API_SEARCH'

    if dest.startswith("/rest/api/2/filter/"):
        return 'REST_API_FILTER'

    if dest.startswith("/rest/api/1.0/shortcuts"):
        return 'REST_API_SHORTCUTS'

    if dest.startswith("/rest/scriptrunner/"):
        return 'REST_scriptrunner'

    if dest.startswith("/rest/scriptrunner-jira/"):
        return 'REST_scriptrunner'

    if dest.startswith("/rest/remote-link-aggregation/"):
        return 'REST_remote_link_aggregation'

    if dest.startswith("/rest/com.onresolve.jira.plugin.Behaviours/"):
        return 'REST_onresolveBehaviours'

    if dest.startswith("/rest/jeditortemplateresource/"):
        return 'REST_jeditortemplateresource'

    if dest.startswith("/rest/bamboo/"):
        return 'REST_bamboo'

    if dest.startswith("/secure/errors.jsp"):
        return 'Errors_jsp'

    if dest.startswith("/TempoIssuePanel!default.jspa"):
        return 'TempoIssuePanel'

    if dest.startswith("/secure/Tempo") or dest.startswith("/Tempo"):
        return 'Tempo_misc'

    if dest.startswith("/rest/tempo-rest/"):
        return "Tempo_Rest"

    if dest.startswith("/rest/api/2/status"):
        return "REST Status"

    if dest.startswith("/rest/api/2/user?username"):
        return "User info"

    if dest.startswith("/rest/api/latest/user"):
        return "User info"

    re_rest_edit = re.compile(r'^/rest/api/2/issue/.*/editmeta')
    rest_edit = re_rest_edit.match(dest)
    if rest_edit:
        return 'REST Edit Issue'

    re_remote = re.compile(r'/rest/api/latest/issue/.*/remotelink')
    remote = re_remote.match(dest)
    if remote:
        return "Issue Link"

    if dest.startswith("/rest/api/"):
        return 'REST_API'

    if dest.startswith("/rest/"):
        return 'REST_OTHER'

    return "Other"


class CategoryParser:
    def __init__(self):
        # I know nothing about classes in python!
        self.result = {}

    def add_values(self, destination, duration, size):
        if size == "-":
            size = 0
        cat = get_category(destination)
        if cat not in self.result.keys():
            self.result[cat] = {'duration': int(duration), 'size': int(size),
                                'count': 1}
        else:
            self.result[cat]['duration'] += int(duration)
            self.result[cat]['size'] += int(size)
            self.result[cat]['count'] += 1
"""
What should this class do?
Input?
    RAW
        destination -> category
        duration
        size
        count
Output?
    '{"category": %s, "duration": %s, "size": %s, "count": %s"}'
Plan:
    Create an instance of this class
    Feed it all the lines
    Call the print method

    removed from leftovers:
    ^/rest/api/2/issue/.*/editmeta.*\r\n
    /rest/tempo-timesheets/.*\r\n
    /rest/api/2/user\?username.*\r\n
    /rest/auth/1/session
    /rest/api/2/status
    /rest/api/latest/issue/.*/remotelink
    /rest/api/latest/user
    /rest/api/2/issue
"""