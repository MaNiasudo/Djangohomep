from django.contrib import admin
from home.models import *
# Register your models here.


class ContactAdmin(admin.ModelAdmin):
    empty_value_display = "-empty-" 
    list_display = ["name", "email","subject","created_date"] # display this like a table row
    list_filter = ["email"] # make a filter list to chose from
    date_hierarchy = "created_date"

admin.site.register(Contact, ContactAdmin)# If dont add the ContactAdmin class here we not gonna see it on the admin page
admin.site.register(Newsletter)