
from django.contrib import admin
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static 
from home.sitemaps import StaticViewSitemap
from django.contrib.sitemaps.views import sitemap
from blog.models import *
from blog.sitemaps import BlogSitemap

sitemaps = {
    "static": StaticViewSitemap,
    "blog":BlogSitemap
    
}


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include("home.urls")),
    path('blog/',include("blog.urls")),
    path(
        "sitemap.xml",
        sitemap,
        {"sitemaps": sitemaps},
        name="django.contrib.sitemaps.views.sitemap",
    ),
    path('robots.txt', include('robots.urls')),
    path('summernote/', include('django_summernote.urls')),
    path('captcha/', include('captcha.urls')),
]   

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)