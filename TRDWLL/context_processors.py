from .utils import get_version_checksum
from blog.models import Post
from experiments.models import Experiment

def get_posts():
    archive = {}

    for post in Post.objects.filter(is_published=True).order_by('-published_date'):
        archive.setdefault(post.published_date.year, []).append(post)

    return archive

def get_experiments():
    archive = {}

    for experiment in Experiment.objects.filter(is_published=True).order_by('-published_date'):
        archive.setdefault(experiment.published_date.year, []).append(experiment)

    return archive

def global_settings(request):
    return {
        'SITE_VERSION': get_version_checksum(),
        'POSTS_HOMEPAGE': get_posts(),
        'EXPERIMENTS': get_experiments()
    }