from FanProject_Atlantis import db


class Project(db.Model):

    __table_args__ = {"schema": "fanproject-atlantis"}
    __tablename__ = "projects"

    Id = db.Column(db.Integer(), primary_key=True)
    Name = db.Column(db.String())
    DateStart = db.Column(db.Date())
    DateEnd = db.Column(db.Date())
    DetailedName = db.Column(db.String())