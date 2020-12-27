from django.shortcuts import render, get_object_or_404
from django.views.generic import View
from django.template.loader import render_to_string

from .models import Post, Category

class BlogPostView(View):
    template_name = 'blog/post.html'

    def get(self, request, slug):

        q = request.GET.get('preview')
        preview = q is not None and q == 'true'
        post = get_object_or_404(Post.objects.filter(slug=slug))
        if preview or request.user.is_authenticated and request.user.is_superuser and post.is_published == False:
            msg = render_to_string('utils/alerts/alert_warning.html', {'title': 'Hold up!', 'content': 'You\'re viewing this post as a preview. Please don\'t share the post with anyone.' if preview else 'This post is not published. Only staff can view this post currently.'})
        else:
            post = get_object_or_404(Post.objects.filter(slug=slug, is_published=True))
            msg = ''

        result = 'hljs' in post.body or 'code class="language-' in post.body or 'language-' in post.body
        return render(request, self.template_name, {'POST': post, 'msg': msg, 'has_hljs': result})


class BlogCategoryPostView(View):
    template_name = 'blog/category_posts.html'
    def get(self, request, slug):
        return render(request, self.template_name, {'POSTS': Category.get_posts_formatted(slug), 'POSTS_CATEGORY': Category.objects.filter(slug__iexact=slug).first()})
