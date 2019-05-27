from django.urls import path

from .views import *

urlpatterns = [
    path('api/<slug:slug>/update/<channel>/', ProjectUpdateListView.as_view())
]