import os

from flask import abort
from flask import current_app
from flask import redirect
from flask import request
from flask import session
from flask import url_for
from flask_login import current_user
from flask_login import login_user
from flask_login import logout_user
from requests_oauthlib import OAuth2Session

from . import blueprint
from . import User
from FanProject_Atlantis import login_manager


os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
TOKEN_URL = "https://discordapp.com/api/oauth2/token"
AUTHORIZE_URL = "https://discordapp.com/api/oauth2/authorize"
SCOPE = ["identify", "guilds"]


@blueprint.route("/")
def index():
    """ Test page """
    if current_user.is_authenticated:
        return f"Hello, {current_user.username}!<img src='https://cdn.discordapp.com/avatars/{current_user.id}/{current_user.avatar}' alt='Discord Avatar' \>"
    return "Hello, Anonymous!"


@blueprint.route("/login")
def login():
    discord_oauth = OAuth2Session(current_app.config["CLIENT_ID"], redirect_uri=url_for("auth.oauth_callback", _external=True), scope=SCOPE)
    login_url, state = discord_oauth.authorization_url(AUTHORIZE_URL)
    session["oauth_state"] = state
    return redirect(login_url)


@blueprint.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("home.home"))


@blueprint.route("/oauth_callback")
def oauth_callback():
    if session.get("oauth_state") is None:
        abort(400)

    discord_oauth = OAuth2Session(
        current_app.config["CLIENT_ID"],
        redirect_uri=url_for("auth.oauth_callback", _external=True),
        state=session["oauth_state"]
    )
    token = discord_oauth.fetch_token(
        TOKEN_URL,
        client_secret=current_app.config["CLIENT_SECRET"],
        authorization_response=request.url,
    )
    session["oauth_token"] = token
    discord_user = discord_oauth.get("https://discord.com/api/users/@me").json()
    user_info = {
        "discord_id": discord_user["id"],
        "discord_username": discord_user["username"],
        "discord_avatar": discord_user["avatar"],
    }
    session["user_info"] = user_info
    user = User(**user_info)
    login_user(user)
    return redirect(url_for("home.home"))


@login_manager.user_loader
def load_user(user_id):
    user_info = session.get("user_info")
    if user_info and user_info.get("discord_id") == user_id:
        return User(**user_info)

    return None
