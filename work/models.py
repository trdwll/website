from django.db import models
from django.urls import reverse
from django.db.models.signals import pre_save

from tinymce.models import HTMLField

from TRDWLL.signals import create_redirect

class WorkProduct(models.Model):
    is_published = models.BooleanField(default=True, help_text='Is this project public?')
    title = models.CharField(max_length=256, help_text='What\'s the name of this product?')
    slug = models.SlugField(unique=True)
    release_date = models.DateTimeField()
    keywords = models.CharField(max_length=512, help_text='SEO keywords to help get more exposure.', blank=True, null=True)
    body = HTMLField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('work_product_page', kwargs={'slug': self.slug})

    class Meta: 
        db_table = 'work_product'
        ordering = ['-release_date']
        verbose_name = 'Work Product'
        verbose_name_plural = 'Work Products'


pre_save.connect(create_redirect, sender=WorkProduct)