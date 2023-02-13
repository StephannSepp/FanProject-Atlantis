import os
import platform


class BaseConfig(object):
    BLUEPRINTS = [
        "auth",
        "home",
        "project"
    ]
    # Babel Variable
    BABEL_DEFAULT_LOCALE = "zh"
    BABEL_DEFAULT_TIMEZONE = "Asia/Taipei"


class ProductionConfig(BaseConfig):
    SECRET_KEY = os.getenv("SECRET")
    # OAuth Variable
    CLIENT_ID = os.getenv("CLIENT_ID")
    CLIENT_SECRET = os.getenv("CLIENT_SECRET")

    
class DevelopmentConfig(BaseConfig):
    if platform.system().capitalize() == "Windows":
        from dotenv import load_dotenv
        load_dotenv()
        SECRET_KEY = os.getenv("SECRET")
        # OAuth Variable
        CLIENT_ID = os.getenv("CLIENT_ID")
        CLIENT_SECRET = os.getenv("CLIENT_SECRET")
