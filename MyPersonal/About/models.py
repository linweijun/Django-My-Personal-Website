# -*- coding=utf-8 -*-
from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.db import models
# Create your models here.

class About(models.Model):
    Name = models.CharField(max_length=60)
    Introduction = models.CharField(max_length=255)
    Gender = models.BooleanField(default=1)
    Desired_position = models.CharField(max_length=128)
    Skills_list = models.TextField()
    Create_time = models.DateTimeField(auto_now_add=True)
    Edit_time = models.DateTimeField(auto_now=True)
