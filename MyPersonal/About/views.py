# -*- coding:utf-8 -*-
from django.shortcuts import render
from .models import About


# Create your views here.
def about(request):
    about = About.objects.get(id=5)
    return render(request, 'about.html', {'about': about})
