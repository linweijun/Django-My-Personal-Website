from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, "index.html")

def show_Article_content(request,id):
    return render(request, "blog_item.html")
