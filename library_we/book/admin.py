from django.contrib import admin
from . import models

class Model_Book(admin.ModelAdmin):
    list_display=('title','author','exist')
    list_filter=('title','author','genre')
    search_fields=('title','author','genre')    
    list_editable=('exist',)

admin.site.register(models.book,Model_Book)
