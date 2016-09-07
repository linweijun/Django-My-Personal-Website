from django.shortcuts import render_to_response

def my_custom_page_not_found_view(request):
    return render_to_response('404.html')

def my_custom_permission_denied_view(request):
    return render_to_response('403.html')

def my_custom_error_view(request):
    return render_to_response('500.html')