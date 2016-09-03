# -*- coding:utf-8 -*-
from django.shortcuts import render

# Create your views here.

def login(request):
    return render(request, "sign_in.html")

def register(request):
    return render(request, "sign_up.html")