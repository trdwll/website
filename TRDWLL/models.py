from django.db import models
from django.template.loader import render_to_string
from django.db.models import Q

from tinymce.models import HTMLField

class About(models.Model):
    body = HTMLField()

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
        ('indigo', 'Indigo Notice'),
        ('green', 'Green Notice'),
        ('red', 'Red Notice'),
        ('yellow', 'Yellow Notice'),
        ('blue', 'Blue Notice'),
        ('purple', 'Purple Notice'),
        ('pink', 'Pink Notice'),
    )
    type = models.CharField(choices=TYPES, help_text='The style of the alert.', max_length=32)
    title = models.CharField(max_length=128, help_text='The title for the alert!', null=True, blank=True, default='')
    body = HTMLField(help_text='The content that should be displayed for the alert.')
    short_body = models.CharField(max_length=128, help_text='A short version of the body.', null=True, blank=True, default='')
    url = models.CharField(max_length=512, null=True, blank=True, help_text='Display the alert on a specified page.') # URLField requires a valid url, here we only want /blog/ etc
    notice_url = models.CharField(max_length=512, null=True, blank=True, help_text='The url that you want to redirect to on the button.')

    def __str__(self):
        return 'A ' + str(self.get_type_display()) + ' alert on ' + str(self.url)

    def print_alerts(request, is_notice=False):
        """ Get the alerts and format them for display """

        alerts = [] 
        alert_defs = dict((v, k) for k, v in Alert.TYPES)

        if not is_notice:
            d = [alert_defs['Success'], alert_defs['Danger'], alert_defs['Warning'], alert_defs['Info']]
            for tmp in Alert.objects.filter(Q(type__in=d)):
                if request.get_full_path() == tmp.url or tmp.url == None or tmp.url == '':
                    alerts.append(render_to_string('utils/alerts/alert_'+tmp.get_type_display().lower()+'.html', {'title': tmp.title, 'content': tmp.body}))
        else:
            d = [alert_defs['Indigo Notice'], alert_defs['Green Notice'], alert_defs['Red Notice'], alert_defs['Yellow Notice'], alert_defs['Blue Notice'], alert_defs['Purple Notice'], alert_defs['Pink Notice']]
            for tmp in Alert.objects.filter(Q(type__in=d)):
                if request.get_full_path() == tmp.url or tmp.url == None or tmp.url == '':
                    alerts.append(render_to_string('utils/notices/notice_'+tmp.type.lower()+'.html', { 'notice': tmp }))

        return ''.join(alerts)

    class Meta:
        db_table = 'alert_entry'
        ordering = ['type']
        verbose_name = 'Alert'
        verbose_name_plural = 'Alerts'