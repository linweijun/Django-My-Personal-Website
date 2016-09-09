from django.shortcuts import render
from django.http import HttpResponse
from Article.models import Article, A_Classics
import time

# Create your views here.

def index(request):
   return render(request, 'index.html')

def show_Article_content(request,id):
    return HttpResponse(id);
    #return render(request, "blog_item.html")
