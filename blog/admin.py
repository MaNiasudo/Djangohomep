from django.contrib import admin
from blog.models import *
from django_summernote.admin import SummernoteModelAdmin

class PostAdmin(SummernoteModelAdmin):
    empty_value_display = "-empty-" 
    list_display = ["title", "author", "status","created_date","updated_date","published_date"] # display this like a table row
    list_filter = ["status"] # make a filter list to chose from
    date_hierarchy = "created_date" # give a selection on top of list that can chose a certain time
   # ordering = ["-created_date"]
    summernote_fields = ('content',)

class CommentAdmin(admin.ModelAdmin):
    list_display = ["name","subject","email","created_date","approved"]
    list_filter = ["email"]


admin.site.register(Post, PostAdmin) # admin.site.register(Post) THis is to just register the models here and other for admin features
admin.site.register(Category)   
admin.site.register(Comment ,CommentAdmin)