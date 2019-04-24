from django.urls import path

from .views import ExperimentsHomeView, ExperimentPostView

urlpatterns = [
    path('', ExperimentsHomeView.as_view(), name='experiments_home_page'),
    path('<slug:slug>/', ExperimentPostView.as_view(), name='experiment_post_page'),
]