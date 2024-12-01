from blog.views import *
from django.urls import path 

app_name = 'blog' #This is for specifying our routes when we call them inside templates for example | blog:blog-home

urlpatterns = [
    path("", blog_home , name="blog-home"),
    path("<int:pid>", blog_single , name="single"), # we want to use id=pid to get redirected to actuall post page , and we can {% url 'blog:single' pid=post.id %} do this in our template to render pages
    #path('test/post-<int:pid>/',test,name='test')
   
]