from django.conf import settings

if not settings.DEBUG:
    import RPi.GPIO as GPIO
else:
    from .mock import MockGPIO as GPIO 

def initBoard():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

def setAsInput(pinNumber):
    GPIO.setup(pinNumber, GPIO.IN)

def setAsOutput(pinNumber):
    GPIO.setup(pinNumber, GPIO.OUT)

def readsPort(pinNumber):
    return GPIO.input(pinNumber)

def writesToPort(pinNumber, portState):
    GPIO.output(pinNumber, portState)