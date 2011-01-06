from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User, Group

from taggit.managers import TaggableManager


class Project(models.Model):
    title = models.CharField(verbose_name=_("title"), max_length=100)
    slug = models.SlugField(verbose_name=_("slug"))
    subtitle = models.CharField(verbose_name=_("sub-title"), max_length=100, blank=True)
    description = models.TextField(verbose_name=_("description"), blank=True)
    group = models.ForeignKey(Group, verbose_name=_("user group"), related_name="projects")
    
    class Meta:
        verbose_name = _("project")
        verbose_name_plural = _("projects")
    
    def __unicode__(self):
        return u"%s" % (self.title,)


class Issue(models.Model):
    STATUS_NEW = 1
    STATUS_ASSIGNED = 2
    STATUS_RESOLVED = 3
    STATUS_CLOSED = 4
    STATUS_CHOICES = (
        (STATUS_NEW, _("new")),
        (STATUS_ASSIGNED, _("assigned")),
        (STATUS_RESOLVED, _("resolved")),
        (STATUS_CLOSED, _("closed")),
    )
    
    project = models.ForeignKey(Project, verbose_name=_("project"), related_name="issues")
    title = models.CharField(verbose_name=_("title"), max_length=255)
    description = models.TextField(verbose_name=_("description"), blank=True)
    status = models.PositiveSmallIntegerField(verbose_name=_("status"), choices=STATUS_CHOICES, default=STATUS_NEW)
    reported_by = models.ForeignKey(User, verbose_name=_("reported by"), related_name="reported_issues")
    assigned_to = models.ForeignKey(User, verbose_name=_("assigned to"), related_name="assigned_issues", blank=True, null=True)
    tags = TaggableManager()
    
    class Meta:
        verbose_name = _("issue")
        verbose_name_plural = _("issues")
    
    def __unicode__(self):
        return u"%s" % (self.title,)
    
    def save(self, *args, **kwargs):
        if self.status == self.STATUS_NEW and self.assigned_to:
            self.status = self.STATUS_ASSIGNED
        super(Issue, self).save(*args, **kwargs)
