from django.views.generic import ListView, DetailView

from issuetracking.models import Project, Issue


class ProjectMixin(object):
    model = Project


class IssueMixin(object):
    model = Issue


class ProjectListView(ProjectMixin, ListView):
    context_object_name = "project_list"


class ProjectDetailView(ProjectMixin, DetailView):
    context_object_name = "project"


class IssueDetailView(IssueMixin, DetailView):
    context_object_name = "issue"
