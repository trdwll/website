from django.shortcuts import render, get_object_or_404
from django.views.generic import View

from .models import Post, Category

class BlogPostView(View):
    template_name = 'blog/post.html'

    def get(self, request, slug):
        post = get_object_or_404(Post.objects.filter(slug=slug, is_published=(request.user.is_authenticated and request.user.is_superuser) == False))
        return render(request, self.template_name, {'POST': post})


class BlogCategoryPostView(View):
    template_name = 'blog/category-posts.html'
    def get(self, request, slug):
        return render(request, self.template_name, {'POSTS': Category.get_posts_formatted(slug), 'POSTS_CATEGORY': Category.objects.filter(slug=slug).first()})
