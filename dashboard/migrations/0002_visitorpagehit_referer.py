# Generated by Django 3.1 on 2020-11-21 01:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='visitorpagehit',
            name='referer',
            field=models.CharField(default='', help_text='The page that this visitor came from.', max_length=150),
        ),
    ]