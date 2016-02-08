import RPi.GPIO as GPIO
import time

while True:
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(3,GPIO.OUT)
	GPIO.output(3, 0)
	time.sleep(1)
	GPIO.output(3, 1)
	time.sleep(1)
GPIO.cleanup()

