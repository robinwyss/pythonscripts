import requests
from cachetools import cached, TTLCache

forecast_request = "https://api.darksky.net/forecast/"


@cached(cache=TTLCache(maxsize=1024, ttl=1800))
def get_forecast(api_key, lat, lng):
    url = forecast_request + api_key + "/" + lat + "," + lng
    print(url)
    params = {"units": "si", "exclude": "minutely,alerts,flags"}
    r = requests.get(url, params)
    return r.json()
