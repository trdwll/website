from django.db import models
from django.urls import reverse

from ckeditor_uploader.fields import RichTextUploadingField


def experiment_upload_path(instance, filename):
    return 'experiments/%s/%s' % (instance.slug, filename)


class Experiment(models.Model):
    published_date = models.DateTimeField(help_text='When was this project created?')
    title = models.CharField(max_length=100, help_text='Title of the post.')
    body = RichTextUploadingField()
    is_published = models.BooleanField(default=True, help_text='Do you want this post to be published publicly?')
    tech_used = models.CharField(max_length=250, help_text='Tech that was used for this experiment.')
    slug = models.SlugField(unique=True)

    # TODO: add a tagline?

    def get_absolute_url(self):
        return reverse('experiment_post_page', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'experiment_entry'