# -*- coding:utf-8 -*-
from django.conf.urls import url
from .views import login, register

urlpatterns = [
    url(r'^$', login, name='login'),
    url(r'^register', register, name='register')
]