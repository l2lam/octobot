from machine import Pin, Timer

headRedLED = Pin(2, Pin.OUT)
headGreenLED = Pin(3, Pin.OUT)

def blinkLED(led, durationMS = 500):
    led.on()
    time.sleep(durationMS / 1000)
    led.off()

def showAlert():
    pass

def showError():
    for i in range(0, 3):
        blinkLED(headRedLED)


