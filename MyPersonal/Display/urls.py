# -*- coding:utf-8 -*-
from django.conf.urls import url
from .views import index, show_Article_content

urlpatterns = [
    url(r'^$', index,name='index'),
    url(r'^a/(\d{4})?$', show_Article_content, name='a')
]
