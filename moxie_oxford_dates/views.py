import json
from datetime import datetime, timedelta

from flask import request, url_for, jsonify, make_response

from moxie.core.views import ServiceView, accepts
from moxie.core.exceptions import BadRequest
from moxie.core.representations import JSON, HAL_JSON
from .services import DatesService 


class Today(ServiceView):
    """View that exposes today's date
    """

    expires = datetime.utcnow().replace(hour=23, minute=59, second=59)

    def handle_request(self):
        dates_service = DatesService.from_context()
        components = dates_service.get_today_components()
        formatted_date = dates_service.get_formatted_date(components)
        return {'today': formatted_date, 'components': components}

    @accepts(HAL_JSON, JSON)
    def as_json(self, response):
        return jsonify({
            'today': response['today'],
            'components': response['components'],
            '_links': {
                'self': {
                    'href': url_for(request.url_rule.endpoint)
                }
            }
        })

    @accepts('application/javascript')
    def as_jsonp(self, result):
        callback = request.args.get('callback', 'callback')
        content = {
            'today': result['today'],
            'components': result['components'],
        }
        jsonp = "{method}({js});".format(method=callback,
                                         js=json.dumps(content))
        response = make_response(jsonp)
        response.headers['Content-Type'] = 'application/javascript'
        return response


class Date(ServiceView):

    expires = timedelta(days=10)    # far

    def handle_request(self, year, month, day):
        dates_service = DatesService.from_context()
        try:
            date = datetime(int(year), int(month), int(day))
        except ValueError as ve:
            raise BadRequest(message=ve.message)
        components = dates_service.get_ox_components(date)
        return {
            'formatted': dates_service.get_formatted_date(components),
            'components': components,
            '_links': {
                'self': {
                    'href': url_for(request.url_rule.endpoint, year=year, month=month, day=day)
                }
            }
        }
