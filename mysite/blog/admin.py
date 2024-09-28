from django.contrib import admin
from . import models

class AdminPost(admin.ModelAdmin):
    list_display = ('title','slug','status')
    list_editable = ('status',)
    list_filter = ('title',)
    search_fields = ('title',)

admin.site.register(models.Post,AdminPost)
#----------
class Adminkedmat(admin.ModelAdmin):
    list_display = ('name','slug','status')
    list_editable = ('status',)
    list_filter = ('name',)
    search_fields = ('name',)
admin.site.register(models.khadamat,Adminkedmat)
#------------------------
class Admin_magh(admin.ModelAdmin):
    list_display = ('name','slug','status','author')
    list_editable = ('status',)
    list_filter = ('name',)
    search_fields = ('name',)
admin.site.register(models.maghalat,Admin_magh)
#-----------------------------------------
class Admin_comment(admin.ModelAdmin):
    list_display = ('post','active')
    list_editable =('active',)
# list_filter = ('name',)
# search_fields = ('name',)
admin.site.register(models.model_comment,Admin_comment)