from bs4 import BeautifulSoup
import re
from collections import namedtuple

departures = namedtuple('Timetable', ['nextdepartures', 'departuretimes'])


def extract_departures(html_doc):
    soup = BeautifulSoup(html_doc, 'html.parser')
    nextdepartures = parse_nextdepartures(soup)
    timetable = parse_timetable(soup)
    return departures(nextdepartures, timetable)

def parse_nextdepartures(soup):
    next_departures = soup.find("td", class_="next").get_text()
    return [int(i) for i in next_departures.split('min') if i != '']

def parse_timetable(soup):
    tablerows = soup.find_all('table')[1].find_all('tr', class_=re.compile("even|odd"))
    # strip the last four rows, as they don't contain times
    usedtablerows = tablerows[:len(tablerows)-4]  
    timetable = []
    for row in usedtablerows:
        cells = row.find_all("td")
        hour = cells[0].get_text().strip()
        minutes = cells[1].get_text().strip().split(" ")
        timetable.append((hour, minutes))
    return timetable
        
