# -*- coding:utf-8 -*-

from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponse
from django.views.generic.detail import DetailView
from django.utils import timezone
import time
from Admin.models import Tags,Posts
from django.core.paginator import PageNotAnInteger, Paginator, EmptyPage


def my_custom_page_not_found_view(request):
    return render_to_response('404.html')


def my_custom_permission_denied_view(request):
    return render_to_response('403.html')


def my_custom_error_view(request):
    return render_to_response('500.html')

# Create your views here


def index(request):
    try:
        posts = Posts.objects.all().order_by('-publish_date')
        tags = posts[0].tags.all()
        paginator = Paginator(posts, 4)
        page = request.GET.get('page')
        try:
            contacts = paginator.page(page)
        except PageNotAnInteger:
            contacts = paginator.page(1)
        except EmptyPage:
            contacts = paginator.page(paginator.num_pages)
        return render(request, 'blog_index.html', {'contacts': contacts, 'tags': tags})
    except:
        return render(request, 'blog_index.html')


def show_posts(request, slug):
    categories = Tags.objects.all()
    article = Posts.objects.get(slug=slug)
    tags = article.tags.all()
    count = article.readcount
    count += 1
    try:
        article.readcount = count
        article.save()
    except:
        pass
    author = article.author.username
    return render(request, 'blog_post.html', {'article': article, 'tags': tags, 'author': author, 'categories': categories})


def about_me(request):
    return render(request,'about_me.html')


def about_the_web(request):
    return HttpResponse('test')

