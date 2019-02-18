import busbiel
import display
from departureextractor import DepartureTimeExtractor

html_doc = busbiel.load_timetable_html("line_25_04", "s_bibliothek", "forward")

departureExtractor = DepartureTimeExtractor(html_doc)

print(departureExtractor.nextdepartures())
print(departureExtractor.timetable())
display.generateimage(departureExtractor.nextdepartures())