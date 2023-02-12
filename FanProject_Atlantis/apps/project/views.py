from flask import render_template
from . import blueprint
from . import Project
from FanProject_Atlantis import db


@blueprint.route("/api", methods=["GET"])
def project_api():
    try:
        projects = db.session.execute(db.select(Project).order_by(Project.DateStart.desc()).limit(5)).scalars().all()
    except Exception as exce:
        # :TODO: exception handling
        print(exce)
        projects = None

    return render_template("recentProjects.html", projects=projects)


@blueprint.route("/gawr-gura-birthday-2022")
def project_2022_bday():
    return render_template("2022bday.html")


@blueprint.route("/gawr-gura-birthday-2023")
def project_2023_bday():
    return render_template("2023bday.html")
