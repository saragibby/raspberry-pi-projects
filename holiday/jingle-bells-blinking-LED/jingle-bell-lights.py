#!/usr/bin/python

import RPi.GPIO as GPIO
import time

redLightsPin = 15
greenLightsPin = 11
yellowLightsPin = 13
purpleLightsPin = 7

allPins = [redLightsPin, yellowLightsPin, greenLightsPin, purpleLightsPin]


def setup():
    GPIO.setmode(GPIO.BOARD)  # Numbers GPIOs by physical location
    for pin in allPins:
        GPIO.setup(pin, GPIO.OUT)  # Set all pins' mode is output
        GPIO.output(pin, GPIO.HIGH)  # Set all pins to high(+3.3V) to off led


def playJingleBells():
    for x in range(2):
        print 'Jingle bells'
        flashLights(redLightsPin)
        time.sleep(0.2)  # additional sleep for longer pause in song

        print 'Jingle bells'
        flashLights(greenLightsPin)
        time.sleep(0.2)  # additional sleep for longer pause in song

        print 'jingle all the way'
        turnOn(redLightsPin)
        time.sleep(0.2)
        turnOn(greenLightsPin)
        time.sleep(0.2)
        turnOn(yellowLightsPin)
        time.sleep(0.2)
        turnOn(greenLightsPin)
        time.sleep(0.2)
        turnOn(redLightsPin, 0.8)
        time.sleep(0.4)

        print 'oh what fun'
        flashLights(yellowLightsPin)
        time.sleep(0.2)  # additional sleep for longer pause in song

        print 'it is to ride in a one-horse open sleigh'
        turnOn(redLightsPin)
        time.sleep(0.2)
        turnOn(greenLightsPin)
        time.sleep(0.2)
        turnOn(yellowLightsPin)
        time.sleep(0.2)
        turnOn(greenLightsPin)
        time.sleep(0.2)
        turnOn(redLightsPin)
        time.sleep(0.2)
        turnOn(yellowLightsPin)
        time.sleep(0.2)
        turnOn(redLightsPin)
        time.sleep(0.2)
        turnOn(greenLightsPin)
        time.sleep(0.2)
        turnOn(yellowLightsPin)
        time.sleep(0.2)
        turnOn(greenLightsPin)
        time.sleep(0.4)

        if x == 0:  # only run first trip through loop
            print 'hey'
            turnOn(purpleLightsPin, 0.9)

    flashLights(purpleLightsPin, 5, 0.05, 0.1)


def turnOn(pinNumber, stayLitFor=0.3):
    GPIO.output(pinNumber, GPIO.LOW)
    time.sleep(stayLitFor)
    GPIO.output(pinNumber, GPIO.HIGH)


def flashLights(
    pinNumber,
    numberOfFlashes=3,
    amountToSleep=0.2,
    stayLitFor=0.3,
    ):
    for x in range(numberOfFlashes):
        turnOn(pinNumber, stayLitFor)
        time.sleep(amountToSleep)


def destroy():
    for pin in allPins:
        GPIO.output(pin, GPIO.HIGH)  # turn off all leds
        GPIO.cleanup()  # Release resource


if __name__ == '__main__':  # Program start from here
    setup()
    try:
        playJingleBells()
        GPIO.cleanup()
    except KeyboardInterrupt: # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
        destroy()