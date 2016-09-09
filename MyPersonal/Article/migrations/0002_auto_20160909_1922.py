# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-09 19:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Article', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='slug',
            field=models.CharField(blank=True, max_length=20, unique=True, verbose_name='\u6587\u7ae0url\u6807\u8bc6'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=100, unique=True, verbose_name='\u6807\u9898'),
        ),
    ]
