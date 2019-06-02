from django.urls import path

from .views import *

urlpatterns = [
    path('api/<slug:slug>/update/<str:channel>/', ProjectUpdateListView.as_view()),
    path('api/<slug:slug>/update/<str:channel>/<str:version>/', ProjectUpdateVersionView.as_view())
]