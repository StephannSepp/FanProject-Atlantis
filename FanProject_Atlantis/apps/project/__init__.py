from flask import Blueprint
from .models import Project

blueprint = Blueprint(
    "project", __name__,
    url_prefix="/project",
    template_folder="templates",
    static_folder="static",
    static_url_path="project/static"
)
