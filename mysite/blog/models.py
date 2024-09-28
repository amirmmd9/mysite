from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
class Post(models.Model):
    STATUS_D = (
        ('draft','Draft'),
        ('published','Published'),
    )
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name="user_model1",null=True)
    pic_author = models.ImageField(upload_to='upload_author/',null=True)
    title = models.CharField(max_length=25,unique=True)
    slug = models.SlugField(max_length=25,unique=True)
    body = models.TextField()
    status = models.CharField(max_length=10,choices=STATUS_D,default='draft')
    pic = models.ImageField(upload_to='upload/',null=True)
    created = models.DateTimeField(auto_now_add=True,null=True)
    updated = models.DateTimeField(auto_now=True,null=True)
    def get_absolute_url(self):
        return reverse("detailes",args=[self.slug,self.id])
    def active_comment(self):
        return self.comment_user.filter(active = True)
    
class khadamat(models.Model):
    STATUS = (
        ('draft','Draft'),
        ('published','Published'),
    )
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name="user_model2",null=True)
    name = models.CharField(max_length=25,unique=True)
    text = models.TextField()
    slug = models.SlugField(max_length=25,unique=True)
    status = models.CharField(max_length=10,choices=STATUS,default='draft')
    def get_url(self):
        return reverse("khedmat",args=[self.slug,self.id,self.name])

class maghalat(models.Model):
    STATUS = (
        ('draft','Draft'),
        ('published','Published'),
    )
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name="user_model3",null=True)
    name = models.CharField(max_length=25,unique=True)
    text = models.TextField()
    slug = models.SlugField(max_length=25,unique=True)
    status = models.CharField(max_length=10,choices=STATUS,default='draft')
    def get_url_m(self):
        return reverse("maghale_detail",args=[self.slug,self.id,self.name])

class model_comment(models.Model):
    post = models.ForeignKey(Post,models.CASCADE,related_name='comment_user',null=True)
# name = models.CharField(max_length=25,null=True)
    comment = models.TextField()
    active = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True,null=True)
    def __str__(self):
        return "{0}".format(self.comment)
