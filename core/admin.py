from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from .models import *
#admin.site.register(Post)
 
class PostAdmin(SummernoteModelAdmin):
    list_display = ('title', 'slug', 'intro','date_added')
    search_fields = ['title', 'body']
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('body',)

class BioAdmin(SummernoteModelAdmin):
    list_display = ('title', 'slug', 'intro','date_added')
    search_fields = ['title', 'body']
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('body',)

class FlashAdmin(SummernoteModelAdmin):
    list_display = ('title', 'slug', 'intro','date_added')
    search_fields = ['title', 'body']
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('body',)

class CommuniqueAdmin(SummernoteModelAdmin):
    list_display = ('title', 'slug', 'intro','date_added')
    search_fields = ['title', 'body']
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('body',)

class AgendaAdmin(SummernoteModelAdmin):
    list_display = ('title', 'slug', 'intro','date_added')
    search_fields = ['title', 'body']
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('body',)


class PublicationAdmin(SummernoteModelAdmin):
    list_display = ('title', 'slug', 'intro','date_added')
    search_fields = ['title', 'body']
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('body',)

class ActualiteAdmin(SummernoteModelAdmin):
    list_display = ('title', 'slug', 'intro','date_added')
    search_fields = ['title', 'body']
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('body',)

class ConjonctureAdmin(SummernoteModelAdmin):
    list_display = ('title', 'source', 'slug', 'intro','date_added')
    search_fields = ['title', 'body']
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('body',)


admin.site.register(Actualite, ActualiteAdmin)
admin.site.register(Publication, PublicationAdmin)
admin.site.register(Agenda, AgendaAdmin)
admin.site.register(Communique, CommuniqueAdmin)
admin.site.register(Flash, FlashAdmin)
admin.site.register(Bio, BioAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Rubrique)
admin.site.register(Conjoncture, ConjonctureAdmin)
