from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.views.generic import View, ListView

from blog.models import Post
from .models import About

class HomeView(View):
    template_name = 'index.html'

    def get(self, request):
        return render(request, self.template_name, {'POSTS': Post.get_posts_formatted()})


class AboutView(View):
    template_name = 'about.html'

    def get(self, request):
        text = About.objects.all().first()

        return render(request, self.template_name, {'about_text': text})


class RedirectHomeView(View):
    def get(self, request):
        return redirect('home_page')