from django.shortcuts import render , redirect 
from blog.models import Post

# Create your views here.

def blog_home(request):
    posts = Post.objects.filter(status=1)
    context = {'posts':posts}
    return render(request, "blog/blog-home.html",context)

def blog_single(request):
    return render(request, "blog/blog-single.html")

def test(request):
    posts = Post.objects.all() # Query to data base and get all we can also use get , filter 
    #posts = Post.objects.filter(status=1) # it means if post was published then we display it to screen other wise if status=0 it not gonna show those since they are not published
    context = {'posts':posts} # use context and use a variable 'posts' and equal to our posts and then we use it inside the template for display
    return render(request,"test.html" , context)