from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible

from django.db import models
# from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.

@python_2_unicode_compatible
class Bookmark(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    url = models.URLField('url', unique=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL)

    def __str__(self):
        return self.title
