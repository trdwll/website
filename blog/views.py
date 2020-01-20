from django.shortcuts import render, get_object_or_404
from django.views.generic import View

from .models import Post

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