#Jeremy Durdel
#Chapter 15 CPX 1
#7/20/2025

import time
from adafruit_circuitplayground import cp

class Region:
    def __init__(self, color, leds):
        self._color = color
        self._leds = leds

    def set_color(self, color):
        self._color = color

    def set_leds(self, leds):
        self._leds = leds

    def get_color(self):
        return self._color

    def get_leds(self):
        return self._leds

    def all_on(self):
        for i in self._leds:
            cp.pixels[i] = self._color

    def all_off(self):
        for i in self._leds:
            cp.pixels[i] = (0, 0, 0)

red = Region((255, 0, 0), (5, 6, 7))
blue = Region((0, 255, 0), (2, 3, 4))

while True:
    red.all_on()
    blue.all_off()
    time.sleep(1)

    red.all_off()
    blue.all_off()
    time.sleep(1)

    red.all_off()
    blue.all_on()
    time.sleep(1)

    red.all_off()
    blue.all_off()
    time.sleep(1)
