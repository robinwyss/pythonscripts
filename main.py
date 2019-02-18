from BusTimetable import busbiel, extract_departures 

html_doc = busbiel.load_timetable_html("line_25_04", "s_bibliothek", "forward")

departures = extract_departures(html_doc)

print(departures.nextdepartures)
print(departures.table)