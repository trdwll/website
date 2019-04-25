from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

from taggit.managers import TaggableManager

def blog_post_upload_path(instance, filename):
    return 'blog/%s/%s' % (instance.slug, filename)


class Category(models.Model):
    title = models.CharField(max_length=100, help_text='Title of the category.')
    slug = models.SlugField(unique=True)

    def get_absolute_url(self):
        return reverse('blog_category_page', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'blog_category'


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_author')
    published_date = models.DateTimeField()
    title = models.CharField(max_length=200, help_text='Title of the post.')
    body = models.TextField(help_text='The content of the post. (<strong>Markdown Supported</strong>)')
    description = models.CharField(max_length=100, help_text='A short tagline that describes what the reader will be reading about.')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, help_text='The category that the post will be listed under.')
    tags = TaggableManager(blank=True)
    is_published = models.BooleanField(default=True, help_text='Do you want this post to be published publicly?')
    image = models.ImageField(upload_to=blog_post_upload_path)
    slug = models.SlugField(unique=True)

    def get_absolute_url(self):
        return reverse('blog_post_page', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'blog_post'
