from django import forms

class ProfileImageForm(forms.Form):
    image = forms.FileField(label='Select a profile Image')
    name = forms.CharField(max_length=20)