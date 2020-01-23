from django.urls import path

from .views import BlogPostView, BlogCategoryPostView
from TRDWLL.views import RedirectHomeView

urlpatterns = [
    path('', RedirectHomeView.as_view()), # force redirect back to home
    path('<slug:slug>/', BlogPostView.as_view(), name='blog_post_page'),
    path('category/<slug:slug>/', BlogCategoryPostView.as_view(), name='blog_category_page'),
]
