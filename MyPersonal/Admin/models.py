# -*- coding:utf-8 -*-

from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
@python_2_unicode_compatible
class Tags(models.Model):
    tag = models.CharField(max_length=20,unique=True)
    meta_description = models.CharField(max_length=64)
    articecount = models.IntegerField(default=0,blank=True)

    def __str__(self):
        return self.tag

@python_2_unicode_compatible
class Posts(models.Model):
    title = models.CharField('标题',max_length=254, unique=True)
    image = models.FileField(null=True,blank=True)
    content = models.TextField('正文')
    author = models.ForeignKey(User)
    tags = models.ManyToManyField(Tags)
    publish_date = models.DateTimeField('发布时间')
    readcount = models.IntegerField('阅读数',blank=True )
    slug = models.SlugField(unique=True)



    def __str__(self):
        return self.title
