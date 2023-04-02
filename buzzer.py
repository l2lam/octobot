from machine import ADC, Pin, PWM
import time

class Buzzer:
    """Controlling a buzzer"""
    def __init__(self, pin):
        self.pwm = PWM(Pin(pin))

# buzzerPWM = PWM(Pin(0))
# frequencyADC = ADC(Pin(28))
# toneADC = ADC(Pin(27))
# pauseADC = ADC(Pin(26))

# play = False

# debounce_time = 0
# buttonPin = Pin(1,Pin.IN,Pin.PULL_UP)
# def buttonPressed(pin):
#     global debounce_time, play
#     if (time.ticks_ms() - debounce_time) > 500:
#         debounce_time=time.ticks_ms()
#         play = not play
#         print(f'play: {play}')
        
# buttonPin.irq(trigger=Pin.IRQ_FALLING, handler=buttonPressed)


# while True:
#     if play:
#         freq = max(frequencyADC.read_u16(), 31)
#         tone = toneADC.read_u16()
#         pause = pauseADC.read_u16() // 256
#         print(f'freq({freq}), tone({tone}), pause({pause})')
#         buzzerPWM.freq(freq)
#         buzzerPWM.duty_u16(tone)
#         time.sleep(1)
#     else:
#         buzzerPWM.duty_u16(0)
#         time.sleep(1)
