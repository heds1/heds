from django.contrib import admin
from blog.models import BlogPost, Tag, Comment
from django.contrib.sites.models import Site

admin.site.register(BlogPost)
admin.site.register(Tag)
admin.site.register(Comment)

admin.site.unregister(Site)


class SiteAdmin(admin.ModelAdmin):
    fields = ('id', 'name', 'domain')
    readonly_fields = ('id',)
    list_display = ('id', 'name', 'domain')
    list_display_links = ('name',)
    search_fields = ('name', 'domain')
admin.site.register(Site, SiteAdmin)