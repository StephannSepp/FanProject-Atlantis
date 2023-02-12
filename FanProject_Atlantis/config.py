import os


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
    # SQLAlchemy
    SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI")


class DevelopmentConfig(BaseConfig):
    # from dotenv import load_dotenv
    # load_dotenv()
    SECRET_KEY = os.getenv("SECRET")
    # OAuth Variable
    CLIENT_ID = os.getenv("CLIENT_ID")
    CLIENT_SECRET = os.getenv("CLIENT_SECRET")
    # SQLAlchemy
    SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI")
