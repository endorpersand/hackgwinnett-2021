from flask import Blueprint, render_template
from .newsapi import get_news

views = Blueprint("views", __name__)


@views.route("/")
def home():
    return render_template("index.html")

@views.route("/covid")
def covid():
    return render_template("covid.html", search=get_news("covid"))

@views.route("/natural-disasters")
def nat_disasters():
    return render_template("nat_disasters.html")
