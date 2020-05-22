# web_app/routes/home_routes.py

from flask import Blueprint, render_template

home_routes = Blueprint("home_routes", __name__)


@home_routes.route("/")
def index():
    return render_template("prediction_form.html")


@home_routes.route("/hello")
def hello():
    return "Welcome to my Tweet Predictions app!"


@home_routes.route("/about")
def about():
    about_string = """
    This is a web app designed to take in a user generated tweet
     and see which twitter user is more likely to tweet that text.
    """
    return about_string
