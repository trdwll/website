from django.contrib import admin

from .models import About, Alert, VisitorPageHit

class AboutAdmin(admin.ModelAdmin):
    
    def has_add_permission(self, *args, **kwargs):
        # restrict only 1 entry of this model
        return not About.objects.exists()

class AlertAdmin(admin.ModelAdmin):
    list_display = ('type', 'url')


class VisitorPageHitAdmin(admin.ModelAdmin):
    list_display = ('page_url', 'ip_address', 'created', 'referer', )
    list_filter = ('ip_country', )
    search_fields = ['page_url', 'ip_address', 'created', 'user_agent']

admin.site.register(About, AboutAdmin)
admin.site.register(Alert, AlertAdmin)
admin.site.register(VisitorPageHit, VisitorPageHitAdmin)
