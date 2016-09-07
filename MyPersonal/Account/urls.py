# -*- coding:utf-8 -*-
from django.conf.urls import url
from .views import login_views, register, Management, Article_new

urlpatterns = [
    url(r'^login/', login_views, name='login'),
    url(r'^register/', register, name='register'),
    url(r'^user',Management, name='user'),
    url(r'^new_Article', Article_new, name='new'),
]