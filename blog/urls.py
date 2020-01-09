from django.urls import path

from .views import BlogPostView

urlpatterns = [
    path('<slug:slug>/', BlogPostView.as_view(), name='blog_post_page'),
]
