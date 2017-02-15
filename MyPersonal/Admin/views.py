# -*- coding:utf-8 -*-
import json
import time
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, logout,login
from django.contrib.auth.views import login
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.contrib.auth.hashers import make_password
import time
from About.models import About
from django.contrib import messages
from django.core.exceptions import  ObjectDoesNotExist
from .models import Tags, Posts
from django.db import IntegrityError
from django.views.generic import RedirectView
from django.db import connection

# Create your views here.

@login_required
def about_edit(request):
    try:
        #使用原始SQL语句获取
        cursor = connection.cursor()
        cursor.execute("SELECT id  FROM About_about ")
        about_id = cursor.fetchall()
        if about_id:
            cursor.execute("SELECT Introduction FROM About_about WHERE id=%s", [about_id])
            about_info = cursor.fetchall()[0]

        if request.method == 'POST':
            Introduction = request.POST['Introduction']
            try:
                if about_id:
                    cursor.execute("UPDATE About_about SET Introduction = %s WHERE id=%s", [Introduction, about_id])
                    messages.success(request, "更新完成")
                else:
                    About.objects.create(Introduction=Introduction)
                    messages.success(request,"创建完成")
                return JsonResponse(request, {'status':'success'})
            except:
                return JsonResponse(request, {'status':'error','message':"出错啦"})

    #return HttpResponse(about_info)
        else:
            return render(request, 'edit_about.html', {'about_info':about_info[0]})
    except:
        return render(request, 'edit_about.html')
        #return HttpResponse("error")





class LogoutViews(RedirectView):
    url = '/'

    def get(self, request, *args, **kwargs):
        logout(request)
        return super(LogoutViews, self).get(request, *args, **kwargs)

