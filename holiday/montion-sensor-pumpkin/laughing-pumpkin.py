import RPi.GPIO as GPIO
import os
from time import sleep
import pygame 

ledPin1 = 12
ledPin2 = 16
sensorPin = 11
leds = [ledPin1, ledPin2]

pygame.mixer.init()
pygame.mixer.music.load('evil-laugh.mp3')

def setup():
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(ledPin1, GPIO.OUT)
	GPIO.setup(ledPin2, GPIO.OUT)
	GPIO.setup(sensorPin, GPIO.IN)
	
def playSound():
	if pygame.mixer.music.get_busy() != True:
		pygame.mixer.music.play()
		
def blinkLights():
	print('blink lights')
	for led in leds:
		GPIO.output(led, GPIO.HIGH)
		sleep(.05)
		GPIO.output(led, GPIO.LOW)

def lightsOut():
	print('- lights out -')
	for led in leds:
		GPIO.output(led, GPIO.LOW)
	
def main():
	print('in main')
	while True:
		if GPIO.input(sensorPin) == GPIO.HIGH:
			playSound()
			blinkLights()
		else:
			print '----busy??  ' + str(pygame.mixer.music.get_busy())
			if pygame.mixer.music.get_busy() != True:
				print 'turn lights off!!!'
				lightsOut()
			else:
				blinkLights()
					
def destroy(): 
	lightsOut()
	GPIO.cleanup()
	
if __name__ == '__main__':
	print('Program is starting')
	setup()
	try:
		main()
	except KeyboardInterrupt:
		destroy()
