from django.urls import path

from .views import BlogHomeView, BlogPostView

urlpatterns = [
    path('', BlogHomeView.as_view(), name='blog_home_page'),
    path('<slug:slug>/', BlogPostView.as_view(), name='blog_post_page'),

    # path('page/<int:page>/', BlogHomeView.as_view(), name='blog_home_page_paginated'),

    # path('category/<slug:slug>/', BlogCategoryView.as_view(), name='blog_category_page'),
    # path('category/<slug:slug>/page/<int:page>/', BlogCategoryView.as_view(), name='blog_category_page_paginated'),
]
