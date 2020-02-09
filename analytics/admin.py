from django.contrib import admin
from django.contrib.admin import SimpleListFilter
from django.conf import settings
from django.db.models import Count, Sum, Min, Max
from django.db.models.functions import Trunc
from django.db.models import DateTimeField

from .models import (
    GlobalPageHit, Visitor, VisitorPageHit,
    GlobalPageHitSummary, VisitorSummary, VisitorPageHitSummary
)

class PageHitFilter(SimpleListFilter):
    title = 'Page Hits Type'
    parameter_name = 'pagehit'

    def lookups(self, request, model_admin):
        return [('highestcount', 'Highest Count'), ('newest', 'Newest'), ('oldest', 'Oldest'), ('file', 'File'), ('page', 'Page')]

    # this queryset using __contains is probably the worst way to verify if it's a file or not - however it does work... for now lol
    def queryset(self, request, queryset):
        if self.value() == 'highestcount':
            return queryset.order_by('-hit_count')
        elif self.value() == 'newest':
            return queryset.order_by('-id')
        elif self.value() == 'oldest':
            return queryset.order_by('id')
        elif self.value() == 'file':
            return queryset.filter(page_url__contains='.')
        elif self.value() == 'page':
            return queryset.exclude(page_url__contains='.')
        else:
            return queryset

@admin.register(GlobalPageHitSummary)
class GlobalPageHitAdminSummary(admin.ModelAdmin):
    change_list_template = 'admin/custom/globalpagehitsummary_change_list.html'

    def changelist_view(self, request, extra_context=None):
        response = super().changelist_view(
            request,
            extra_context=extra_context,
        )

        return response

class GlobalPageHitAdmin(admin.ModelAdmin):
    list_display = ('page_url', 'hit_count', 'created', 'modified', )
    list_filter = (PageHitFilter, )
    search_fields = ['page_url', 'hit_count', 'created', 'modified']

class VisitorAdmin(admin.ModelAdmin):
    list_display = ('created', 'ip_address', 'ip_country', 'last_visit', )
    search_fields = ['created', 'ip_address', 'ip_country', 'last_visit']

class VisitorPageHitAdmin(admin.ModelAdmin):
    list_display = ('page_url', 'visitor', 'hit_count', 'created', )
    list_filter = (PageHitFilter, )
    search_fields = ['page_url', 'visitor__ip_address', 'hit_count', 'created']


admin.site.register(GlobalPageHit, GlobalPageHitAdmin)
admin.site.register(Visitor, VisitorAdmin)
admin.site.register(VisitorPageHit, VisitorPageHitAdmin)
