from PIL import Image, ImageDraw, ImageFont
import sys

def generateimage(nextdepartures):
    im = Image.new('1', (296,128), 255)
    draw = ImageDraw.Draw(im)
    for index, departure in enumerate(nextdepartures):
        xdelta = 35 * index
        if index == 1 and nextdepartures[0] < 10:
            xdelta -= 3
        draw.text((2 + xdelta, 2 ), str(departure) + "min ")
    #draw.text((2,2), 'hello')
    #draw.text((2,10), 'world')
    im.save('img.png', 'PNG')    
