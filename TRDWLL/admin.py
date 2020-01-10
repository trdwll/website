from django.contrib import admin

from .models import About

class AboutAdmin(admin.ModelAdmin):
    
    def has_add_permission(self, *args, **kwargs):
        # restrict only 1 entry of this model
        return not About.objects.exists()

admin.site.register(About, AboutAdmin)
