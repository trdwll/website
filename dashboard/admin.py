from django.contrib import admin

from .models import analytics

class GlobalPageHitAdmin(admin.ModelAdmin):
    list_display = ('page_url', 'hit_count', 'created', 'modified', )
    search_fields = ['page_url', 'hit_count', 'created', 'modified']


class VisitorAdmin(admin.ModelAdmin):
    list_display = ('created', 'ip_country', 'last_visit', )
    list_filter = ['ip_country']
    search_fields = ['created', 'ip_address', 'ip_country', 'last_visit']


class VisitorPageHitAdmin(admin.ModelAdmin):
    list_display = ('page_url', 'created', 'referer', )
    list_filter = ('visitor__ip_country', )
    search_fields = ['page_url', 'visitor__ip_address', 'created', 'user_agent']


admin.site.register(analytics.GlobalPageHit, GlobalPageHitAdmin)
admin.site.register(analytics.Visitor, VisitorAdmin)
admin.site.register(analytics.VisitorPageHit, VisitorPageHitAdmin)