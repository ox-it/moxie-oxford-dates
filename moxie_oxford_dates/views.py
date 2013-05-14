from datetime import datetime

from moxie.core.views import ServiceView
from .services import DatesService 


class Today(ServiceView):
    """View that exposes today's date
    """

    def handle_request(self):
        dates_service = DatesService.from_context()
        components = dates_service.get_today_components()
        response = {
            'today': dates_service.get_formatted_date(components),
            'components': components
        }
        return response


class Date(ServiceView):

    def handle_request(self, year, month, day):
        dates_service = DatesService.from_context()
        components = dates_service.get_ox_components(datetime(int(year), int(month), int(day)))
        response = {
            'today': dates_service.get_formatted_date(components),
            'components': components
        }
        return response