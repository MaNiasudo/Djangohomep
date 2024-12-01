from django.shortcuts import render , redirect , get_object_or_404
from blog.models import Post

# Create your views here.

def blog_home(request):
    posts = Post.objects.filter(status=1)
    context = {'posts':posts}
    return render(request, "blog/blog-home.html",context)

def blog_single(request,pid):
    post = get_object_or_404(Post,id=pid,status=1)# with status = 1 users can only access to published posts  
    context = {'post':post}
    return render(request, "blog/blog-single.html", context)

def blog_category(request,cat_name):
    posts = Post.objects.filter(status=1)
    posts = posts.filter(category__name=cat_name) # we cant use single category here becvasue it look at id's and if we want to check name we need use category__name or any other variable we need
    context = {'posts':posts}
    return render(request, "blog/blog-home.html",context)











def test(request): #we can use pid to take only a single paramether out for example 1 post for display instead of taking everything out
   # posts = get_object_or_404(Post,id=pid,status=1) # Query to data base and get all we can also use get , filter or  get_object_or_404
    #posts = Post.objects.filter(status=1) # it means if post was published then we display it to screen other wise if status=0 it not gonna show those since they are not published
    #context = {'posts':posts} # use context and use a variable 'posts' and equal to our posts and then we use it inside the template for display
    return render(request,"test.html")

