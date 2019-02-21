from BusTimetable import busbiel, extract_departures 
from display import generateimage
from Utils import convert_daparturetimes_to_list
from Weather import get_forecast
import config

# get bus departures
html_doc = busbiel.load_timetable_html("line_25_04", "s_bibliothek", "forward")
departures = extract_departures(html_doc)

# get weather forecast
forecast = get_forecast(config.darksky_api_key, "47.1402", "7.2439")
print(forecast)

print(departures.nextdepartures)
print(departures.departuretimes)
print(convert_daparturetimes_to_list(departures.departuretimes))

generateimage(departures.nextdepartures, departures.departuretimes, forecast)