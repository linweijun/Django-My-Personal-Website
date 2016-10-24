# -*- coding:utf-8 -*-

from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from Admin.models import Tags,Posts
from django.core.mail import send_mail, BadHeaderError
from django.contrib import messages
from django.conf import settings
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
        q = len(tags)
        paginator = Paginator(posts, 4)
        page = request.GET.get('page')
        try:
            contacts = paginator.page(page)
        except PageNotAnInteger:
            contacts = paginator.page(1)
        except EmptyPage:
            contacts = paginator.page(paginator.num_pages)
        return render(request, 'blog_index.html', {'contacts': contacts})
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

def contact(request):
    if request.method == 'POST':
        send_email(request)
    return render(request, 'contact.html')

def about_me(request):
    return render(request,'about_me.html')


def about_the_web(request):
    return HttpResponse('test')



def send_email(request):
    message = request.POST['message']
    emails = request.POST['email']
    name = request.POST['name']
    message_html = ("<h1>THis is Contact email <br> <p> name:%s <br> email: %s <br> <p> <hr>%s")%(name, emails, message)

    if messages and emails and name:
        try:
            send_mail('from:Next Day messags', message_html, settings.EMAIL_HOST_USER, ['linweijun93315@gmail.com'], html_message=message_html)
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        messages.success(request, "Thinks your")
        return render(request, 'contact.html')
    else:
        messages.warning(request, 'Make sure all fields are entered and valid.')
        return render(request, 'contact.html')

