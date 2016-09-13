# -*- coding:utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class dec_info(models.Model):
    userId = models.ForeignKey(User)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    b_day = models.DateTimeField()
    dec = models.TextField()


class tags(models.Model):
    # 技能标签
    userid = models.ForeignKey(User)
    tags_name = models.CharField(max_length=16)


class works(models.Model):
    # 作品
    userid = models.ForeignKey(User)
    works_name = models.CharField(max_length=100)
    works_url = models.URLField()
    works_decs = models.TextField()


class work_ex(models.Model):
    # 工作经历
    userid=models.ForeignKey(User)
    company_name = models.CharField(max_length=100)
    work_date = models.DateTimeField()
    work_Duty = models.TextField()