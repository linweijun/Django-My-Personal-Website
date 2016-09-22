# -*- coding:utf-8 -*-
from django.shortcuts import render, redirect, HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth import authenticate, logout,login
from django.contrib.auth.views import login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.contrib.auth.hashers import make_password
import time
from django.contrib import messages
from .models import Tags, Posts
# Create your views here.


def logout_views(request):
    logout(request)
    return HttpResponseRedirect("/index")

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
                login(request,user_status)
                return JsonResponse({'status':'success','message':'登入成功','url':'/'})
            else:
                if User.objects.filter(username=username):
                    return JsonResponse({'status':'error', 'message':'密码错误'})
                else:
                    return JsonResponse({'status':'error','message':'用户不存在'})
        return render(request, "login.html")

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
                return JsonResponse({'status':'success', 'message':'用户创建成功','url':'/account/login'})
        else:
            return JsonResponse({'status':'error', 'message':'两次密码不一致'})


    return render(request, "register.html")


def Post_index(request):
    posts = Posts.objects.all()
    tags = posts[0].tags.all()
    return  render(request, 'posts_index.html', {"posts":posts, 'tags':tags })

def Post_edit(request,id):
    if request.method == "POST":
        method = request.POST['_method']
        post_id = id
        if method == 'DELETE':
            del_status = Tags.objects.get(id=post_id).delete()
    post = Posts.objects.get(id=id)
    tags = post.tags.all()
    return render(request, 'posts_edit.html', {"post":post, "tags":tags })


def Post_create(request):
    if request.method == 'POST':
        userid = request.user.id
        title = request.POST['title']
        content = request.POST['content']
        tags = request.POST['tags']
        slug = request.POST['slug']
        date = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
        try:

            post = Posts(title=title, content=content,publish_date=date,
                                   readcount=0,author_id=userid,slug=slug)
            post.save()
            post.tags.add(Tags.objects.get(id=tags))
            post.save()


            if post:
                return JsonResponse({'status':'success', 'message':'文章保存成功'})
        except :
            return JsonResponse({'status':'error', 'message':'数据库君拒收～！请在检查检查！～'})
    tags = Tags.objects.all()
    return render(request, "posts_create.html", {"tags": tags})


# tags

def Tag_index(request):
    tags = Tags.objects.all()
    return render(request,'tags_index.html',{"tags": tags})

def create_tags(request):
    if request.method == 'POST':
        tags = request.POST['tags']
        meta_description = request.POST['meta_description']

        object_status = Tags.objects.create(tag = tags,meta_description=meta_description)
        if object_status:
            messages.success(request, "The tag '" +tags+ "' was created.")
            return HttpResponseRedirect("/admin/tags")
    else:
        return render(request,'tags_create.html')


def edit_tags(request, id):
    if request.method == "POST":
        method = request.POST['_method']
        tags_id = id
        if method == 'DELETE':

            tags_name = Tags.objects.get(id=tags_id)
            del_status = Tags.objects.get(id=tags_id).delete()
            if del_status:
                messages.success(request, "The '"+tags_name.tag+"' tag has been deleted.")
                return HttpResponseRedirect("/admin/tags")
        elif method == 'PUT':

            tag = request.POST['tag']
            meta_description = request.POST['meta_description']
            update_status = tags_update(tags_id, tag, meta_description)
            if update_status:
                messages.success(request, "The '" + tag + "' tag has been updated.")
                return HttpResponseRedirect("/admin/tags")

    data = Tags.objects.get(id=id)
    return render(request, 'tags_edit.html', {'data':data})

def tags_update(id,tag,meta):
    p = Tags.objects.get(id=id)

    p.tag = tag
    p.meta_description = meta
    p.save()

    return True


def upload_index(request):
    return render(request, 'upload_index.html')

def upload_files(request):
    files = request


