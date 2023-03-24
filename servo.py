from time import sleep
from machine import Pin, PWM

class Servo:
    """ A simple class for controlling a 9g servo with the Raspberry Pi Pico.
        Original code from: https://how2electronics.com/how-to-control-servo-motor-with-raspberry-pi-pico/
     """
 
    def __init__(self, pin: int or Pin or PWM, maxRotationDegrees = 180, zeroDegreesCycle=2500, maxDegreesCycle=7500):
        if isinstance(pin, int):
            pin = Pin(pin, Pin.OUT)
        if isinstance(pin, Pin):
            self.__pwm = PWM(pin)
        if isinstance(pin, PWM):
            self.__pwm = pin
        self.__pwm.freq(50)
        self.zeroDegreesCycle = zeroDegreesCycle
        self.maxDegreesCycle = maxDegreesCycle
        self.period = maxDegreesCycle - zeroDegreesCycle
        self.maxRotationDegrees = maxRotationDegrees
 
    def stop(self):
        """ Stop signal to the servo.
 
        """
        self.__pwm.deinit()
 
    def gotoDegrees(self, degrees: int):
        """ Moves the servo to the specified position in degrees.
        """

        cycle = int(self.zeroDegreesCycle + self.period * degrees / self.maxRotationDegrees)
        self.__pwm.duty_u16(cycle)
 
    def gotoMiddle(self):
        """ Moves the servo to the middle.
        """
        self.gotoDegrees(int(self.maxRotationDegrees / 2))
 
    def free(self):
        """ Allows the servo to be moved freely.
        """
        self.__pwm.duty_u16(0)
        
        
class Servo9GR(Servo):
    def __init__(self, pin):
        super().__init__(pin, 180, 1000, 9000)
