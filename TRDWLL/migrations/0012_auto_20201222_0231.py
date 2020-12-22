# Generated by Django 3.1 on 2020-12-22 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TRDWLL', '0011_visitorpagehit'),
    ]

    operations = [
        migrations.AddField(
            model_name='alert',
            name='notice_url',
            field=models.CharField(blank=True, help_text='The url that you want to redirect to on the button.', max_length=512, null=True),
        ),
        migrations.AlterField(
            model_name='alert',
            name='type',
            field=models.CharField(choices=[('alert alert-success', 'Success'), ('alert alert-danger', 'Danger'), ('alert alert-warning', 'Warning'), ('alert alert-info', 'Info'), ('indigo', 'Indigo Notice'), ('green', 'Green Notice'), ('red', 'Red Notice'), ('yellow', 'Yellow Notice'), ('blue', 'Blue Notice'), ('purple', 'Purple Notice'), ('pink', 'Pink Notice')], help_text='The style of the alert.', max_length=32),
        ),
    ]