from .utils import get_version_checksum
from blog.models import Post
from experiments.models import Experiment

def get_formatted_data(query):
    archive = {}

    for obj in query:
        archive.setdefault(obj.published_date.year, []).append(obj)

    return archive

def global_settings(request):
    return {
        'SITE_VERSION': get_version_checksum(),
        'POSTS_HOMEPAGE': get_formatted_data(Post.objects.filter(is_published=True).order_by('-published_date')),
        'EXPERIMENTS': get_formatted_data(Experiment.objects.filter(is_published=True).order_by('-published_date'))
    }