from django.db import models


# The overall count of hits to a page.
class GlobalPageHit(models.Model):
    created = models.DateTimeField(auto_now_add=True, help_text='When the page was hit (viewed) for the first time.')
    modified = models.DateTimeField(auto_now=True, help_text='When the page was hit (viewed) for the x time.')
    page_url = models.URLField(help_text='The url that was accessed.')
    hit_count = models.PositiveIntegerField(default=0, help_text='The amount of times that the page has been accessed.')

    # TODO: class Meta

    def __str__(self):
        return str(self.page_url)

# The actual visitor of the website.
class Visitor(models.Model):
    created = models.DateTimeField(auto_now_add=True, help_text='When the visitor viewed the site for the first time.')
    ip_address = models.GenericIPAddressField(help_text='The IP address of the visitor.')
    ip_country = models.CharField(max_length=100, help_text='The country location of the ip address.')
    last_visit = models.DateTimeField(auto_now=True, help_text='The last time that the visitor visited the site.')

    # TODO: class Meta

    def __str__(self):
        return str(self.ip_address)


# A page that the visitor has viewed.
class VisitorPageHit(models.Model):
    created = models.DateTimeField(auto_now_add=True, help_text='When the visitor viewed the page.')
    visitor = models.ForeignKey(Visitor, on_delete=models.CASCADE, help_text='The visitor that has visited this page.')
    page_url = models.URLField(help_text='The url that was accessed.')
    hit_count = models.PositiveIntegerField(default=0, help_text='The amount of times that the page has been accessed by the visitor.')

    # TODO: class Meta

    def __str__(self):
        return str(self.page_url)


class GlobalPageHitSummary(GlobalPageHit):
    class Meta:
        proxy = True
        verbose_name = 'Global Page Hit Summary'
        verbose_name_plural = 'Global Page Hits Summary'

class VisitorSummary(Visitor):
    class Meta:
        proxy = True
        verbose_name = 'Visitor Summary'
        verbose_name_plural = 'Visitors Summary'

class VisitorPageHitSummary(VisitorPageHit):
    class Meta:
        proxy = True
        verbose_name = 'Visitor Page Hit Summary'
        verbose_name_plural = 'Visitor Page Hits Summary'