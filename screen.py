import platform

if platform.node() == 'raspberrypi':
    import epd2in13

    def showImageOnScreen(image):
        epd = epd2in13.EPD()
        epd.init(epd.lut_full_update)
        epd.clear_frame_memory(0xFF)
        epd.set_frame_memory(image, 0, 0)
        epd.display_frame()


else:
    def showImageOnScreen(image):
        image.save('img.png', 'PNG')
