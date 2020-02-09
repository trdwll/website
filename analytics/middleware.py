from .models import GlobalPageHit, Visitor, VisitorPageHit
from django.db.models import F
from django.urls import reverse
from django.conf import settings

from ipware import get_client_ip
import ipinfo

class PageViewsMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # If the requested url isn't in the admin panel
        if not reverse('admin:index') in request.path or reverse('admin:index') + 'login/' in request.path or request.path == reverse('admin:index'):
            
            # Create the GlobalPageHit
            page_hit, page_hit_created = GlobalPageHit.objects.get_or_create(page_url=request.path)
            page_hit.hit_count = F('hit_count') + 1
            page_hit.save()

            # Create the Visitor
            visitor_ip = get_client_ip(request)
            visitor, visitor_created = Visitor.objects.get_or_create(ip_address=visitor_ip[0]) 

            # if the ip is not localhost then do a lookup of the country for the ip
            if visitor_ip[0] not in ('localhost', '127.0.0.1'):
                handler = ipinfo.getHandler(settings.IPINFO_API_KEY)
                details = handler.getDetails(str(visitor_ip[0]))
                if details.country_name is not None:
                    visitor.ip_country = details.country_name
            
            visitor.save()

            # Create the VisitorPageHit
            visitor_page_hit, visitor_page_hit_created = VisitorPageHit.objects.get_or_create(page_url=request.path, visitor=visitor)
            visitor_page_hit.hit_count = F('hit_count') + 1
            visitor_page_hit.save() 

        return self.get_response(request)

        