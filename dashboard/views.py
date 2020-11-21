from django.shortcuts import render
from django.views.generic import View, ListView
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator

from django.db.models import Count

from .models import (
    GlobalPageHit, Visitor, VisitorPageHit,
)

@method_decorator(staff_member_required, name='dispatch')
class DashboardHomeView(View):
    template_name = 'dashboard/home.html'

    def get(self, request):
        # get all pages that were hit and the count
        global_entries = GlobalPageHit.objects.all().order_by('-hit_count')
        top_ten_global_entries = global_entries[:10]
        
        # ability change the data date (1hr, 6hr, 24hr, 48hr, 72hr, 5d, 1w, 2w, 1m, 3m, 6m, 1y, all)

        # get all countries and sort by count
        all_countries = VisitorPageHit.objects.all().values('visitor__ip_country').annotate(total=Count('visitor__ip_country')).order_by('-total')
        top_ten_countries = all_countries[:10]

        return render(request, self.template_name, { 'global_entries': top_ten_global_entries, 'top_ten_countries': top_ten_countries })


@method_decorator(staff_member_required, name='dispatch')
class VisitorPageView(ListView):
    template_name = 'dashboard/visitor_page_list.html'
    model = VisitorPageHit
    queryset = VisitorPageHit.objects.all()
    context_object_name = 'visitorpagehits'
    paginate_by = 10