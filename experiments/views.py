from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.views.generic import View, ListView

from .models import Experiment

class ExperimentsHomeView(View):
    template_name = 'experiments/index.html'

    def get(self, request):
        return render(request, self.template_name, {'EXPERIMENTS': Experiment.get_experiments_formatted()})


class ExperimentPostView(View):
    template_name = 'experiments/experiment.html'

    def get(self, request, slug):
        experiment = get_object_or_404(Experiment.objects.filter(is_published=True, slug=slug))

        return render(request, self.template_name, {'EXPERIMENT': experiment})