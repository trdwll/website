from django.db import models

from ckeditor_uploader.fields import RichTextUploadingField

class About(models.Model):
    body = RichTextUploadingField()

    def __str__(self):
        return 'About Me'

    class Meta:
        db_table = 'about_entry'


class Alert(models.Model):
    TYPES = (
        ('alert alert-primary', 'Primary'),
        ('alert alert-secondary', 'Secondary'),
        ('alert alert-success', 'Success'),
        ('alert alert-danger', 'Danger'),
        ('alert alert-warning', 'Warning'),
        ('alert alert-info', 'Info'),
        ('alert alert-light', 'Light'),
        ('alert alert-dark', 'Dark'),
    )
    type = models.CharField(choices=TYPES, help_text='The style of the alert.', max_length=32)
    body = models.TextField(help_text='The content that should be displayed for the alert.') # no need for a richtextfield
    url = models.CharField(max_length=512, null=True, blank=True, help_text='Display the alert on a specified page.') # URLField requires a valid url, here we only want /blog/ etc

    def __str__(self):
        return 'A ' + str(self.get_type_display()) + ' alert on ' + str(self.url)

    def print_alerts(request):
        """ Get the alerts and format them for display """

        alerts = [] 

        for tmp in Alert.objects.all():
            if request.get_full_path() == tmp.url or tmp.url is None or tmp.url is '':
                alerts.append('<div class="'+tmp.type+'" role="alert">'+tmp.body+'</div>')

        return ''.join(alerts)

    class Meta:
        db_table = 'alert_entry'