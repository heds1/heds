from django.contrib import sitemaps
from django.urls import reverse
from blog.models import BlogPost, Tag


class HomeViewSitemap(sitemaps.Sitemap):
    priority = 1
    changefreq = 'monthly'

    def items(self):
        return ['home']

    def location(self, item):
        return reverse(item)


class StaticViewSitemap(sitemaps.Sitemap):
    priority = 1
    changefreq = 'monthly'

    def items(self):
        return ['posts', 'contact']

    def location(self, item):
        return reverse(item)


class BlogPostSitemap(sitemaps.Sitemap):
    priority = 0.7
    changefreq = 'monthly'

    def items(self):
        return BlogPost.objects.all()

    def lastmod(self, obj):
        if obj.modified_date is not None:
            return obj.modified_date
        else:
            return obj.published_date


class TagSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'yearly'

    def items(self):
        return Tag.objects.all()

# todo: define a lastmod that gets the latest modified/published
# date of a blogpost related to a tag