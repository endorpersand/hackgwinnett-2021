from bs4 import BeautifulSoup
import requests
import re

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

def stringify(h):
    contents = h.contents
    if any(not isinstance(e, str) for e in contents):
        contents = [
            e if isinstance(e, str)
            else stringify(e)
            for e in contents
        ]
    return " ".join(contents).strip()

# GET TABLE
table = soup.select_one("#main_table_countries_today")
thead, tbody = soup.select_one("thead"), soup.select("tbody")[0]

headings = [stringify(h) for h in thead.select("th")[1:5]]
data_rows = tbody.select("tr")[7:-1]
data = [[stringify(e) for e in r.select("td")[1:5]] for r in data_rows]

for r in data:
    numerical_row = r[1:]

    numerical_row = [
        0 if e == ''
        else int(e.replace(",", ""))
        for e in numerical_row
        ]

    r[1:] = numerical_row

data.sort(key=lambda r: r[1], reverse=True)