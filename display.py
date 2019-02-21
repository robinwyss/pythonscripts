from PIL import Image, ImageDraw, ImageFont
import sys
from collections import namedtuple
from datetime import datetime

imgwidth = 296
imgheight = 128

# letter size ca. 5x7 (depends on char)
lineheight = 10
charwidth = 5
margin = 2


def generateimage(nextdepartures, departuretimes, forecast):
    im = Image.new('1', (imgwidth, imgheight), 255)
    draw = ImageDraw.Draw(im)
    draw_nextdepartures(draw, nextdepartures)
    draw_departuretimes(draw, departuretimes)
    draw_time(draw)
    draw_forecast(draw, forecast)
    im.save('img.png', 'PNG')

def draw_nextdepartures(draw, nextdepartures):
    text = ""
    for departure in nextdepartures:
        text += str(departure) + ' min '
    draw.text((margin, margin ), text)

def draw_departuretimes(draw, departuretimes):
    ydelta = lineheight + (margin * 3)
    for (hour, minutes) in departuretimes:
        draw.text((margin, margin + ydelta), hour)
        xdelta = charwidth # add some space before the minutes
        for minute in minutes:
            xdelta += (3 * charwidth)
            draw.text((margin + xdelta, margin + ydelta), minute)
        ydelta += lineheight

def draw_time(draw):
    timestr = datetime.now().strftime("%H:%M")
    draw.text((imgwidth - (6 * charwidth) - margin, margin), timestr)

def draw_forecast(draw, forecast):
    ydelta = lineheight + (margin * 10)
    current = forecast["currently"]
    startx = imgwidth / 2
    draw.text((startx, ydelta), current["summary"])
    draw.text((startx, ydelta + lineheight), str(current["temperature"]) + "°")

