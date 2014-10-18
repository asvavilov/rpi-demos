import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(7, GPIO.OUT)

c = 5
try:
    while c >= 0:
	c -= 1
	GPIO.output(7, 1)
	time.sleep(0.0015)
	GPIO.output(7, 0)
	time.sleep(2)
except KeyboardInterrupt:
    GPIO.cleanup()
GPIO.cleanup()
