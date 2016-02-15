#Primer raboty s datchikom vlazhnosti i temperatury DHT-11 Author: Gilmitdinov Noel
import Adafruit_DHT#Biblioteka dlya raboty s datchikom DHT-11
import time
import RPi.GPIO as GPIO
#Vybor rezhima numeracii pinov
GPIO.setmode(GPIO.BOARD)

GPIO.setup(7, GPIO.IN)

temperature = 0
humidity = 0

#Ustanovka sensora
sensor = Adafruit_DHT.DHT11
#Poluchenie dannyh
humidity, temperature = Adafruit_DHT.read_retry(sensor, 7)

#Vivod dannyh
print "Humidity ", humidity, "%"
print "Temperature ", temperature, "C"




