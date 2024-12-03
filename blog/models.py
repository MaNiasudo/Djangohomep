from django.db import models
from taggit.managers import TaggableManager
from django.contrib.auth.models import User  # -> Imported Our User Model here for use
from django.urls import reverse



class Category(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name
    


class Post(models.Model):
    image = models.ImageField(upload_to='blog/',default='blog/default.jpg')
    author = models.ForeignKey(User , on_delete=models.CASCADE , null=True) #author -> related to User Model
    title = models.CharField(max_length=255)
    content = models.TextField()
    category = models.ManyToManyField(Category)
    #category -> need a category Model to relate to posts for the time we want to show posts have same categorys
    #tag -> need tag Model Like category
    tags = TaggableManager()
    counted_views = models.IntegerField(default=0) # after making database if we dont give a default value , an error gonna accour
    status = models.BooleanField(default=False) #status bolean -> for publishing if true  published if not true not published and we can use it to show only published posts
    published_date = models.DateTimeField(null=True)
    created_date = models.DateTimeField(auto_now_add=True) # -> save time when i create it
    updated_date = models.DateTimeField(auto_now=True) # -> save time when i update
    
    class Meta: # Meta classes do some action -> read more when needed https://docs.djangoproject.com/en/5.1/ref/models/options/
       ordering = ['-created_date'] # This works in our project too but if just do it in our admin section it dosent effect our data's Its general
       #verbos_name for change name to persian
       #verbos_name_plural for change group to a group name

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('blog:single', args=[str(self.id)])
    

class Comment(models.Model):
    post =models.ForeignKey(Post,on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True) 
    updated_date = models.DateTimeField(auto_now=True)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return self.subject