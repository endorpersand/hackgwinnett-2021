import datetime as dt

current_date = dt.date.today()
past_date = current_date - dt.timedelta(days=30)
countries: "list[str]" = []

class CountryCase:
    def __init__(self, country: str):
        self.country = country
        self.case_rates = self.find_rate(country)

    def find_rate(self, country: str) -> "tuple[float, float]":
        # TODO
        current_case = NotImplemented # get current case
        past_case = NotImplemented # get date 30 days ago
        country_pop = NotImplemented

        growth_rate = (current_case-past_case) / 30
        growth_rate_rel_population = growth_rate / country_pop

        return (growth_rate, growth_rate_rel_population)

country_rates = [CountryCase(c) for c in countries]
country_rates.sort(lambda e: e.case_rates[1], reverse=True)


