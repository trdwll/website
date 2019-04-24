from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.views.generic import View, ListView

from .models import Post

class BlogHomeView(View):
    template_name = 'blog/index.html'

    def get(self, request):
        posts = Post.objects.filter(is_published=True).order_by('published_date')

        return render(request, self.template_name, {
            'POSTS': posts
        })


class BlogPostView(View):
    template_name = 'blog/post.html'

    def get(self, request, slug):
        # Get the post object from the database by using the slug
        post = get_object_or_404(Post.objects.filter(slug=slug, is_published=True))

        return render(request, self.template_name, {
            'POST': post
        })