from flask import Blueprint
from .models import User

blueprint = Blueprint(
    "auth", __name__,
    url_prefix="/auth",
    template_folder="templates",
    static_folder="static",
    static_url_path="auth/static"
)
