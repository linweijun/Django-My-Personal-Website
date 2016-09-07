# -*- coding:utf-8 -*-
from django.shortcuts import render
from django.contrib.auth import authenticate, logout,login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.contrib.auth.hashers import make_password
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

        if password == password_confirm:
            username_status = User.objects.filter(username=username)
            if username_status:
                return JsonResponse({'status':'error','message':'用户名已经存在'})
            else:
                try:
                    User.objects.create(username=username,email=email,password=make_password(password_confirm))
                except:
                    pass
                return JsonResponse({'status':'success', 'message':'用户创建成功'})
        else:
            return JsonResponse({'status':'error', 'message':'两次密码不一致'})


    return render(request, "sign_up.html")
@login_required
def Management(request):
    return render(request, "account_base.html")


def Article_new(request):
    return render(request, "article_new.html")
