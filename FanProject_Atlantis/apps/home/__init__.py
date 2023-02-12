from flask import Blueprint


blueprint = Blueprint(
    "home", __name__,
    url_prefix="/",
    template_folder="templates",
    static_folder="static",
    static_url_path="home/static"
)
