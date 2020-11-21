from django.db import models

# The overall count of hits to a page.
class GlobalPageHit(models.Model):
    created = models.DateTimeField(auto_now_add=True, help_text='When the page was hit (viewed) for the first time.')
    modified = models.DateTimeField(auto_now=True, help_text='When the page was hit (viewed) for the x time.')
    page_url = models.CharField(max_length=200, help_text='The url that was accessed.')
    hit_count = models.PositiveIntegerField(default=0, help_text='The amount of times that the page has been accessed.')

    class Meta:
        db_table = 'analytics_globalpagehit'
        ordering = ['-hit_count']

    def __str__(self):
        return str(self.page_url)

# The actual visitor of the website.
class Visitor(models.Model):
    created = models.DateTimeField(auto_now_add=True, help_text='When the visitor viewed the site for the first time.')
    ip_address = models.GenericIPAddressField(help_text='The IP address of the visitor.')
    ip_country = models.CharField(max_length=100, help_text='The country location of the ip address.')
    country_code = models.CharField(max_length=16, help_text='The country location of the ip address (country code).', default='', blank=True)
    user_agent = models.CharField(max_length=300, help_text='The useragent that the visitor is using.')
    last_visit = models.DateTimeField(auto_now=True, help_text='The last time that the visitor visited the site.')

    class Meta:
        db_table = 'analytics_visitor'
        ordering = ['-last_visit']

    def __str__(self):
        return str(self.ip_address)


# A page that the visitor has viewed.
class VisitorPageHit(models.Model):
    created = models.DateTimeField(auto_now_add=True, help_text='When the visitor viewed the page.')
    visitor = models.ForeignKey(Visitor, on_delete=models.CASCADE, help_text='The visitor that has visited this page.')
    page_url = models.CharField(max_length=200, help_text='The url that was accessed.')
    user_agent = models.TextField(help_text='The useragent that the visitor is using.')
    referer = models.CharField(max_length=150, help_text='The page that this visitor came from.', default='', blank=True)

    class Meta:
        db_table = 'analytics_visitorpagehit'
        ordering = ['-created']

    def __str__(self):
        return str(self.page_url)