# -*- coding:utf-8 -*-
from django.conf.urls import url
from .views import edit_tags, login_views, post_edit, LogoutViews, \
    upload_index, register, post_index, post_create, tag_index, create_tags,\
    about_edit
from django.contrib.auth import views as auth_views
app_name = 'Admin'
urlpatterns = [
    url(r'^$', login_views, name='login'),
    url(r'^login/$',login_views, name='login'),
    url(r'^logout/$',LogoutViews.as_view(), name='logout'),
    url(r'^register/$', register, name='register'),
    url(r'^posts$',post_index, name='posts'),
    url(r'^posts/([\d]+)/edit/$',post_edit, name="post_edit"),
    url(r'^posts/create/$', post_create, name='post_create'),
    url(r'^tags/$', tag_index, name='tags'),
    url(r'^create_tags',create_tags,name='create_tags'),
    url(r'^tags/([\d]+)/edit/',edit_tags, name='edit_tag'),
    url(r'^about/edit/', about_edit, name='about_edit'),
    url(r'^upload/$', upload_index, name='upload'),
]
