from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from Article.models import Article, A_Classics
from django.views.generic.detail import DetailView
from django.utils import timezone
import time

# Create your views here.

def index(request):
    Categories = A_Classics.objects.all()
    ArticleList = Article.objects.all()
    return render(request, 'index.html',{'ArticleList':ArticleList, 'Categories':Categories})

def show_Ariticle_Deta(request, slug):
    Article_Deta = Article.objects.get(slug=slug)
    author = Article_Deta.author.username
    return render(request, 'blog_item.html', {'Article_Deta':Article_Deta, 'author':author})