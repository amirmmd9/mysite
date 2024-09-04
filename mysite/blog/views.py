from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from . import models
from . import forms
from django.contrib.auth import login,logout,authenticate

def index(request):
    post = models.Post.objects.filter(status = 'published')
    khedmat = models.khadamat.objects.filter(status = 'published')
    mmd={
        "post":post,
        "khedmat":khedmat,
    }
    return render(request,"index.html",context=mmd)

def detailes(request,slug,id):
    post = get_object_or_404(models.Post,slug=slug,id=id,status='published')
    comment = models.model_comment.objects.filter(post=post)
    new_comment = None
    comment_form = forms.Comment_Form()
    if request.method == 'POST':
        comment_form = forms.Comment_Form(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
    amir={
        "post":post,
        'new_comment':new_comment,
        'comment_form':comment_form,
        'comment':comment,
    }
    return render(request,'detailes.html',context=amir)

def khedmat(request,slug,id,name):
    amir2 = get_object_or_404(models.khadamat,slug=slug,id=id,name=name,status='published')
    dd={
        "amir2":amir2,
    }
    return render(request,'khedmat.html',context=dd)

def about(request):
    return render(request,"about.html")

def log_in_and_join(request):
    if request.method == 'POST':
        form = forms.Log_in(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,username=cd['username'],password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request,user)
                    return redirect('index')
                else:
                    return HttpResponse('شما اکانت فعال ندارید')
            else:
                return HttpResponse('اکانت شما موجود نمی باشد')
    else:
        form = forms.Log_in()
    return render(request,'login_join.html',{'form':form})

def logout_view(request):
    logout(request)
    return redirect('index')

def rezome(request):
    return render(request,"rezome.html")

def maghale(request):
    post = models.maghalat.objects.filter(status = 'published')
    return render(request,"maghale.html",{'post':post})


def maghale_detail(request,slug,id,name):
    post_model = get_object_or_404(models.maghalat,slug=slug,id=id,name=name,status='published')
    con={
        'post':post_model
    }
    return render(request,"maghale_detail.html",context=con)