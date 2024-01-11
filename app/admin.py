from django.contrib import admin

# Register your models here.

from .models import *


class WebpageAdminView(admin.ModelAdmin):
    # values for class members can be provided in the form of list[] or tuple().
    
    # list_display=['name','topic_name']
    pass
    
    
    # list_display = ['topic_name','name','url','email']
    
    # list_display_links = ('name',)
    # # list_editable = ('name',)       #The value of 'name' cannot be in both 'list_editable' and 'list_display_links'.
    # list_editable = ['email']
    
    # # list_per_page = 1
    # search_fields = ('name','email')
    # list_filter = ['name','email']
    
    
class AccessRecordAdminView(admin.ModelAdmin):
    # values for class members can be provided in the form of list[] or tuple().

    list_display = ['name','author','date']
    
    list_display_links = ('author',)
    # list_editable = ('author',)     # The value of 'author' cannot be in both 'list_editable' and 'list_display_links'.
    list_editable = ('date',)
    
    list_per_page = 1
    search_fields = ['author']
    list_filter = ('date','author')


admin.site.register(Topic)
admin.site.register(Webpage,WebpageAdminView)
admin.site.register(AccessRecord,AccessRecordAdminView)


admin.site.site_title = 'Dude'
admin.site.site_header = 'HEIST'
admin.site.index_title = 'HHHHHHHHHH'