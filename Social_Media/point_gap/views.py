from django.shortcuts import render
from django.http import HttpResponse
from . import models
from rest_framework.request import Request
from rest_framework.decorators import api_view
from django.shortcuts import redirect, render,get_object_or_404
from . import serialiazers
from rest_framework.response import Response
from rest_framework import status,viewsets
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User
from . import forms
from django.contrib.auth.decorators import login_required
from taggit.models import Tag
from django.core.paginator import Paginator


def index(request,tag_slug=None):
    if tag_slug:
        tag = get_object_or_404(Tag,slug = tag_slug)
        post = models.Post.objects.filter(status = 'published',tag__in = [tag,])
    else:
    
        post = models.Post.objects.filter(status = 'published')
    query = {
        'page_obj':post,
    }
    paginator_v = Paginator(post,3)
    page_number = request.GET.get("page")
    page_obj = paginator_v.get_page(page_number)
    return render(request,'index.html',{"page_obj": page_obj})



def post_detail(request,id,title):
    post = get_object_or_404(models.Post,id  = id , title = title,status = 'published')
    query = {
        'post':post,
    }
    return render(request,'detail.html',query)
#serialiaze
class Api_view(viewsets.ModelViewSet):
    queryset = models.Post.objects.all()
    serializer_class = serialiazers.Serialiaze_M
#--------------------------------
def logup_m(request):
    if request.method == 'POST':
        form_m = forms.Logup_Form(request.POST)
        if form_m.is_valid():
            cd = form_m.cleaned_data
            user = User.objects.create_user(username=cd['username'],password=cd['your_password'],email=cd['email'])
            user.first_name = cd['first_name']
            user.last_name = cd['last_name']
            user.save()
            return redirect('index')
    else:
        form_m = forms.Logup_Form()
    return render(request,'logup.html',{'form':form_m})





#--------------------------------

def profile(request):
    user = request.user
    return render(request,'profile.html',{'user':user})

def addpost(request,n=None):
    user = request.user
    print(user)
    if request.method == 'POST':
        form_post = forms.Add_Post(request.POST)
        if form_post.is_valid():
            form_post.save()
            return redirect('prof')
    else:
        form_post = forms.Add_Post()
# if user:

# else:
#     return HttpResponse('you have to login!!!')
    return render(request,'addpost.html',{'form':form_post})


def login_a(request):
    if request.method == 'POST':
        form = forms.Login_Form(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,username=cd['username'],password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request,user)
                    return redirect('index')
                else:
                    return HttpResponse('user is not active!')
            else:
                return HttpResponse('user is None!')
    else:
        form = forms.Login_Form()
    return render(request,'login.html',{'form':form})

def logout_a(request):
    logout(request)
    return redirect('index')

@login_required(login_url='index')
def changepassword(request):
    if request.method == 'POST':
        user = request.user
        form = forms.ChangePassword(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            check_password = cd['old_password']
            new_password1 = cd['new_password1']
            new_password2 = cd['new_password2']
            if not user.check_password(check_password):
                return HttpResponse('Warning!!!...old password is false')
            elif new_password1 != new_password2:
                return HttpResponse('New passwords is not equals!!!')
            else :
                user.set_password(new_password1)
                user.save()
                return HttpResponse('Change password done!')
    else:
        form = forms.ChangePassword()
    return render(request,'Changepassword.html',{'form':form})



        
