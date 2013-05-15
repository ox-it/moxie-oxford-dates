from datetime import datetime

from flask import request, url_for

from moxie.core.views import ServiceView
from .services import DatesService 


class Today(ServiceView):
    """View that exposes today's date
    """

    def handle_request(self):
        dates_service = DatesService.from_context()
        components = dates_service.get_today_components()
        return {
            'today': dates_service.get_formatted_date(components),
            'components': components,
            '_links': {
                'self': {
                    'href': url_for(request.url_rule.endpoint)
                }
            }
        }


class Date(ServiceView):

    def handle_request(self, year, month, day):
        dates_service = DatesService.from_context()
        components = dates_service.get_ox_components(datetime(int(year), int(month), int(day)))
        return {
            'formatted': dates_service.get_formatted_date(components),
            'components': components,
            '_links': {
                'self': {
                    'href': url_for(request.url_rule.endpoint, year=year, month=month, day=day)
                }
            }
        }
