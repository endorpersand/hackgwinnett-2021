from flask import Blueprint, render_template
from bs4 import BeautifulSoup
import requests
import re
from .newsapi import get_news
from .covid_data import headings, data
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
    stats = re.findall(pattern, string)
    stats = {
        'Total Coronavirus Cases': stats[0],
        'Total Deaths': stats[1],
    } 

    changes = soup.find_all('strong')
    pattern = re.compile('<strong>(.* new cases)</strong>') 
    changes = re.findall(pattern, str(changes))
    print(changes)  

    return render_template("covid.html", search=get_news("covid-19"), stats=stats, covid_data={"headings": headings, 'data': data})

@views.route("/nat-disasters")
def nat_disasters():
    return render_template("nat_disasters.html")
