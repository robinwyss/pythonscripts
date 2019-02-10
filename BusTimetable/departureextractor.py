from bs4 import BeautifulSoup
import re

class DepartureTimeExtractor:
    def __init__(self, html_doc):
        self.soup = BeautifulSoup(html_doc, 'html.parser')

    def nextdepartures(self):
        next_departures = self.soup.find("td", class_="next").get_text()
        return [int(i) for i in next_departures.split('min') if i != '']

    def timetable(self):
        #self.soup.find_all('table')
        tablerows = self.soup.find_all('table')[1].find_all('tr', class_=re.compile("even|odd"))
        for row in tablerows:
            print(row.get_text())
        return tablerows
        
