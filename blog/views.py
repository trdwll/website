from django.shortcuts import render, get_object_or_404
from django.views.generic import View

from .models import Post, Category

class BlogPostView(View):
    template_name = 'blog/post.html'

    def get(self, request, slug):

        q = request.GET.get('preview')
        preview = q is not None and q == 'true'
        post = get_object_or_404(Post.objects.filter(slug=slug))
        if preview or request.user.is_authenticated and request.user.is_superuser and post.is_published == False:
            msg = 'You\'re viewing this post as a preview. Please don\'t share the post with anyone.' if preview else 'This post is not published. Only staff can view this post currently.'
        else:
            post = get_object_or_404(Post.objects.filter(slug=slug, is_published=True))
            msg = ''

        return render(request, self.template_name, {'POST': post, 'msg': msg})


class BlogCategoryPostView(View):
    template_name = 'blog/category-posts.html'
    def get(self, request, slug):
        return render(request, self.template_name, {'POSTS': Category.get_posts_formatted(slug), 'POSTS_CATEGORY': Category.objects.filter(slug__iexact=slug).first()})
