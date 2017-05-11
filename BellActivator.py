#This file sends power from a raspberry pi to an output such as an LED
#Also used in conjunction with a PowerSwitch Tail II to convert to 110v

#Python 3

from gpiozero import LED
from time import sleep

#pinout from T on breadboard. No jumper
led = LED(12)

led.on()

sleep(3)

led.off()
