from django.shortcuts import render, get_object_or_404
from django.views.generic import View

from .models import Post, Category

class BlogPostView(View):
    template_name = 'blog/post.html'

    def get(self, request, slug):
        # Get the post object from the database by using the slug

        if request.user.is_authenticated and request.user.is_superuser:
            post = get_object_or_404(Post.objects.filter(slug=slug))
        else:
            post = get_object_or_404(Post.objects.filter(slug=slug, is_published=True))


        return render(request, self.template_name, {
            'POST': post
        })


def get_posts_by_category(slug):
    archive = {}

    for post in Post.objects.filter(is_published=True, category=Category.objects.filter(slug=slug).first()).order_by('-published_date'):
        archive.setdefault(post.published_date.year, []).append(post)

    return archive
    

class BlogCategoryPostView(View):
    template_name = 'blog/category-posts.html'

    def get(self, request, slug):
        return render(request, self.template_name, {'POSTS': get_posts_by_category(slug), 'POSTS_CATEGORY': Category.objects.filter(slug=slug).first()})
