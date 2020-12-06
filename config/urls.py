"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from django.contrib.sitemaps import GenericSitemap
from .sitemaps import BlogPostSitemap, TagSitemap, HomeViewSitemap, StaticViewSitemap
from config.settings import ADMIN_URL
from blog import views

# define objects for sitemap
sitemaps = {
    'blog': BlogPostSitemap,
    'tag': TagSitemap,
    'home': HomeViewSitemap,
    'static': StaticViewSitemap,
}

urlpatterns = [
    path(route=ADMIN_URL, view=admin.site.urls),
    #path(route='', view=include('blog.urls')),
    path(route='', view=views.home, name='home'),
    path(route='posts/', view=views.posts, name='posts'),
    path(route='posts/<slug:slug>/', view=views.detail, name='detail'),
    path(route='tags/<tag>/', view=views.tag, name='tag'),
    path(route='contact/', view=views.contact, name='contact'),
    path(route='privacy/', view=views.privacy, name='privacy'),
    path(route='thanks/', view=views.thanks, name='thanks'),
    path(route='comment/', view=views.comment, name='comment'),
    path(route='projects/', view=include('projects.urls')),

    path('sitemap.xml', sitemap, 
        {'sitemaps': sitemaps},
        name='django.contrib.sitemaps.views.sitemap')
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)