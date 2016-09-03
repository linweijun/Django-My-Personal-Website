# -*- coding:utf-8 -*-
from django.conf.urls import url
from .views import login_views, register

urlpatterns = [
    url(r'^$', login_views, name='login'),
    url(r'^register', register, name='register')
]