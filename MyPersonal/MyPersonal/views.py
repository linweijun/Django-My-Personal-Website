from django.shortcuts import render_to_response
from Article.models import Article
from django.http import HttpResponse

def my_custom_page_not_found_view(request):
    return render_to_response('404.html')

def my_custom_permission_denied_view(request):
    return render_to_response('403.html')

def my_custom_error_view(request):
    return render_to_response('500.html')

def urlU(request):
    slug = request.POST['slug']
    slug_status = Article.objects.get(slug=slug)
    if slug_status:
        return HttpResponse('error')
    else:
        return HttpResponse('success')


