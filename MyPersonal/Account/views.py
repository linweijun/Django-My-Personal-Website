# -*- coding:utf-8 -*-
from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, logout,login
from django.contrib.auth.views import login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.contrib.auth.hashers import make_password
import time
from Article.models import Article
# Create your views here.


def logout_views(request):
    logout(request)

def login_views(request):
    if request.user.is_authenticated:
        username = request.user.username
        url = "/account/user/" + username
        return HttpResponseRedirect(url)

    else:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']

            user_status =authenticate(username=username, password=password)
            if user_status:
                login(request, '')
                login(request,user_status)
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
def Management(request,id):
    content = User.objects.get(username = id)

    return render(request, "account_base.html", {'content':content})

@login_required
def Article_new(request):
    if request.method == 'POST':
        userid = request.user.id
        title = request.POST['title']
        content = request.POST['content']
        tags = request.POST['tags']
        classic = request.POST['classic']
        date = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
        try:
            status = Article.objects.create(title=title, content=content,
                                   tags=tags,publish_date=date,
                                   readcount=0,author_id=userid,classic_id=1)
            if status:
                return JsonResponse({'status':'success', 'message':'文章保存成功'})
        except :
                return JsonResponse({'status':'error', 'message':'数据库君拒收～！请在检查检查！～'})
    return render(request, "article_new.html")
