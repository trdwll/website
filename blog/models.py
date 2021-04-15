from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from django.template.loader import render_to_string
from django.db.models import Q, Count
from django.contrib.sitemaps import ping_google

from TRDWLL.signals import create_redirect
from TRDWLL.utils import get_formatted_data

from tinymce.models import HTMLField

import operator
from datetime import datetime

class Category(models.Model):
    title = models.CharField(max_length=100, help_text='Title of the category.')
    description = models.CharField(max_length=200, blank=True, help_text='A short description for the category.')
    slug = models.SlugField(unique=True)

    def get_absolute_url(self):
        return reverse('blog_category_page', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title

    def get_posts_formatted(slug, year=None):
        """ Get the posts and format them for display """
        if year == None:
            queried_posts = get_formatted_data(Post.objects.filter(is_published=True, category=Category.objects.filter(slug__iexact=slug).first()))
        else:
            queried_posts = get_formatted_data(Post.objects.filter(is_published=True, published_date__year=year))
        
        formatted_posts = []

        for i, (year,posts) in enumerate(queried_posts.items()):
            formatted_posts.append(render_to_string('blog/extra/post_home/post_start.html', {'year': year, 'index': i, 'post_count': len(posts)}))

            for count, post in enumerate(posts, 1):
                formatted_posts.append(render_to_string('blog/extra/post_home/post_body.html', {'post': post, 'index': count}))
            
            formatted_posts.append('</ul>')
        return ''.join(formatted_posts)

    class Meta:
        db_table = 'blog_category'
        ordering = ['title']
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Post(models.Model):
    DIFFICULTIES = (
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
    )
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_author')
    published_date = models.DateTimeField()
    title = models.CharField(max_length=200, help_text='Title of the post.')
    body = HTMLField()
    difficulty = models.CharField(max_length=64, choices=DIFFICULTIES, blank=True, null=True, help_text='If this is a guide/tutorial then what difficulty level is this?')
    description = models.CharField(max_length=100, help_text='A short tagline that describes what the reader will be reading about.')
    keywords = models.CharField(max_length=512, help_text='SEO keywords to help get more exposure.', blank=True, null=True)
    category = models.ManyToManyField(Category, help_text='The category that the post will be listed under.')
    is_published = models.BooleanField(default=True, help_text='Do you want this post to be published publicly?')
    slug = models.SlugField(unique=True)

    def get_absolute_url(self):
        return reverse('blog_post_page', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title

    def get_categories_formatted_sidebar():
        """ Get the categories and format them for display on the sidebar """
        categories = []
        cats = {}

        # sort through all categories and add them to a dictionary
        for tmp in Category.objects.all().exclude(post__isnull=True).annotate(count=Count("id")).filter(count__gte=0, post__is_published=True):
            cats.update({tmp:tmp.count})

        # sort the dictionary by value
        cats = dict(sorted(cats.items(), key=operator.itemgetter(1), reverse=True))

        # create the html format for the sidebar
        categories.append(render_to_string('blog/extra/sidebar/categories_start.html', {}))
        for k,v in cats.items():
            categories.append(render_to_string('blog/extra/sidebar/categories_body.html', {'category': k, 'category_count': v}))
        categories.append(render_to_string('blog/extra/sidebar/categories_end.html', {})) # lol it's just a </ul>

        return ''.join(categories)

    def get_posts_formatted(is_authenticated):
        """ Get the posts and format them for display """
        if is_authenticated:
            queried_posts = get_formatted_data(Post.objects.all())
        else:
            queried_posts = get_formatted_data(Post.objects.filter(is_published=True))

        formatted_posts = []

        for i, (year,posts) in enumerate(queried_posts.items()):
            # filter out previous years content, but display the year/archive link
            if year == datetime.today().year:
                formatted_posts.append(render_to_string('blog/extra/post_home/post_start.html', {'year': year, 'index': i, 'post_count': len(posts)}))
                
                for count, post in enumerate(posts, 1):
                    categories = [] 
                    # TODO: By doing this query we're adding a query per post 
                    # at the time of writing this we do 5 queries on home
                    # for tmp in post.category.all():
                    #     categories.append(render_to_string('blog/extra/post_home/categories_list.html', {'category': tmp}))
                    # categories.sort() # sort the categories to be alphabetical order

                # if post.published_date.year == datetime.today().year:
                    formatted_posts.append(render_to_string('blog/extra/post_home/post_body.html', {'post': post, 'index': count, 'post_categories': ''.join(categories)}))
                    
                formatted_posts.append('</ul>')
        return ''.join(formatted_posts)

    def get_archive_posts_sidebar():
        queried_posts = get_formatted_data(Post.objects.filter(is_published=True))

        formatted_archive = []
        
        formatted_archive.append(render_to_string('blog/extra/sidebar/archive_start.html'))
        for i, (year,posts) in enumerate(queried_posts.items()):
            # filter out previous years content, but display the year/archive link
            if year != datetime.today().year:
                formatted_archive.append(render_to_string('blog/extra/sidebar/archive_body.html', {'year': year, 'index': i, 'post_count': len(posts)}))
        
        formatted_archive.append('</ul>')
        return ''.join(formatted_archive)

    
    def categories(self):
        return ", ".join([str(p.title) for p in self.category.all()])

    def save(self, force_insert=False, force_update=False):
        super().save(force_insert, force_update)
        try:
            ping_google()
        except Exception:
            pass

    class Meta: 
        db_table = 'blog_post'
        ordering = ['-published_date']
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'


pre_save.connect(create_redirect, sender=Post)
pre_save.connect(create_redirect, sender=Category)