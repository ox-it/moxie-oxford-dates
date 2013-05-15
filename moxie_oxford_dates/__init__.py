from flask import Blueprint, request
from flask.helpers import make_response

from moxie.core.representations import HALRepresentation
from .views import Today, Date


def create_blueprint(blueprint_name, conf):
    oxford_dates_blueprint = Blueprint(blueprint_name, __name__, **conf)

    oxford_dates_blueprint.add_url_rule('/', view_func=get_routes)

    oxford_dates_blueprint.add_url_rule('/today',
            view_func=Today.as_view('today'))
    oxford_dates_blueprint.add_url_rule('/<year>-<month>-<day>',
            view_func=Date.as_view('date'))
    return oxford_dates_blueprint


def get_routes():
    path = request.path
    representation = HALRepresentation({})
    representation.add_curie('hl', 'http://moxie.readthedocs.org/en/latest/http_api/oxford_dates.html#{rel}')
    representation.add_link('self', '{bp}'.format(bp=path))
    representation.add_link('hl:today', '{bp}today'.format(bp=path),
                            title='Today date')
    representation.add_link('hl:date', '{bp}{{yyyy}}-{{mm}}-{{dd}}'.format(bp=path),
                            templated=True, title="Format arbitrary date")
    response = make_response(representation.as_json(), 200)
    response.headers['Content-Type'] = "application/json"
    return response
