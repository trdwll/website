# Generated by Django 3.1 on 2020-10-27 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_post_keywords'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='keywords',
            field=models.CharField(blank=True, help_text='SEO keywords to help get more exposure.', max_length=512, null=True),
        ),
    ]