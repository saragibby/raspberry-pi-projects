# Motion Sensor House

from gpiozero import MotionSensor, LED
from time import sleep, time
import pygame


sensor = MotionSensor(14)
green = LED(15)
red = LED(18)

def on_motion():
    print("Motion detected!")
    pygame.mixer.init()
    pygame.mixer.music.load("hohoho.wav")
    pygame.mixer.music.play()
    green.off()
    red.on()

def no_motion():
    green.on()
    red.off()
    
print("Setting up")
green.on
red.on

print("do not move setting up the PIR sensor")
sensor.wait_for_no_motion()

print("device ready!")
red.off()

sensor.when_motion = on_motion
sensor.when_no_motion = no_motion

input("Press enter of crtl+c to exit\n\n")

