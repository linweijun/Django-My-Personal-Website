# -*- coding:utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from .forms import ProfileImageForm
from django.utils import timezone
from .models import ProfileImage


def upload(request):
    if request.method == 'POST':
        form = ProfileImageForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = ProfileImage(image=request.FILES['image'],name=request.POST['name'],datetiem=timezone.now())
            newdoc.save()

            return HttpResponseRedirect('/')
    else:
        doc = ProfileImage.objects.all()

        return render(request, 'upload.html',{'doc':doc})