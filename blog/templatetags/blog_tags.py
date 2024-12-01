from django import template
from blog.models import Post

register = template.Library()


@register.simple_tag
def hello():
    return " test Hello"

@register.simple_tag(name="posts")
def counttotal():
    posts = Post.objects.filter(status=1)
    return posts


@register.filter
def snippet(value):
    return value[:20] + " ..."


@register.inclusion_tag('blog/blog-latestposts.html')
def latestposts():
    posts = Post.objects.filter(status=1).order_by('-published_date')[:4]
    return {'posts':posts}