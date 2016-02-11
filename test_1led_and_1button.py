#Primer raboty s knopkoy Author: Gilmitdinov Noel
import RPi.GPIO as GPIO         
import time
#Vybor rezhima numeracii pinov
GPIO.setmode(GPIO.BOARD)        
#Inicializaciya pinov
GPIO.setup(5, GPIO.IN)       

while True:                     
#Schityvanie i vivod dannyh s knopki
    sensor_data = GPIO.input(5);
    print "Crash Sensor: ", sensor_data
    time.sleep(0.1);
