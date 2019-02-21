import requests

forecast_request = "https://api.darksky.net/forecast/"

def get_forecast(api_key, lat, lng):
    url = forecast_request + api_key + "/" + lat + "," + lng
    print(url)
    params = {"units": "si", "exclude": "minutely,hourly,daily,alerts,flags"}
    r = requests.get(url, params)
    return r.json()
