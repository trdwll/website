from django.contrib import admin
from .models import Experiment


class ExperimentAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title', )}
    search_fields = ['title', 'body']
    list_display = ['title', 'published_date', 'is_published']
    ordering = ('-published_date', )

admin.site.register(Experiment, ExperimentAdmin)