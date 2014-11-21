import time
import wiringpi
# GPIO pin 12 = BCM pin 18 = wiringpi pin 1
led_pin  = 1
wiringpi.wiringPiSetup()
wiringpi.pinMode(led_pin, 2)
wiringpi.pwmWrite(led_pin, 0)
def led(led_value):
    wiringpi.pwmWrite(led_pin, led_value)
led(0)
while 1:
        for dc in range(0, 1023, 5):
                led(dc)
                time.sleep(0.01)
        for dc in range(1024, 0, -5):
                led(dc)
                time.sleep(0.01)
