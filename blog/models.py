from django.db import models
from django.urls import reverse

class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    is_published = models.BooleanField(default=True)
    published_date = models.DateField()
    modified_date = models.DateField(null=True, blank=True)
    slug = models.SlugField(unique=True)
    tags = models.ManyToManyField('Tag', related_name='blog_posts')
    snippet = models.CharField('snippet', max_length=250)
    content = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail', kwargs = {'slug': self.slug})


class Tag(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('tag', kwargs = {'tag': self.name})


class Comment(models.Model):
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    email = models.EmailField()
    body = models.TextField()
    published_date = models.DateField(auto_now_add=True)
    is_approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['-published_date']

    def __str__(self):
        return "Comment by %s on %s: %s" % (self.name, self.published_date, self.body)