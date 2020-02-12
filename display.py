from PIL import Image, ImageDraw, ImageFont
import sys
import platform
from collections import namedtuple
from datetime import datetime
from textwrap import wrap
import screen

imgwidth = 250
imgheight = 128

# letter size ca. 5x7 (depends on char)
lineheight = 10
charwidth = 6
margin = 2

# use a truetype font
font = ImageFont.truetype("VeraMono.ttf", 10)

# icons
iconlookup = {"clear-day": "sun.xbm",
              "clear-night": "moon.xbm",
              "rain": "rain0.xbm",
              "snow": "snow.xbm",
              "sleet": "rain_snow.xbm",
              "wind": "wind.xbm",
              "fog": "cloud_wind.xbm",
              "cloudy": "clouds.xbm",
              "partly-cloudy-day": "cloud_sun.xbm",
              "partly-cloudy-night": "cloud_moon.xbm"}


def displayInfo(nextdepartures, departuretimes, forecast):
    img = generateimage(nextdepartures, departuretimes, forecast)
    img = img.rotate(270, expand=True)
    screen.showImageOnScreen(img)

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
    return im

def draw_nextdepartures(draw, nextdepartures):
    text = ""
    for departure in nextdepartures:
        text += str(departure) + ' min '
    draw_text(draw, (margin, margin +  3), text)

def draw_departuretimes(draw, departuretimes):
    ydelta = lineheight + (margin * 3)
    # only take the five first elements due to space limitations
    for (hour, minutes) in departuretimes[:5]:
        draw_text(draw, (margin, margin + ydelta), hour)
        xdelta = charwidth  # add some space before the minutes
        ydelta += lineheight
        for minute in minutes:
            draw_text(draw, (margin + xdelta, margin + ydelta), minute)
            xdelta += (3 * charwidth)
        ydelta += lineheight


def draw_time(draw):
    timestr = datetime.now().strftime("%H:%M")
    draw_text(draw, (imgwidth - (6 * charwidth) - margin, margin + 3), timestr)


def draw_date(draw):
    ydelta = lineheight + (margin * 3)
    timestr = datetime.now().strftime("%d.%m.%y")
    draw_text(draw, (imgwidth - (9 * charwidth) -
                     margin, ydelta), timestr)


def draw_forecast(draw, forecast):
    ydelta = lineheight + (margin * 10)
    current = forecast["currently"]
    startx = imgwidth / 2
    draw_text(draw, (startx, ydelta), str(
        round(current["temperature"])) + "°" + current["summary"])
    ydelta += (lineheight * 2)
    icon = current["icon"]
    im = Image.open("icons/" + iconlookup[icon])
    draw.bitmap((startx, ydelta), im)
    ydelta += lineheight
    draw_text(draw, (startx + 40, ydelta), "Feels like " +
              str(round(current["apparentTemperature"])) + "°")
    ydelta += (lineheight * 2)
    hourly = forecast["hourly"]
    summary = hourly["summary"]
    chars_per_line = (imgwidth / 2) / charwidth
    lines = wrap(summary, chars_per_line)
    for line in lines:
        draw_text(draw, (startx, ydelta), line)
        ydelta += lineheight
    daily = forecast["daily"]
    today = daily["data"][0]
    minTemp = today["temperatureMin"]
    maxTemp = today["temperatureMax"]
    draw_text(draw, (startx, ydelta), "Min " + str(round(minTemp)) + "° Max " + str(round(maxTemp)) + "°")


def draw_text(draw, pos, text):
    draw.text(pos, text, font=font)
