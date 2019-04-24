from .utils import get_version_checksum

def global_settings(request):
    return {
        'SITE_VERSION': get_version_checksum(),
    }