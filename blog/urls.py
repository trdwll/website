from django.urls import path

from .views import BlogPostView
from TRDWLL.views import HomeView

urlpatterns = [
    path('', HomeView.as_view()), # force redirect back to home
    path('<slug:slug>/', BlogPostView.as_view(), name='blog_post_page'),
]
