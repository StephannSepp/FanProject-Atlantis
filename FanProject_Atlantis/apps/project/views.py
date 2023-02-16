from cachetools import cached
from cachetools import TTLCache
from firebase_admin import firestore
from flask import abort
from flask import render_template
from flask import url_for

from . import blueprint
from FanProject_Atlantis import firebase


@cached(cache=TTLCache(maxsize=8, ttl=600))
def get_projects(limit=None) -> list:
    projects_ref = firebase.collection("projects")
    docs = projects_ref.order_by("date_start", direction=firestore.Query.DESCENDING).limit(limit).get()
    projects = [doc.to_dict() for doc in docs]
    return projects


@blueprint.route("/api", methods=["GET"])
def project_api():
    try:
        projects = get_projects(limit=5)
    except Exception as exce:
        # TODO: error handling
        print(exce)
        projects = None

    return render_template("recentProjects.html", projects=projects)


@blueprint.route("/")
@blueprint.route("/<project_id>")
def project_page(project_id: str=None):
    if project_id is None:
        try:
            projects = get_projects()
        except Exception as exce:
            # TODO: error handling
            print(exce)
            projects = None
        return render_template("projects.html", projects=projects)

    try:
        return render_template(f"{project_id}.html")
    except Exception as exec:
        # TODO: error handling
        print(exec)
        abort(404)


@blueprint.route("/gawr-gura-birthday-2022")
def project_2022_bday():
    return render_template("2022bday.html")


@blueprint.route("/gawr-gura-birthday-2023")
def project_2023_bday():
    return render_template("2023bday.html")
