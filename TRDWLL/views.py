from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.views.generic import View, ListView

from blog.models import Post
from experiments.models import Experiment

class HomeView(View):
    template_name = 'index.html'

    def get(self, request):
        featured_experiments = Experiment.objects.filter(is_published=True, is_featured=True)[:2]
        recent_posts = Post.objects.filter(is_published=True).order_by('-published_date')[:4]

        return render(request, self.template_name, {
            'FEATURED_EXPERIMENTS': featured_experiments,
            'RECENT_POSTS': recent_posts,
        })


class AboutView(View):
    template_name = 'about.html'

    def get(self, request):
        return render(request, self.template_name)