from blog.models import Post
from experiments.models import Experiment
from TRDWLL.models import Alert


def global_settings(request):
    return {
        'ALERTS': Alert.print_alerts(request),
        'NOTICES': Alert.print_alerts(request, True),
        'theme': request.COOKIES.get('theme', 'light')
    }