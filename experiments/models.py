from django.db import models
from django.urls import reverse


def experiment_upload_path(instance, filename):
    return 'experiments/%s/%s' % (instance.slug, filename)


class Experiment(models.Model):
    published_date = models.DateTimeField()
    title = models.CharField(max_length=100, help_text='Title of the post.')
    body = models.TextField(help_text='The content of the post. (<strong>Markdown Supported</strong>)')
    is_published = models.BooleanField(default=True, help_text='Do you want this post to be published publicly?')
    is_featured = models.BooleanField(default=False, help_text='Do you want this post to be displayed as a featured post on the homepage?')
    image = models.ImageField(upload_to=experiment_upload_path)
    slug = models.SlugField(unique=True)


    def get_absolute_url(self):
        return reverse('experiment_post_page', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'experiment_entry'