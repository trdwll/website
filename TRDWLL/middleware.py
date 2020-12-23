from .models import VisitorPageHit
from django.db.models import F
from django.urls import reverse
from django.conf import settings

from ipware import get_client_ip
import ipinfo
import bleach

class PageViewsMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        requested_url = bleach.clean(request.path)
        
        if reverse('admin:index') in requested_url or \
            reverse('admin:index') + 'login/' in requested_url or \
            requested_url is reverse('admin:index') or \
            'dashboard' in requested_url or \
            'favicon' in requested_url or \
            'robots.txt' in requested_url or \
            '__debug__' in requested_url:
            return self.get_response(request)

        # Create the VisitorPageHit (adds a new entry for each visitor that visits a page)
        visitor_ip = get_client_ip(request)[0]
        visitor_page_hit = VisitorPageHit(page_url=requested_url, ip_address=visitor_ip, user_agent=request.META['HTTP_USER_AGENT'], referer=request.META.get('HTTP_REFERER', ''), theme=request.COOKIES.get('theme', 'light'))

        if visitor_ip not in ('localhost', '127.0.0.1'):
            handler = ipinfo.getHandler(settings.IPINFO_API_KEY)
            details = handler.getDetails(str(visitor_ip))
            if details.country_name is not None:
                visitor_page_hit.ip_country = details.country_name
            if details.country is not None:
                visitor_page_hit.country_code = details.country

        visitor_page_hit.save() 

        return self.get_response(request)