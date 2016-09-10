# -*- coding:utf-8 -*-
from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
@python_2_unicode_compatible
class A_Classics(models.Model):
    name = models.CharField(max_length=64, verbose_name='分类名')
    articecount = models.IntegerField()

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=100, unique=True,verbose_name='标题')
    content = models.TextField(verbose_name='正文')
    author = models.ForeignKey(User)
    tags = models.CharField(max_length=1024, verbose_name='标签', blank=True)
    classic = models.ForeignKey(A_Classics)
    publish_date = models.DateTimeField(verbose_name='发布时间')
    readcount = models.IntegerField(blank=True, verbose_name='阅读数')
    slug = models.SlugField(unique=True)


    def __repr__(self):
        p = []
        p.append(self.readcount)
        p.append(self.content)
        return p

@python_2_unicode_compatible
class Comment(models.Model):
    article = models.ForeignKey(Article)
    content = models.TextField()
    date = models.DateField()
    email = models.EmailField()
    commentator = models.TextField()

    def __str__(self):
        return self.content, self.date, self.email,self.commentator


