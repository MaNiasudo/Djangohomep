from django.shortcuts import render , redirect , get_object_or_404
from blog.models import Post
from django.core.paginator import Paginator , EmptyPage , PageNotAnInteger

def blog_home(request,cat_name=None,author_username=None):
    posts = Post.objects.filter(status=1)
    if cat_name:
        posts = posts.filter(category__name=cat_name) # We can have 2 path in same func and use and if to call each 
    if author_username:
        posts = posts.filter(author__username=author_username) # and if we wanted to have more arguments we just add more  the author relating to our User Model
    posts = Paginator(posts,3)
    try:
        page_number = request.GET.get('page')
        posts = posts.get_page(page_number)
    except PageNotAnInteger:
        posts = posts.get_page(1)
    except EmptyPage:
        posts = posts.get_page(1)

    context = {'posts':posts}
    return render(request, "blog/blog-home.html",context)

def blog_single(request,pid):
    post = get_object_or_404(Post,id=pid,status=1)# with status = 1 users can only access to published posts  
    context = {'post':post}
    return render(request, "blog/blog-single.html", context)
 
def blog_search(request):
    posts = Post.objects.filter(status=1)
    if request.method == 'GET':
        if s :=  request.GET.get('s'):
            posts= posts.filter(content__contains=s)
    context = {'posts':posts}
    return render(request, "blog/blog-home.html",context)












