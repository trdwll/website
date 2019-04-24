from django.contrib import admin
from .models import Experiment


class ExperimentAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title', )}
    search_fields = ['title', 'body']
    list_display = ['title', 'published_date', 'is_published', 'is_featured']

    def save_model(self, request, obj, form, change):

        if obj.is_featured:
            featured_experiments = Experiment.objects.filter(is_published=True, is_featured=True)
            featured_count = featured_experiments.count()

            # Check if featured_experiments contains the experiment that we're saving
            experiment_is_featured = featured_experiments.filter(pk=obj.pk).exists()

            # If the featured experiments are equal to 2 and the current experiment that we're adding/editing isn't featured then edit the oldest
            if featured_count == 2 and not experiment_is_featured:
                # find the oldest experiment that's featured and unfeature it then feature this experiment
                oldest_featured = featured_experiments.order_by('published_date')[:1]
                Experiment.objects.filter(id__in=oldest_featured).update(is_featured=False)

                obj.is_featured = True

        super().save_model(request, obj, form, change)


admin.site.register(Experiment, ExperimentAdmin)