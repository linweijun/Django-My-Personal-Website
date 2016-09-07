# -*- coding:utf-8 -*-
from django.conf.urls import url
from .views import login_views, register, Management

urlpatterns = [
    url(r'^login/', login_views, name='login'),
    url(r'^register/', register, name='register'),
    url(r'^user',Management, name='user')
]