#Primer raboty s datchikom temperatury DS18B20 Author: Gilmitdinov Noel
from w1thermsensor import W1ThermSensor #podkluchenie biblioteki dlya obrabotki dannyh temperatury
import time
import RPi.GPIO as GPIO

#Vybor rezhima numeracii pinov
GPIO.setmode(GPIO.BOARD)

GPIO.setup(7, GPIO.IN)
#Schityvanie dannyh
sensor = W1ThermSensor(W1ThermSensor.THERM_SENSOR_DS18B20, "0315650344ff")
temperature = sensor.get_temperature()
#Vivod dannyh
print temperature
