from . import models
from django import forms
#ثبت نام
# class Registeration(forms.Form):
#     first_name = forms.CharField(max_length=25,required=True)
#     last_name = forms.CharField(max_length=35,required=False)
#     user_name = forms.CharField(max_length=25,required=True)
#     phone = forms.CharField(max_length=11,required=False)
#     email = forms.EmailField(required=False)
#     password = forms.CharField(min_length=8,required=True)
#نا آماده
    
#ورود
class Log_in(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True)

#کامنت
class Comment_Form(forms.ModelForm):
    class Meta:
        model = models.model_comment
        fields = ('name','comment')

class ChangePassword(forms.Form):
    old_password = forms.CharField(widget=forms.PasswordInput)
    new_password1 = forms.CharField(widget=forms.PasswordInput)
    new_password2 = forms.CharField(widget=forms.PasswordInput)