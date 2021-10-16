from pathlib import Path
import datetime as dt
import json
import requests

with open(Path("secret") / "newsapi.txt") as f:
    API_KEY = f.read()

# with open(Path("tester.json")) as f:
#     t = json.load(f)

def get_news(query: str, n_articles: int = 5) -> list:
    # return t["articles"][:n_articles]
    week_ago = dt.date.today() - dt.timedelta(days=7)
    r = requests.get(f"https://newsapi.org/v2/everything?q={query}&from={week_ago}&sortBy=publishedAt&apiKey={API_KEY}")
    if r.ok:
        news = r.json()
        return news["articles"][:n_articles]

    return []