import datetime as dt
import bs4
import requests
import io
import csv
import dataclasses

current_date = dt.date.today() - dt.timedelta(days=1)
past_date = current_date - dt.timedelta(days=30)


url = "https://covid.ourworldindata.org/data/owid-covid-data.csv"
r = requests.get(url)
file = io.StringIO(r.text)

def get_reader(file: io.StringIO):
    file.seek(0)
    return csv.DictReader(file)

def restrict_dict(dct: dict):
    return {
        k: dct[k] for k in [
            "total_cases", "total_deaths", "population"
        ]
    }
current_data = {r["location"]: restrict_dict(r) for r in get_reader(file) if r["date"] == str(current_date)}
past_data = {r["location"]: restrict_dict(r) for r in get_reader(file) if r["date"] == str(past_date)}

@dataclasses.dataclass
class CountryCase:
    country: str
    current_cases: float
    past_cases: float
    current_deaths: float
    past_deaths: float
    pop: float

    def __post_init__(self):
        self.current_cases = 0 if self.current_cases == '' else float(self.current_cases)
        self.past_cases = 0 if self.past_cases == '' else float(self.past_cases)
        self.current_deaths = 0 if self.current_deaths == '' else float(self.current_deaths)
        self.past_deaths = 0 if self.past_deaths == '' else float(self.past_deaths)
        self.pop = 0 if self.pop == '' else float(self.pop)

    @property
    def delta_cases(self):
        return self.current_cases - self.past_cases

    @property
    def delta_deaths(self):
        return self.current_deaths - self.past_deaths
        
    @property
    def delta_case_rate(self):
        return self.delta_cases / self.pop

    @property
    def delta_death_rate(self):
        return self.delta_deaths / self.pop

countries = set(k for k, v in current_data.items() if v["population"] != '') & set(k for k, v in past_data.items() if v["population"] != '')
country_rates = [CountryCase(c, current_data[c]["total_cases"], past_data[c]["total_cases"], current_data[c]["total_deaths"], past_data[c]["total_deaths"], current_data[c]["population"]) for c in countries]
country_rates.sort(key=lambda e: e.delta_death_rate, reverse=True)


