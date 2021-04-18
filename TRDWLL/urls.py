from django.contrib import admin
from django.conf import settings
from django.urls import path, include, reverse
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from django.contrib.sitemaps import Sitemap, GenericSitemap

from django_otp.admin import OTPAdminSite

from .views import HomeView, AboutView
from blog.models import Post
from experiments.models import Experiment

import debug_toolbar

class BlogSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.6
    protocol = 'https'

    def items(self):
        return Post.objects.filter(is_published=True)

    def lastmod(self, obj):
        return obj.published_date

class ExperimentsSitemap(Sitemap):
    changefreq = ''
    priority = 0.4
    protocol = 'https'

    def items(self):
        return Experiment.objects.filter(is_published=True)

    def lastmod(self, obj):
        return obj.published_date

class StaticViewSitemap(Sitemap):
    priority = 0.7
    changefreq = 'daily'

    def items(self):
        return ['']

    def location(self, item):
        return item

sitemaps = {
    'static': StaticViewSitemap,
    'blog': BlogSitemap,
    'experiments': ExperimentsSitemap
}

urlpatterns = [
    path('', HomeView.as_view(), name='home_page'),
    path('about/', AboutView.as_view(), name='about_page'),
    path('blog/', include('blog.urls'), name='blog_page'),
    path('experiments/', include('experiments.urls'), name='experiments_page'),
    
    path('admin/', admin.site.urls),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),

    path('tinymce/', include('tinymce.urls')),
    path('__debug__/', include(debug_toolbar.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


admin.site.site_header = 'TRDWLL AdminCP'
admin.site.site_title = 'TRDWLL AdminCP'

if not settings.DEBUG:
    admin.site.__class__ = OTPAdminSite


# Error pages

handler403 = 'TRDWLL.views.permission_denied_403'
handler404 = 'TRDWLL.views.not_found_404'
handler500 = 'TRDWLL.views.server_error_500'