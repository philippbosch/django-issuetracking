from django.contrib import admin

from issuetracking.models import Project, Issue


class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title",)
    prepopulated_fields = {"slug": ("title",)}


class IssueAdmin(admin.ModelAdmin):
    list_display = ("title", "status", "reported_by", "assigned_to",)
    list_filter = ("reported_by", "assigned_to",)


admin.site.register(Project, ProjectAdmin)
admin.site.register(Issue, IssueAdmin)
