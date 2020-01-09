from .utils import get_version_checksum
from blog.models import Post
from experiments.models import Experiment

from django.db.models.functions import ExtractYear

def get_entries(obj):
    nobj = {}
    
    for value in obj:
        nobj.setdefault(value['year'], []).append(value)

    return nobj

def global_settings(request):
    return {
        'SITE_VERSION': get_version_checksum(),
        'POSTS_HOMEPAGE': get_entries(Post.objects.filter(is_published=True).order_by('-published_date').annotate(year=ExtractYear('published_date')).values()),
        'EXPERIMENTS': get_entries(Experiment.objects.filter(is_published=True).order_by('-published_date').annotate(year=ExtractYear('published_date')).values()),
    }