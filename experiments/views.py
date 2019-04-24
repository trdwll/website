from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.views.generic import View, ListView

from .models import Experiment

class ExperimentsHomeView(View):
    template_name = 'experiments/index.html'

    def get(self, request):
        experiments = Experiment.objects.filter(is_published=True).order_by('published_date')

        return render(request, self.template_name, {
            'EXPERIMENTS': experiments,
        })


class ExperimentPostView(View):
    template_name = 'experiments/post.html'

    def get(self, request, slug):
        experiment = get_object_or_404(Experiment.objects.filter(is_published=True, slug=slug))

        return render(request, self.template_name, {
            'EXPERIMENT': experiment
        })