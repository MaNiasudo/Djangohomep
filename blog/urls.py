from blog.views import *
from django.urls import path 

app_name = 'blog' #This is for specifying our routes when we call them inside templates for example | blog:blog-home

urlpatterns = [
    path("", blog_home , name="blog-home"),
    path("single/", blog_single , name="blog-single"),
    path('test/',test,name='test')
   
]