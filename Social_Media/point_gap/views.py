from django.shortcuts import render
from django.http import HttpResponse
from . import models
from rest_framework.request import Request
from rest_framework.decorators import api_view
from django.shortcuts import redirect, render,get_object_or_404
from . import serialiazers
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import login,logout,authenticate
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
@api_view(['GET'])
def serialiaze_m(request : Request):
    obj = models.Post.objects.order_by('status').all()
    serialiaze_obj = serialiazers.Serialiaze_M(obj,many = True)
    return Response(serialiaze_obj.data,status.HTTP_200_OK)

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

        
