# coding:utf-8
from django import forms
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.conf import settings


class ContactForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)

    def send_email(self):
        message = self.cleaned_data['message']
        name = self.cleaned_data['name']
        emails = self.cleaned_data['email']
        if message and emails and name:
            message_html = "<h1>THis is Contact email <br> <p> name:%s <br> email: %s <br> <p> <hr>%s" % (
                name, emails, message)
            try:
                send_mail('from:Next Day messags', message_html,
                          settings.EMAIL_HOST_USER, ['linweijun93315@gmail.com'],
                          html_message=message_html)
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            success_message = "Thinks Your!~"
            return success_message


