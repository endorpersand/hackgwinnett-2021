from pathlib import Path
import datetime as dt
import json
import requests

with open(Path("secret") / "newsapi.txt") as f:
    API_KEY = f.read()

def get_news(query: str, n_articles: int = 5) -> list:
    week_ago = dt.date.today() - dt.timedelta(days=7)
    r = requests.get(f"""https://gnews.io/api/v4/search?q="{query}"&lang=en&token={API_KEY}&from={week_ago}&max={n_articles}""")
    if r.ok:
        news = r.json()
        return news["articles"]

    return []