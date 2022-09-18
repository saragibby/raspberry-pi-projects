#import RPi.GPIO as GPIO
#import time

#GPIO.setmode(GPIO.BCM)
#PIR_PIN = 8
#GPIO.setup(PIR_PIN, GPIO.IN)

#def MOTION(PIR_PIN):
	#print "Motion Detected!"

#print "PIR Module Test (CTRL+C to exit)"
#time.sleep(2)
#print "Ready"

#try:
	#GPIO.add_event_detect(PIR_PIN, GPIO.RISING, callback=MOTION)
	#while 1:
		#time.sleep(100)
#except KeyboardInterrupt:
	#print "Quit"
	#GPIO.cleanup()

from gpiozero import MotionSensor, LED
from time import sleep, time

sensor = MotionSensor(11)
green = LED(12)
red = LED(22)

def on_motion():
	print "Motion detected!"
	green.off()
	red.on()

def no_motion():
	green.on()
	red.off()
	
print "Setting up"
green.on
red.on

print "do not move setting up the PIR sensor"
sensor.wait_for_no_motion()

print "device ready!"
red.off()

sensor.when_motion = on_motion
sensor.when_no_motion = no_motion

input("Press enter of crtl+c to exit")
