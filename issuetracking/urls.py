from django.conf.urls.defaults import patterns, url, include

from issuetracking.views import ProjectListView, ProjectDetailView, IssueDetailView


urlpatterns = patterns('',
    url(r'^', include(patterns('', 
        url(r'^$', ProjectListView.as_view(), name="project_list"),
        url(r'^(?P<slug>[^/]+)/$', ProjectDetailView.as_view(), name="project_detail"),
        url(r'^(?P<project_slug>[^/]+)/(?P<pk>\d+)/$', IssueDetailView.as_view(), name="issue_detail"),
    ), app_name="issuetracking", namespace="issuetracking"))
)
