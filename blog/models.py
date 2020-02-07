from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from TRDWLL.signals import create_redirect

from TRDWLL.utils import get_formatted_data

from ckeditor_uploader.fields import RichTextUploadingField

# for category separation
prefix_char = '['
suffix_char = ']'


class Category(models.Model):
    title = models.CharField(max_length=100, help_text='Title of the category.')
    description = models.CharField(max_length=200, blank=True, help_text='A short description for the category.')
    slug = models.SlugField(unique=True)

    def get_absolute_url(self):
        return reverse('blog_category_page', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title

    def get_posts_formatted(slug):
        """ Get the posts and format them for display """
        queried_posts = get_formatted_data(Post.objects.filter(is_published=True, category=Category.objects.filter(slug=slug).first()).order_by('-published_date'))
        
        formatted_posts = []

        for year,posts in queried_posts.items():
            formatted_posts.append('<h2 class="archive-year">'+str(year)+'</h2>')

            for post in posts:
                formatted_posts.append('<div class="archive-item"><span class="post-date archive-date">'+str(post.published_date.strftime('%b %d %Y'))+'</span><a href="'+post.get_absolute_url()+'" class="archive-title">'+post.title+'</a></div>')
            
        return ''.join(formatted_posts)

    class Meta:
        db_table = 'blog_category'


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_author')
    published_date = models.DateTimeField()
    title = models.CharField(max_length=200, help_text='Title of the post.')
    body = RichTextUploadingField()
    description = models.CharField(max_length=100, help_text='A short tagline that describes what the reader will be reading about.')
    category = models.ManyToManyField(Category, help_text='The category that the post will be listed under.')
    is_published = models.BooleanField(default=True, help_text='Do you want this post to be published publicly?')
    slug = models.SlugField(unique=True)

    def get_absolute_url(self):
        return reverse('blog_post_page', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title

    def get_categories_formatted(self):
        """ Get the categories and format them for display """
        categories = [] 

        for tmp in self.category.all():
            categories.append(prefix_char+'<a href="'+tmp.get_absolute_url()+'">'+tmp.title+'</a>'+suffix_char)

        return ''.join(categories)

    def get_posts_formatted():
        """ Get the posts and format them for display """
        queried_posts = get_formatted_data(Post.objects.filter(is_published=True).order_by('-published_date'))

        formatted_posts = []

        for year,posts in queried_posts.items():
            formatted_posts.append('<h2 class="archive-year">'+str(year)+'</h2>')

            for post in posts:
                formatted_posts.append('<div class="archive-item">'+post.get_categories_formatted()+' <span class="post-date archive-date">'+str(post.published_date.strftime('%b %d %Y'))+'</span><a href="'+post.get_absolute_url()+'" class="archive-title">'+post.title+'</a></div>')
            
        return ''.join(formatted_posts)

    def categories(self):
        return ", ".join([str(p.title) for p in self.category.all()])

    class Meta:
        db_table = 'blog_post'


pre_save.connect(create_redirect, sender=Post)
pre_save.connect(create_redirect, sender=Category)