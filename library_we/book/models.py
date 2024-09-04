from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from django.urls import reverse

class book(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='user1',null=True)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    published_date_book = models.CharField(max_length=100)
    exist = models.BooleanField(default=False)
    price = models.IntegerField(blank=True,null=True)
    genre = TaggableManager()
    def get_absolute_url(self):
        return reverse("detail",args=[self.id,self.title])
    
