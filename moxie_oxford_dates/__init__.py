from flask import Blueprint

from .views import Today


def create_blueprint(blueprint_name):
    oxford_dates_blueprint = Blueprint(blueprint_name, __name__)

    oxford_dates_blueprint.add_url_rule('/today',
            view_func=Today.as_view('today'))
    return oxford_dates_blueprint
