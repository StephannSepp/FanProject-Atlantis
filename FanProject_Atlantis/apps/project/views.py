from botocore.exceptions import ClientError
from flask import render_template
from . import blueprint
from FanProject_Atlantis import dynamodb


@blueprint.route("/api", methods=["GET"])
def project_api():
    try:
        resp = dynamodb.Table("Projects").scan(
            Limit=5,
            AttributesToGet=[
                "project_name", "detailed_name", "date_start", "date_end"
            ]
        )
    except ClientError as exce:
        assert exce.response["Error"]["Code"] == "ResourceNotFoundException"
        projects = None
    else:
        projects = resp["Items"]

    return render_template("recentProjects.html", projects=projects)


@blueprint.route("/gawr-gura-birthday-2022")
def project_2022_bday():
    return render_template("2022bday.html")


@blueprint.route("/gawr-gura-birthday-2023")
def project_2023_bday():
    return render_template("2023bday.html")
