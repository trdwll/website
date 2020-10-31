from django.contrib import admin
from .models import Experiment


class ExperimentAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title', )}
    search_fields = ['title', 'body']
    list_display = ['title', 'status', 'published_date', 'is_published']
    ordering = ('-published_date', )
    fieldsets = (
      ('Experiment Information', {
          'fields': ('published_date', 'is_published', 'status', 'title', 'description', 'slug', 'body', )
      }),
      ('Sidebar Information', {
          'fields': ('download_link', 'tech_used',  ('learned_list', 'struggled_list', ))
      }),
   )

admin.site.register(Experiment, ExperimentAdmin)