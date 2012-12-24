from moxie.core.views import ServiceView
from .services import DatesService 


class Today(ServiceView):
    """View that exposes today's date
    """

    def handle_request(self):
        dates_service = DatesService.from_context()
        response = {
            'today': dates_service.get_today_date(),
            'components': dates_service.get_today_components()
        }
        return response
