from django.contrib import admin
from blog.models import *

class PostAdmin(admin.ModelAdmin):
    empty_value_display = "-empty-" 
    list_display = ["title", "status","created_date","updated_date","published_date"] # display this like a table row
    list_filter = ["status"] # make a filter list to chose from
    date_hierarchy = "created_date" # give a selection on top of list that can chose a certain time
   # ordering = ["-created_date"]

admin.site.register(Post, PostAdmin) # admin.site.register(Post) THis is to just register the models here and other for admin features