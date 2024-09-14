from django.contrib import admin
from . import models

class Post_Admin(admin.ModelAdmin):
    list_display = ('user','title','status')
    list_filter = ('title',)
    list_editable = ('status',)
    search_fields = ('title',)

admin.site.register(models.Post,Post_Admin)
