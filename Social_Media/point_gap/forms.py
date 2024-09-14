from . import models
from django import forms

class Login_Form(forms.Form):
    username = forms.CharField()
    password = forms.CharField()

class ChangePassword(forms.Form):
    old_password = forms.CharField()
    new_password1 = forms.CharField()
    new_password2 = forms.CharField()