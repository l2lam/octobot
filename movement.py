import servo
from time import sleep
#from machine import Pin, PWM

baseServo = servo.Servo9GR(15)
tiltServo = servo.Servo9GR(14)

def takeABow():
    tiltServo.progressToDegrees(90, 30, 90)
    tiltServo.returnToNeutralPosition()
    
def shakeHead():
    for i in range(3):
        baseServo.gotoDegrees(70)
        sleep(0.4)
        baseServo.gotoDegrees(110)
        sleep(0.4)
    baseServo.returnToNeutralPosition(200)

def nod():
    for i in range(3):
        tiltServo.progressToDegrees(110, 70, 20)
    tiltServo.returnToNeutralPosition()

def rollEyes():
    pass