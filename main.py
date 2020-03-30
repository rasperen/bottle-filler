__author__ = "Raymond van Asperen"
__credits__ = ["Loek", "Diede", "hobbybrouwen.nl"]
__license__ = "Beerware"
__maintainer__ = "Raymond van Asperen"
__email__ = "rpva81+bottle+filler@gmail.com"

import ssd1306
from machine import I2C, Pin
import time

led = Pin(14, Pin.OUT)
led(0)
start = Pin(4, Pin.IN, Pin.PULL_UP)
up = Pin(12, Pin.IN, Pin.PULL_UP)
down = Pin(13, Pin.IN, Pin.PULL_UP)
step = .1
timeSet = 6.5
timeLeft = 0

i2c = I2C(-1, Pin(5), Pin(4))
display = ssd1306.SSD1306_I2C(64, 48, i2c)

def showMessage():
    display.fill(0)
    display.text(str(timeSet), 0, 0)
    display.text("sec", 0, 8)
    if timeLeft > 0:
        display.text("sec left", 0, 24)
        display.text(str(timeLeft), 0, 32)
    display.show()

def showStopMessage():
    display.fill(0)
    display.text("STOP", 0, 0)
    display.show()

showMessage()
while True:
    if not up.value():
        timeSet = round(timeSet + step, 1)
        showMessage()
        time.sleep_ms(300)
    if not down.value():
        timeSet = round(timeSet - step, 1)
        showMessage()
        time.sleep_ms(300)
    if not start.value():
        while not start.value():
            time.sleep_ms(300)
            pass
        end = time.ticks_ms() + (1000*timeSet)
        while(time.ticks_ms() < end): 
            led(1)
            timeLeft = (end - time.ticks_ms())/1000
            showMessage()
            if not start.value():
                led(0)
                while not start.value():
                    pass
                showStopMessage()
                time.sleep_ms(5000)
                break
        led(0)
        timeLeft = 0
        showMessage()
    pass
