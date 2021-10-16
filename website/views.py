from flask import Blueprint, render_template

views = Blueprint("views", __name__)


@views.route("/")
def home():
    return render_template("index.html")

@views.route("/covid")
def covid():
    return render_template("covid.html")

@views.route("/natural-disasters")
def nat_disasters():
    return render_template("nat_disasters.html")
