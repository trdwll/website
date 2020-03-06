from django.db import models
from django.urls import reverse
from django.db.models.signals import pre_save
from TRDWLL.signals import create_redirect
from TRDWLL.utils import get_formatted_data

from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.fields import RichTextField

class Experiment(models.Model):
    published_date = models.DateTimeField(help_text='When was this experiment created?')
    title = models.CharField(max_length=100, help_text='Title of the post.')
    description = models.CharField(max_length=500, help_text='The description of the experiment.')
    body = RichTextUploadingField()
    is_published = models.BooleanField(default=True, help_text='Do you want this post to be published publicly?')
    tech_used = models.CharField(max_length=250, help_text='Tech that was used for this experiment.')
    learned_list = RichTextField(blank=True, help_text='Things that I learned during the development of this experiment?', config_name='experiments_sidebar')
    struggled_list = RichTextField(blank=True, help_text='Things that I struggled with during the development of this experiment?', config_name='experiments_sidebar')
    slug = models.SlugField(unique=True)

    def get_absolute_url(self):
        return reverse('experiment_post_page', kwargs={'slug': self.slug})

    def get_experiments_formatted():
        """ Get the posts and format them for display """
        queried_experiments = get_formatted_data(Experiment.objects.filter(is_published=True).order_by('-published_date'))

        formatted_experiments = []

        for year,experiments in queried_experiments.items():
            formatted_experiments.append('<h2 class="archive-year">'+str(year)+'</h2><div class="row">')

            for experiment in experiments:
                description = experiment.description[0:117]+'...' if len(experiment.description) > 117 else experiment.description
                formatted_experiments.append('<div class="col-md-4 pb-2">'+
                    '<div class="card h-100">'+
                    '<div class="card-body"><h5 class="card-title"><a href="'+experiment.get_absolute_url()+'">'+experiment.title+'</a></h5><h6 class="card-subtitle mb-2 text-muted">'+description+'</h6></div>'+
                    '</div>'+ # end card div
                    '</div>') # end col
                #formatted_experiments.append('<div class="archive-item"><a href="'+experiment.get_absolute_url()+'" class="archive-title">'+experiment.title+'</a></div>')
            
            # end the row
            formatted_experiments.append('</div><hr />')

        return ''.join(formatted_experiments)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'experiment_entry'


pre_save.connect(create_redirect, sender=Experiment)