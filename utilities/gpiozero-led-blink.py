from gpiozero import LED
from signal import pause

red = LED(18)
green = LED(15)

green.on()
red.on()

pause()
