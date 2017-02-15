# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-02-15 14:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=60)),
                ('Introduction', models.CharField(max_length=255)),
                ('Gender', models.BooleanField(default=1)),
                ('Desired_position', models.CharField(max_length=128)),
                ('Skills_list', models.TextField()),
                ('Create_time', models.DateTimeField(auto_now_add=True)),
                ('Edit_time', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]