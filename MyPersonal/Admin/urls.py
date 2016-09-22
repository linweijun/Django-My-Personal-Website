# -*- coding:utf-8 -*-
from django.conf.urls import url
from .views import edit_tags, login_views, Post_edit, logout_views, upload_index, register, Post_index, Post_create, Tag_index, create_tags
app_name = 'Admin'
urlpatterns = [
    url(r'^$', login_views, name='login'),
    url(r'^login',login_views, name='login'),
    url(r'^logout$',logout_views, name='logout'),
    url(r'^register', register, name='register'),
    url(r'^posts/$',Post_index, name='posts'),
    url(r'^posts/([\d]+)/edit',Post_edit, name="post_edit"),
    url(r'^posts/create$', Post_create, name='post_create'),
    url(r'^tags/$', Tag_index, name='tags'),
    url(r'^create_tags',create_tags,name='create_tags'),
    url(r'^tags/([\d]+)/edit/',edit_tags, name='edit_tag'),
    url(r'^upload/$', upload_index, name='upload'),
]