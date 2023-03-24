from machine import Pin, Timer
import time

class Button:
    """ Button controls """
    def __init__(self, pin: int, clickHandler):
        self._debounceTime = 0
        self.clickHandler = clickHandler
        buttonPin = Pin(pin, Pin.IN, Pin.PULL_UP)        
        buttonPin.irq(trigger=Pin.IRQ_FALLING, handler=self._buttonPressed)
        
    def _buttonPressed(self, pin):
        if (time.ticks_ms() - self._debounceTime) > 500:
            self._debounceTime=time.ticks_ms()
            self.clickHandler()
            
        
