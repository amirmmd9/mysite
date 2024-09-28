from . import models
from django import forms

class Login_Form(forms.Form):
    username = forms.CharField()
    password = forms.CharField()

class ChangePassword(forms.Form):
    old_password = forms.CharField()
    new_password1 = forms.CharField()
    new_password2 = forms.CharField()

class Logup_Form(forms.Form):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    username = forms.CharField(required=True)
    your_password = forms.CharField(required=True,widget=forms.PasswordInput,min_length=4)
class Add_Post(forms.ModelForm):
    class Meta:
        model = models.Post
        fields = "__all__"
#['title','body','status','created','updated','slug','tag']