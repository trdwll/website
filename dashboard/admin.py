from django.contrib import admin

from .models import analytics

class GlobalPageHitAdmin(admin.ModelAdmin):
    list_display = ('page_url', 'hit_count', 'created', 'modified', )
    search_fields = ['page_url', 'hit_count', 'created', 'modified']


class VisitorAdmin(admin.ModelAdmin):
    list_display = ('get_ip_address', 'ip_country', 'created', 'last_visit', )
    list_filter = ['ip_country']
    search_fields = ['created', 'ip_address', 'ip_country']

    def get_ip_address(self, instance):
        return str(instance.ip_address)
    
    get_ip_address.short_description = 'IP Address'
    get_ip_address.allow_tags = True


class VisitorPageHitAdmin(admin.ModelAdmin):
    list_display = ('page_url', 'get_ip_address', 'created', 'referer', )
    list_filter = ('visitor__ip_country', )
    search_fields = ['page_url', 'visitor__ip_address', 'created', 'user_agent']

    def get_ip_address(self, instance):
        return str(instance.visitor.ip_address)
    
    get_ip_address.short_description = 'IP Address'
    get_ip_address.allow_tags = True


admin.site.register(analytics.GlobalPageHit, GlobalPageHitAdmin)
admin.site.register(analytics.Visitor, VisitorAdmin)
admin.site.register(analytics.VisitorPageHit, VisitorPageHitAdmin)