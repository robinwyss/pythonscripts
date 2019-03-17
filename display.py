from PIL import Image, ImageDraw, ImageFont
import sys
from collections import namedtuple
from datetime import datetime

imgwidth = 250
imgheight = 122

# letter size ca. 5x7 (depends on char)
lineheight = 10
charwidth = 6
margin = 2

# use a truetype font
font = ImageFont.truetype("VeraMono.ttf", 10)


def generateimage(nextdepartures, departuretimes, forecast):
    im = Image.new('1', (imgwidth, imgheight), 255)
    draw = ImageDraw.Draw(im)
    # left part
    draw_nextdepartures(draw, nextdepartures)
    draw_departuretimes(draw, departuretimes)
    # right part
    draw_time(draw)
    draw_date(draw)
    draw_forecast(draw, forecast)
    im.save('img.png', 'PNG')

def draw_nextdepartures(draw, nextdepartures):
    text = ""
    for departure in nextdepartures:
        text += str(departure) + ' min '
    draw_text(draw, (margin, margin ), text)

def draw_departuretimes(draw, departuretimes):
    ydelta = lineheight + (margin * 3)
    for (hour, minutes) in departuretimes:
        draw_text(draw, (margin, margin + ydelta), hour)
        xdelta = charwidth # add some space before the minutes
        for minute in minutes:
            xdelta += (3 * charwidth)
            draw_text(draw, (margin + xdelta, margin + ydelta), minute)
        ydelta += lineheight

def draw_time(draw):
    timestr = datetime.now().strftime("%H:%M")
    draw_text(draw, (imgwidth - (6 * charwidth) - margin, margin), timestr)

def draw_date(draw):
    timestr = datetime.now().strftime("%d.%m.%y")
    draw_text(draw, (imgwidth - (9 * charwidth) - margin, margin + lineheight), timestr)

def draw_forecast(draw, forecast):
    ydelta = lineheight + (margin * 10)
    current = forecast["currently"]
    startx = imgwidth / 2
    draw_text(draw, (startx, ydelta), current["summary"])
    draw_text(draw, (startx, ydelta + lineheight), str(current["temperature"]) + "°")
    im = Image.open("icons/cloud.xbm")
    draw.bitmap((startx, ydelta + lineheight * 2), im)


def draw_text(draw, pos, text):
    draw.text(pos, text, font=font)
