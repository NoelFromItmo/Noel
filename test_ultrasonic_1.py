#Primer raboty s ultrazvukovym datchikom rasstoyaniya UZ HC-SR04 Author: Gilmitdinov Noel
import RPi.GPIO as GPIO
import time

while True:
	#Vybor rezhima numeracii pinov
	GPIO.setmode(GPIO.BOARD)
	#Inicializaciya pinov
	GPIO.setup(10, GPIO.OUT) #trig
	GPIO.setup(8, GPIO.IN) #echo
	#Zapuskayushiy impuls
	GPIO.output(10, False)
	time.sleep(0.2)	
	GPIO.output(10, True)
	time.sleep(0.00001)
	GPIO.output(10, False)
	#Zasechenie nachala i konca vremeni
	while GPIO.input(8) == 0:
		beg_impulse = time.time()
	while GPIO.input(8) == 1:
		end_impulse = time.time()
	#Vichislenie vremeni prohojdeniya signala
	dur_impulse = end_impulse - beg_impulse
	#Vichislenie distancii
	distance = dur_impulse * 17150
	
	print "Distance: ", distance, " cm"

	time.sleep(1)
#Ochistka pinov
GPIO.cleanup();
