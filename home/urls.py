from home.views import *
from django.urls import path 

app_name = 'website'

urlpatterns = [
    path("", home , name="home"),
    path("about/", about , name="about"),
    path("contact/", contact , name="contact"),
    path('test',testview,name='test')
   
]