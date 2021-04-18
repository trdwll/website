from django.shortcuts import render, get_object_or_404
from django.views.generic import View
from django.template.loader import render_to_string
from django.conf import settings

from .models import Post, Category

class BlogHomeView(View):
    template_name = 'blog/index.html'

    def get(self, request):
        return render(request, self.template_name, {'POSTS': Post.get_posts_formatted(request.user.is_authenticated), 'CATEGORIES': Post.get_categories_formatted_sidebar(), 'ARCHIVE': Post.get_archive_posts_sidebar()})

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

        has_hljs = 'hljs' in post.body or 'code class="language-' in post.body or 'language-' in post.body
        context = {'POST': post, 'msg': msg, 'has_hljs': has_hljs}
        if has_hljs:
            context.update({'HIGHLIGHT_JS_VERSION': settings.HIGHLIGHT_JS_VERSION, 'HIGHLIGHT_JS_SHA': settings.HIGHLIGHT_JS_SHA, 'HIGHLIGHT_JS_LIGHT_SHA': settings.HIGHLIGHT_JS_LIGHT_SHA, 'HIGHLIGHT_JS_DARK_SHA': settings.HIGHLIGHT_JS_DARK_SHA})
        return render(request, self.template_name, context=context)


class BlogCategoryPostView(View):
    template_name = 'blog/category_posts.html'
    def get(self, request, slug):
        return render(request, self.template_name, {'POSTS': Category.get_posts_formatted(slug), 'POSTS_CATEGORY': Category.objects.filter(slug__iexact=slug).first()})

class BlogPostsFromYear(View):
    template_name = 'blog/year_posts.html'
    def get(self, request, year):
        return render(request, self.template_name, {'POSTS': Category.get_posts_formatted(None, year), 'year': year})