# -*- coding:utf-8 -*-
from django.conf.urls import url
from .views import login_views, logout_views, register, Management, Article_new
app_name = 'Account'
urlpatterns = [
    url(r'^$', login_views, name='login'),
    url(r'^login',login_views, name='login'),
    url(r'^logout$',logout_views, name='logout'),
    url(r'^register', register, name='register'),
    url(r'^user/([\w]+)$',Management, name='user'),
    url(r'^new_Article', Article_new, name='new'),
]