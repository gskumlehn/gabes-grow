from apps.config.functions.Pinout import *
from apps.config.models import GrowConfig
from time import sleep

wateringRelayPort = 15
waterSensorPort = 24


def wateringOn():
    writesToPort(wateringRelayPort, 0)


def wateringOff():
    writesToPort(wateringRelayPort, 1)


def waterFor(seconds):
    initBoard()
    setAsOutput(wateringRelayPort)
    wateringOn()
    sleep(seconds)
    wateringOff()


def waterIfDryAndWateringOn():
    config = GrowConfig.objects.get(id=1)
    if config.watering and isDry():
        waterFor(10)


def isDry():
    initBoard()
    setAsInput(waterSensorPort)
    return readsPort(waterSensorPort)
