from machine import Pin, Timer
from time import sleep

headRedLED = Pin(2, Pin.OUT)
headGreenLED = Pin(3, Pin.OUT)
voiceLED = Pin(16, Pin.OUT)

def blinkLED(led, durationMS = 500):
    led.on()
    sleep(durationMS / 1000)
    led.off()

def showAlert():
    pass

def showError():
    for i in range(0, 3):
        blinkLED(headRedLED)
        sleep(500/1000)


