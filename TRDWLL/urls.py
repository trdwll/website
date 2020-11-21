from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static

from django_otp.admin import OTPAdminSite

from .views import HomeView, AboutView

urlpatterns = [
    path('', HomeView.as_view(), name='home_page'),
    path('about/', AboutView.as_view(), name='about_page'),
    path('blog/', include('blog.urls'), name='blog_page'),
    path('experiments/', include('experiments.urls'), name='experiments_home_page'),
    path('dashboard/', include('dashboard.urls'), name='dashboard_home_page'),
    
    path('admin/', admin.site.urls),

    path('tinymce/', include('tinymce.urls')),
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