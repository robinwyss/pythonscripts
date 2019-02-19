from BusTimetable import busbiel, extract_departures 
from display import generateimage
from datetime import time

html_doc = busbiel.load_timetable_html("line_25_04", "s_bibliothek", "forward")

departures = extract_departures(html_doc)

print(departures.nextdepartures)
print(departures.departuretimes)

times = []
for (hour, minutes) in departures.departuretimes:
    for minute in minutes:
        times.append(time(int(hour), int(minute)))

generateimage(departures.nextdepartures, departures.departuretimes, None)