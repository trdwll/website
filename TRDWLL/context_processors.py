from .utils import get_version_checksum
from blog.models import Post
from experiments.models import Experiment
from TRDWLL.models import Alert


def global_settings(request):
    return {
        'SITE_VERSION': get_version_checksum(),
        'ALERTS': Alert.print_alerts(request)
    }