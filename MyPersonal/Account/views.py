# -*- coding:utf-8 -*-
from django.shortcuts import render
from django.contrib.auth import authenticate, logout,login
from django.contrib.auth.models import User
from django.http import JsonResponse

# Create your views here.
def login_views(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user_status =authenticate(username=username, password=password)
        if user_status:
            login(request, user_status)
            return JsonResponse({'status':'success','message':'登入成功','url':'/'})
        else:
            if User.objects.filter(username=username):
                return JsonResponse({'status':'error', 'message':'密码错误'})
            else:
                return JsonResponse({'status':'error','message':'用户不存在'})
    return render(request, "sign_in.html")

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        password_confirm = request.POST['password_confirm']
        email = request.POST['email']

        
    return render(request, "sign_up.html")