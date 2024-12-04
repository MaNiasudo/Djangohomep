from django.shortcuts import render , redirect , get_object_or_404 
from blog.models import Post , Comment
from django.core.paginator import Paginator , EmptyPage , PageNotAnInteger
from blog.forms import CommentForm
from django.contrib import messages

def blog_home(request,cat_name=None,author_username=None,tag_name=None):
    posts = Post.objects.filter(status=1)
    if cat_name:
        posts = posts.filter(category__name=cat_name) # We can have 2 path in same func and use and if to call each 
    if author_username:
        posts = posts.filter(author__username=author_username) # and if we wanted to have more arguments we just add more  the author relating to our User Model
    if tag_name:
        posts = posts.filter(tags__name__in=[tag_name]) # We use taggit here and we need to do it diffrently than category
    posts = Paginator(posts,3) # -> we using paginator here we get for example 10 posts az input and we ask for 3 post per pages
    try:
        page_number = request.GET.get('page')
        posts = posts.get_page(page_number) # we use get page to take us to that page so if post is 1 we go on 1 and if its 3 we go on page 3 if it exists
    except PageNotAnInteger:
        posts = posts.get_page(1) # And this take us to page num 1 if we gave it wrong input 
    except EmptyPage:
        posts = posts.get_page(1) # Same here 

    context = {'posts':posts}
    return render(request, "blog/blog-home.html",context)

def blog_single(request,pid):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
           form.save()
        messages.success(request, "Your Message Sended")
    post = get_object_or_404(Post,id=pid,status=1)# with status = 1 users can only access to published posts  
    comments = Comment.objects.filter(post=post.id,approved=1).order_by('-created_date')
    form = CommentForm()
    context = {'post':post,'comments':comments}
    return render(request, "blog/blog-single.html", context)
 
def blog_search(request):
    posts = Post.objects.filter(status=1)
    if request.method == 'GET':
        if s :=  request.GET.get('s'):
            posts= posts.filter(content__contains=s)
    context = {'posts':posts}
    return render(request, "blog/blog-home.html",context)









