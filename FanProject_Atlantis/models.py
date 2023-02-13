import os
import boto3
from flask_babel import Babel
from flask_login import LoginManager


babel = Babel()
login_manager = LoginManager()
dynamodb = boto3.resource(
    "dynamodb",
    region_name="ap-southeast-1",
    aws_access_key_id=os.getenv("DYNAMODB_ACCESS_KEY"),
    aws_secret_access_key=os.getenv("DYNAMODB_SECRET_KEY"),
)
