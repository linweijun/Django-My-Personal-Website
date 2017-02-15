from django.conf.urls import url
from .views import upload
urlpatterns =[
    url('^',upload, name='uploads')
]