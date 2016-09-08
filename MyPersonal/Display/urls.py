# -*- coding:utf-8 -*-
from django.conf.urls import url
from .views import index, show_Article_content
app_name= 'Display'
urlpatterns = [
    url(r'^$', index,name='index'),
    url(r'^index', index,name='index'),
    url(r'^a/(\d{4})?$', show_Article_content, name='a')
]
