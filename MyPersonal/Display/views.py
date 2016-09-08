from django.shortcuts import render
from django.http import HttpResponse
import time

# Create your views here.

def index(request):
    #tim = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    #return HttpResponse(tim)
    userid = request.user.id
    #return render(request, 'index.html')
    return HttpResponse(userid)

def show_Article_content(request,id):
    return HttpResponse(id);
    #return render(request, "blog_item.html")
