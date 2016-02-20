#Primer raboty s datchikom linii (tolko cifrovim) Author: Gilmitdinov Noel
import RPi.GPIO as GPIO         
import time

#Vybor rezhima numeracii pinov
GPIO.setmode(GPIO.BOARD)        

#Inicializaciya pinov
GPIO.setup(5, GPIO.IN)       

while True:                     
	#Zapis i vivod vhodnogo signala
    sensor_data = GPIO.input(5)
    print "Line Sensor: ", sensor_data
    time.sleep(0.1)
