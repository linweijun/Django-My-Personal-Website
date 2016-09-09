# -*- coding:utf-8 -*-
from django.conf.urls import url
from .views import index, show_Ariticle_Deta
app_name= 'Display'
urlpatterns = [
    url(r'^$', index,name='index'),
    url(r'^index', index,name='index'),
    url(r'^a/(?P<slug>[\w]+)/$', show_Ariticle_Deta, name='a')
]
