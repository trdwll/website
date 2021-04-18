from django.urls import path

from .views import BlogHomeView, BlogPostView, BlogCategoryPostView, BlogPostsFromYear
from TRDWLL.views import RedirectHomeView

urlpatterns = [
    path('', BlogHomeView.as_view(), name='blog_home_page'),
    path('<slug:slug>/', BlogPostView.as_view(), name='blog_post_page'),
    path('category/<slug:slug>/', BlogCategoryPostView.as_view(), name='blog_category_page'),
    path('archive/<int:year>/', BlogPostsFromYear.as_view(), name='blog_posts_year_page'),
]
