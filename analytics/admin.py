from django.contrib import admin
from django.contrib.admin import SimpleListFilter
from django.conf import settings

from .models import GlobalPageHit, Visitor, VisitorPageHit

class PageHitFilter(SimpleListFilter):
    title = 'Page Hits Type'
    parameter_name = 'pagehit'

    def lookups(self, request, model_admin):
        return [('highestcount', 'Highest Count'), ('newest', 'Newest'), ('oldest', 'Oldest')]

    def queryset(self, request, queryset):
        if self.value() == 'highestcount':
            return queryset.order_by('-hit_count')
        elif self.value() == 'newest':
            return queryset.order_by('-id')
        elif self.value() == 'oldest':
            return queryset.order_by('id')
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
