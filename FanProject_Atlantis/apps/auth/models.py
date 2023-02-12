from flask_login import UserMixin


class User(UserMixin):
    def __init__(self, discord_id, discord_username, discord_avatar):
        self.id = discord_id
        self.username = discord_username
        self.avatar = discord_avatar
