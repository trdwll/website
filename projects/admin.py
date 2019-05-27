from django.contrib import admin

from .models import Project, ProjectVersion, ProjectPatchNote

class ProjectPatchNoteAdmin(admin.TabularInline):
    model = ProjectPatchNote
    extra = 0


class ProjectVersionAdmin(admin.ModelAdmin):
    inlines = (ProjectPatchNoteAdmin, )
    list_display = ['project', 'version', 'version_label', 'channel', 'is_critical_update', 'date']


class ProjectAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title', )}


admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectVersion, ProjectVersionAdmin)