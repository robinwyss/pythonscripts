import urllib.request



# loads current time table for a given bus line, station and direction as html.
def load_timetable_html(bus_line, station_name, direction ): 
    language = "de" 
    format = "ch.omnitron.schedule.output.OutputWriter" #not sure what this is used or if it is required
    fp = urllib.request.urlopen("http://bus.biel-bienne.info/schedule?l="+language+"&line="+bus_line+"&station="+station_name+"&direction="+direction+"&format="+format)
    mybytes = fp.read()
    html_doc = mybytes.decode("utf8")
    fp.close()
    return html_doc
