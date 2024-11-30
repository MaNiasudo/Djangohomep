from django.contrib import admin
from blog.models import *

class PostAdmin(admin.ModelAdmin):
    empty_value_display = "-empty-"
    list_display = ["title", "status","created_date","updated_date","published_date"]

admin.site.register(Post, PostAdmin)