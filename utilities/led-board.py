from gpiozero import LEDBoard
from time import sleep 
from signal import pause

leds = LEDBoard(21,20,26,16,19,13,12,6,5,1,0,7,8,11,25,9,10,24,23,22,27,18,17,15,14,4,3,2)

leds.on()
sleep(1)
leds.off()
sleep(1)

sleepTime = 0.075
lightArray=[1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

while True:
	leds.value = tuple(lightArray)
	lastVal = lightArray.pop()
	lightArray.insert(0,lastVal)
	sleep(sleepTime)

pause()
