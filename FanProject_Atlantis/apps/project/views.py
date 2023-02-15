from cachetools import cached
from cachetools import TTLCache
from firebase_admin import firestore
from flask import render_template

from . import blueprint
from FanProject_Atlantis import firebase


@cached(cache=TTLCache(maxsize=8, ttl=600))
def get_recent_projects() -> list:
    projects_ref = firebase.collection("projects")
    docs = projects_ref.order_by("date_start", direction=firestore.Query.DESCENDING).limit(5).get()
    projects = [doc.to_dict() for doc in docs]
    return projects


@blueprint.route("/api", methods=["GET"])
def project_api():
    try:
        projects = get_recent_projects()
    except Exception as exce:
        # TODO: error handling
        print(exce)
        projects = None

    return render_template("recentProjects.html", projects=projects)


@blueprint.route("/gawr-gura-birthday-2022")
def project_2022_bday():
    return render_template("2022bday.html")


@blueprint.route("/gawr-gura-birthday-2023")
def project_2023_bday():
    return render_template("2023bday.html")
