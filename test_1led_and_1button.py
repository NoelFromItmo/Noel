import RPi.GPIO as GPIO         
import time

GPIO.setmode(GPIO.BOARD)        



GPIO.setup(5, GPIO.IN)       

while True:                     

    sensor_data = GPIO.input(5);
    print "Crash Sensor: ", sensor_data
    time.sleep(0.1);
