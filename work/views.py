from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.views.generic import View

class WorkHomeView(View):
    template_name = 'work/index.html'

    def get(self, request):
        return render(request, self.template_name)