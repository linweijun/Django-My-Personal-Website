# -*- coding:utf-8 -*-

from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from Admin.models import Tags,Posts
from django.contrib import messages
from django.views.generic import ListView, DetailView, FormView, TemplateView
from .forms import ContactForm
from django.contrib.messages.views import SuccessMessageMixin


def page_not_found_view(request):

    return render_to_response('handler.html',{'title': 'Not Found', 'error_number': '404',
                                              'content_head': 'Sorry but we couldn\'t find this page',
                                              'content': 'This page you are looking for does not exist.'})


def permission_denied_view(request):
    return render_to_response('handler.html',{'title': 'Permission Denied', 'error_number': '403',
                                              'content_head': 'Access denied',
                                              'content': 'Full authentication is required to access this resource.'})


def error_view(request):
    return render_to_response('handler.html',{'title': 'Internal Server Error', 'error_number':'500',
                                              'content_head': 'Internal Server Error',
                                              'content': 'We track these errors automatically, '
                                                         'but if the problem persists feel free to contact us.'})

# Create your views here


class IndexView(ListView):

    template_name = 'blog/blog_index.html'
    context_object_name = 'Article_list'
    paginate_by = 4

    def get_queryset(self):
        Article_list = Posts.objects.all().order_by('-publish_date')
        return Article_list


class ShowPostsViews(DetailView):

    model = Posts
    template_name = 'blog/blog_post.html'
    context_object_name = 'posts'
    slug_url_kwarg = 'slug'

    def get_context_data(self, **kwargs):
        kwargs['tags'] = self.object.tags.all()
        return super(ShowPostsViews, self).get_context_data(**kwargs)


class ContactViews(SuccessMessageMixin, FormView):

    template_name = 'contact.html'
    form_class = ContactForm
    success_url = '/contact/'
    success_message = 'Thinks your!'

    def form_valid(self, form):
        form.send_email()
        return super(ContactViews, self).form_valid(form)


def about_me(request):
    return render(request,'about_me.html')

