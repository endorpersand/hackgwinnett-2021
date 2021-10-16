from flask import Blueprint, render_template
from bs4 import BeautifulSoup
import requests
import re
from .newsapi import get_news
import os

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
    print("\n\n\n\n")

    changes = soup.find_all('strong')
    pattern = re.compile('<strong>(.* new cases)</strong>') 
    changes = re.findall(pattern, str(changes))
    print(changes)  

    return render_template("covid.html", search=get_news("covid-19"), stats=stats)

@views.route("/nat-disasters")
def nat_disasters():
    image_shown = False
    url = "https://www.ncdc.noaa.gov/monitoring-content/billions/images/2021-billion-dollar-disaster-map.png"
    response = requests.get(url)
    if response.status_code == 200:
        with open("website/static/temp.jpg", 'wb') as f:
            f.write(response.content)
            image_shown = True

    fire_url = 'https://disasterphilanthropy.org/disaster/2021-north-american-wildfire-season/'
    
    content = requests.get(fire_url)
    soup = BeautifulSoup(content.text, 'html.parser')


    
    

    return render_template("nat_disasters.html", search=get_news("earthquake"), image_shown=image_shown)
