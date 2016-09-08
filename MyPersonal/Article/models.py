# -*- coding:utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class A_Classics(models.Model):
    name = models.CharField(max_length=64, verbose_name='分类名')
    articecount = models.IntegerField()


    def __unicode__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=100, verbose_name='标题')
    content = models.TextField(verbose_name='正文')
    author = models.ForeignKey(User)
    tags = models.CharField(max_length=1024, verbose_name='标签', blank=True)
    classic = models.ForeignKey(A_Classics)
    publish_date = models.DateTimeField(verbose_name='发布时间')
    readcount = models.IntegerField(blank=True, verbose_name='阅读数')


    def __unicode__(self):
        return self.author, self.title,self.classic,self.content,self.readcount,self.publish_date,\
    self.tags



class Comment(models.Model):
    article = models.ForeignKey(Article)
    content = models.TextField()
    date = models.DateField()
    email = models.EmailField()
    commentator = models.TextField()

