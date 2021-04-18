from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.views.generic import View, ListView
from django.core.exceptions import PermissionDenied

from blog.models import Post
from .models import About

class HomeView(View):
    template_name = 'index.html'

    def get(self, request):
        return render(request, self.template_name)


class AboutView(View):
    template_name = 'about.html'

    def get(self, request):
        text = About.objects.all().first()

        return render(request, self.template_name, {'about_text': text})


class RedirectHomeView(View):
    def get(self, request):
        return redirect('home_page')



# Error Views


def permission_denied_403(request, exception=None):
    return render(request, 'error_pages/403.html', status=403)

def not_found_404(request, exception=None):
    return render(request, 'error_pages/404.html', status=404)

def server_error_500(request, exception=None):
    return render(request, 'error_pages/500.html', status=500)