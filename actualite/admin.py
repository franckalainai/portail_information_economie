from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from .models import *
#admin.site.register(Post)
 
class ActualiteAdmin(SummernoteModelAdmin):
    list_display = ('title', 'slug', 'intro','date_added')
    search_fields = ['title', 'body']
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('body',)
  
admin.site.register(Actualite, ActualiteAdmin)