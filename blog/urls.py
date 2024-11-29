from blog.views import *
from django.urls import path 


urlpatterns = [
    path("blog", blog , name="blog"),
   
]