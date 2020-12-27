from django.contrib import admin

from .models import About, Alert

class AboutAdmin(admin.ModelAdmin):
    
    def has_add_permission(self, *args, **kwargs):
        # restrict only 1 entry of this model
        return not About.objects.exists()

class AlertAdmin(admin.ModelAdmin):
    list_display = ('type', 'url')


admin.site.register(About, AboutAdmin)
admin.site.register(Alert, AlertAdmin)
