from __future__ import unicode_literals

from django.db import models

# Create your models here.

class ProfileImage(models.Model):
    name = models.CharField(max_length=200)
    datetiem = models.DateTimeField()
    image = models.FileField(upload_to='profile/%Y%m%d')
