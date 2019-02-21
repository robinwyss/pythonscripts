from datetime import time

def convert_daparturetimes_to_list(departuretimes):
    times = []
    for (hour, minutes) in departuretimes:
        for minute in minutes:
            times.append(time(int(hour), int(minute)))
    return times

