from django.contrib import admin
from home.models import *
# Register your models here.


class ContactAdmin(admin.ModelAdmin):
    pass

admin.site.register(Contact, ContactAdmin)