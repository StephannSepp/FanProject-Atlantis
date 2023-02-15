from importlib import import_module

from flask import Flask
from flask import render_template
from flask import request

from . import config
from .context import inject_variables
from .context import date_fromisoformate
from .context import datetime_fromisoformate
from .models import babel
from .models import firebase
from .models import login_manager


def get_locale():
    return request.accept_languages.best_match(["zh", "en"])


def register_blueprints(app):
    """ Register every views.py file foreach app. """
    for blueprint in app.config["BLUEPRINTS"]:
        module = import_module(f"FanProject_Atlantis.apps.{blueprint}.views")
        app.register_blueprint(module.blueprint)


def create_app(testing=False):
    app = Flask(__name__)
    if testing:
        app.config.from_object(config.DevelopmentConfig())
    else:
        app.config.from_object(config.ProductionConfig())

    app.config["TEMPLATES_AUTO_RELOAD"] = True
    app.jinja_env.auto_reload = True

    app.context_processor(inject_variables)
    app.add_template_filter(date_fromisoformate)
    app.add_template_filter(datetime_fromisoformate)

    # Register error handlers
    app.errorhandler(404)(lambda e: (render_template("404.html"), 404))
    app.errorhandler(500)(lambda e: (render_template("500.html"), 500))

    babel.init_app(app, locale_selector=get_locale)
    login_manager.init_app(app)
    register_blueprints(app)
    return app
