from django.urls import path

from .views import WorkHomeView

urlpatterns = [
    path('', WorkHomeView.as_view(), name='work_home_page'),
]