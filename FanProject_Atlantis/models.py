import firebase_admin
import platform

from flask_babel import Babel
from flask_login import LoginManager
from firebase_admin import credentials
from firebase_admin import firestore


babel = Babel()
login_manager = LoginManager()
if platform.system().capitalize() == "Windows":
    path = r"etc\secrets\2034ca177738f5073c7668bd11dfcbcfd50146cb.json"
else:
    path = "/etc/secrets/credential.json"
cred = credentials.Certificate(path)
firebase_admin.initialize_app(cred)
firebase = firestore.client()
