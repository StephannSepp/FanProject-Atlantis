from flask import Blueprint


blueprint = Blueprint(
    "project", __name__,
    url_prefix="/project",
    template_folder="templates",
    static_folder="static",
    static_url_path="project/static"
)
