from flask_babel import Babel
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy


babel = Babel()
login_manager = LoginManager()
db = SQLAlchemy()
