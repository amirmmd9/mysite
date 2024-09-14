from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from django.urls import reverse

class Post(models.Model):
    STATUS_CHOIES = (
        ('draft','Draft'),
        ('published','Published'),
    )
    user = models.ForeignKey(User,on_delete = models.CASCADE,related_name = 'users')
    title = models.CharField(max_length = 25)
    body = models.TextField()
    status = models.CharField(max_length = 10,choices=STATUS_CHOIES,default='draft')
    created = models.DateTimeField(auto_now_add=True,null=True)
    updated = models.DateTimeField(auto_now=True,null=True)
    slug  = models.CharField(max_length = 25,null = True)
    tag = TaggableManager()
    def __str__(self):
        return "{0} {1}".format(self.user,self.title)
    def get_absolute_url(self):
        return reverse('post_detail',args=[self.id,self.title])
    

