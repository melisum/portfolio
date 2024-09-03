
import requests


id={"clientId": "66d1af3f9ac4835cdbb43485"}

def check_breweries(text):
    brewery = requests.get(url=f"https://api.openbrewerydb.org/v1/breweries?by_city={text.lower()}&per_page=3")
    brewery.raise_for_status()
    info = brewery.json()
    print(len(info))
    for _ in range(len(info)):
        name= info[_]["name"]
        url = info[_]["website_url"]
        print(name, url)

name=input("Enter a city name: \n")
check_breweries(text=name)