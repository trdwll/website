from django.db import models
from django.template.loader import render_to_string

from ckeditor_uploader.fields import RichTextUploadingField

class About(models.Model):
    body = RichTextUploadingField()

    def __str__(self):
        return 'About Me'

    class Meta:
        db_table = 'about_entry'
        verbose_name = 'About'
        verbose_name_plural = 'About'


class Alert(models.Model):
    TYPES = (
        ('alert alert-success', 'Success'),
        ('alert alert-danger', 'Danger'),
        ('alert alert-warning', 'Warning'),
        ('alert alert-info', 'Info'),
    )
    type = models.CharField(choices=TYPES, help_text='The style of the alert.', max_length=32)
    title = models.CharField(max_length=128, help_text='The title for the alert!', null=True, blank=True, default='')
    body = models.TextField(help_text='The content that should be displayed for the alert.')
    url = models.CharField(max_length=512, null=True, blank=True, help_text='Display the alert on a specified page.') # URLField requires a valid url, here we only want /blog/ etc

    def __str__(self):
        return 'A ' + str(self.get_type_display()) + ' alert on ' + str(self.url)

    def print_alerts(request):
        """ Get the alerts and format them for display """

        alerts = [] 

        for tmp in Alert.objects.all():
            if request.get_full_path() == tmp.url or tmp.url == None or tmp.url == '':
                alerts.append(render_to_string('utils/'+tmp.get_type_display().lower()+'-alert.html', {'title': tmp.title, 'content': tmp.body}))

        return ''.join(alerts)

    class Meta:
        db_table = 'alert_entry'
        ordering = ['type']
        verbose_name = 'Alert'
        verbose_name_plural = 'Alerts'