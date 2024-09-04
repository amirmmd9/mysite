from django.shortcuts import render
from django.http import HttpResponse
from . import models
from django.shortcuts import redirect, render,get_object_or_404

def index(request):
    model = models.book.objects.all()
    con={
        'model':model,
    }
    return render(request,'index.html',context=con)

def detail(request,id,title):
    post = get_object_or_404(models.book,id=id,title=title)
    con={
        'post':post,
    }
    return render(request,'detail.html',context=con)
    
