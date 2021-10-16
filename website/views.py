from flask import Blueprint, render_template
from bs4 import BeautifulSoup
import requests
import re
from .newsapi import get_news

views = Blueprint("views", __name__)


@views.route("/")
def home():
    return render_template("index.html")

@views.route("/covid")
def covid():
    url = "https://www.worldometers.info/coronavirus/"
    content = requests.get(url)

    soup = BeautifulSoup(content.text, 'html.parser')

    span = soup.find_all('div', { 'class': 'maincounter-number'})
    string = str(span)
    pattern = re.compile('<span>(.*)</span>')
    results = re.findall(pattern, string)
    print(results)
    

    

    return render_template("covid.html", search=get_news("covid"))

@views.route("/natural-disasters")
def nat_disasters():
    return render_template("nat_disasters.html")
