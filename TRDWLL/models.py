from django.db import models

from ckeditor_uploader.fields import RichTextUploadingField

class About(models.Model):
    body = RichTextUploadingField()

    def __str__(self):
        return 'About Me'

    class Meta:
        db_table = 'about_entry'