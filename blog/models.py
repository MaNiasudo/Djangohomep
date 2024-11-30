from django.db import models
from django.contrib.auth.models import User  # -> Imported Our User Model here for use

class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    #author -> related to User Model
    #category -> need a category Model to relate to posts for the time we want to show posts have same categorys
    #image
    #tag -> need tag Model Like category
    counted_views = models.IntegerField(default=0) # after making database if we dont give a default value , an error gonna accour
    status = models.BooleanField(default=False) #status bolean -> for publishing if true  published if not true not published and we can use it to show only published posts
    published_date = models.DateTimeField(null=True)
    created_date = models.DateTimeField(auto_now_add=True) # -> save time when i create it
    updated_date = models.DateTimeField(auto_now=True) # -> save time when i update

    def __str__(self):
        return self.title