def login_views(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/admin/posts')
    else:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user_status = authenticate(username=username, password=password)
            if user_status:
                login(request,user_status)
                messages.success(request, "欢迎回来")
                return JsonResponse({'url': '/admin/posts', 'status': 'success'})
            else:
                if User.objects.filter(username=username):
                    return JsonResponse({'message': "密码错误", 'status': 'error'})
                else:
                    return JsonResponse({'status': 'error','message': "用户不存在"})
        return render(request, 'login.html')


def register(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect(post_index)
    else:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            password_confirm = request.POST['password_confirm']
            email = request.POST['email']

            if password == password_confirm:
                username_status = User.objects.filter(username=username)
                if username_status:
                    return JsonResponse({'status': 'error', 'message': "用户名已经存在"})
                else:
                    try:
                        User.objects.create(username=username,email=email,
                                            password=make_password(password_confirm))
                        messages.success(request, "注册成功，请登陆！")
                        return JsonResponse({'status': 'success', 'url': '/admin/login/'})
                    except:
                        messages.error(request,"错了，不是你的问题，是我，是我。排查中…………………………")
            else:
                return JsonResponse({'status': 'error', 'message': "两次密码不一致"})
        admin_status = User.objects.all()
        if admin_status:
            messages.warning(request, "这个房间已经有人了，不能给你钥匙！～！")
        return render(request, 'register.html')


@login_required
def post_index(request):
    try:
        posts = Posts.objects.all()
        tags = posts[0].tags.all()
        return render(request, 'posts_index.html', {'posts': posts, 'tags': tags})
    except:
        return render(request, 'posts_index.html')


@login_required
def post_edit(request,id):
    if request.method == 'POST':
        method = request.POST['_method']
        post_id = id
        if method == 'DELETE':
            post_name = Posts.objects.get(id=post_id)
            del_status = Posts.objects.get(id=post_id).delete()
            if del_status:
                messages.success(request, "The '" + post_name.title + "' posts has been deleted.")
                return HttpResponseRedirect('/admin/posts')
        elif method == 'PUT':
            userid = request.user.id
            title = request.POST['title']
            content = request.POST['content']
            tag = request.POST['tags']
            slug = request.POST['slug']

            update_status = posts_update(id, title, content, userid, tag, slug)
            if update_status:
                messages.success(request, "The '" + title + "' posts has been updated.")
                return JsonResponse({'status': 'success', 'url': '/admin/posts'})
            else:
                return JsonResponse({'status': 'error', 'message': "数据库君可能心情不好，要不你在检查检查"})
    post = Posts.objects.get(id=id)
    tags = post.tags.all()
    return render(request, 'posts_edit.html', {'post': post, "tags": tags})


@login_required
def post_create(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        tags = request.POST['tags']

        try:
            # 处理tags
            tags_id_status= Tags.objects.get(tag=tags)
            tags_id = tags_id_status.id
        except ObjectDoesNotExist:
            tags_save_status = Tags(tag=tags)
            tags_save_status.save()
            tags_id = tags_save_status.id
        slug = request.POST['slug']
        date = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
        try:
            post = Posts(title=title, content=content, publish_date=date,
                         readcount=0, author_id=request.user.id, slug=slug)
            post.save()
            post.tags.add(Tags.objects.get(id=tags_id))
            post.save()
            messages.success(request, "文章创建成功")
            return JsonResponse({'status': 'success', 'url': '/admin/posts'})
        except IntegrityError:
                return JsonResponse({'status': 'error', 'message': "请检查标题或者slug是否重复了"})
        except:
            return JsonResponse({'status':'error', 'message':"出错啦！！！"})

    tags = Tags.objects.all()
    return render(request, "posts_create.html", {'tags': tags})


# tags
@login_required
def tag_index(request):
    tags = Tags.objects.all()
    return render(request,'tags_index.html',{'tags': tags})


@login_required
def create_tags(request):
    if request.method == 'POST':
        tags = request.POST['tags']
        meta_description = request.POST['meta_description']

        object_status = Tags.objects.create(tag = tags,meta_description=meta_description)
        if object_status:
            messages.success(request, "The tag '" +tags+ "' was created.")
            return HttpResponseRedirect('/admin/tags/')
    else:
        return render(request,'tags_create.html')


@login_required
def edit_tags(request, id):
    if request.method == "POST":
        method = request.POST['_method']
        tags_id = id
        if method == 'DELETE':
            tags_name = Tags.objects.get(id=tags_id)
            del_status = Tags.objects.get(id=tags_id).delete()
            if del_status:
                messages.success(request, "The '"+tags_name.tag+"' tag has been deleted.")
                return HttpResponseRedirect('/admin/tags/')
        elif method == 'PUT':

            tag = request.POST['tag']
            meta_description = request.POST['meta_description']
            update_status = tags_update(tags_id, tag, meta_description)
            if update_status:
                messages.success(request, "The '" + tag + "' tag has been updated.")
                return HttpResponseRedirect('/admin/tags/')

    data = Tags.objects.get(id=id)
    return render(request, 'tags_edit.html', {'data':data})


def tags_update(tags_id, tag, meta):
    tags = Tags.objects.get(id=tags_id)

    tags.tag = tag
    tags.meta_description = meta
    tags.save()

    return True


def posts_update(id, title, content, userid, tag, slug):
    post = Posts.objects.get(id=id)# 获取文章标签并判断
    tags = post.tags.all()
    if tag in tags:
        post.title = title
        post.content = content
        post.author_id = userid
        post.slug = slug
        post.save()
    else:
        try:# 处理tags
            tags_id_status = Tags.objects.get(tag=tag)
            tags_id = tags_id_status.id
        except ObjectDoesNotExist:
            tags_save_status = Tags(tag=tag)
            tags_save_status.save()
            tags_id = tags_save_status.id

        post.title = title
        post.content = content
        post.author_id=userid
        post.slug = slug
        post.save()
        post.tags.add(Tags.objects.get(id=tags_id))
        post.save()

    return True


@login_required
def upload_index(request):
    return render(request, 'upload_index.html')


@login_required
def upload_files(request):
    files = request
