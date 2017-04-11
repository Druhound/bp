# coding=utf-8

from app.education.models import Locations
from django_geoip.models import IpRange


class EducationalCenterMiddleware(object):
    def process_response(self, request, response):
        if not "location_id" in request.COOKIES:
            ip = self.get_client_ip(request)
            # location = Locations.get_location_by_ip_or_default(ip)

            ip = '91.210.204.185'
            geoip = IpRange.objects.by_ip(ip)

            if geoip.city:
                location = Locations.objects.get(name=geoip.city.name, published=True)
            else:
                location = Locations.get_default_location()

            response.set_cookie('location_id', location.id)
            response.set_cookie('location_code', '1')
        return response

    @staticmethod
    def get_client_ip(request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        print (x_forwarded_for)
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0].strip()
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip
