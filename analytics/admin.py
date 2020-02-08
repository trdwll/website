from django.contrib import admin
from django.contrib.admin import SimpleListFilter
from django.conf import settings
import os

from .models import GlobalPageHit, Visitor, VisitorPageHit

class PageHitFilter(SimpleListFilter):
    title = 'Page Hits Type'
    parameter_name = 'pagehit'

    def lookups(self, request, model_admin):
        return [('file', 'File'), ('page', 'Page')]

    # this queryset using __contains is probably the worst way to verify if it's a file or not - however it does work... for now lol
    def queryset(self, request, queryset):
        if self.value() == 'file':
            return queryset.filter(page_url__contains='.')
        elif self.value() == 'page':
            return queryset.exclude(page_url__contains='.')
        else:
            return queryset


class GlobalPageHitAdmin(admin.ModelAdmin):
    list_display = ('page_url', 'hit_count', 'created', 'modified', )
    list_filter = (PageHitFilter, )

class VisitorAdmin(admin.ModelAdmin):
    list_display = ('created', 'ip_address', 'ip_country', 'last_visit', )

class VisitorPageHitAdmin(admin.ModelAdmin):
    list_display = ('page_url', 'visitor', 'hit_count', 'created', )
    list_filter = (PageHitFilter, )


admin.site.register(GlobalPageHit, GlobalPageHitAdmin)
admin.site.register(Visitor, VisitorAdmin)
admin.site.register(VisitorPageHit, VisitorPageHitAdmin)
