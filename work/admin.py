from django.contrib import admin
from .models import WorkProduct

class WorkProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title', )}

admin.site.register(WorkProduct, WorkProductAdmin)