#Primer raboty s servoprivodom Author: Gilmitdinov Noel
import time
import RPi.GPIO as GPIO
import wiringpi #podkluchenie biblioteki dlya SHIM
#Vybor rezhima numeracii pinov
GPIO.setmode(GPIO.BOARD)
#Inicializaciya pinov
GPIO.setup(11, GPIO.OUT)
#Zadaem kanal i chastotu 
p = GPIO.PWM(11, 50)
p.start(2.5)
try:
	duty = 0
#Zadaem absolutnuyu velichinu povorota v gradusah
	deg = 180
#Vichislenie skvaznosti
	duty = (deg / 20) +2.5
#Povorot
	p.ChangeDutyCycle(duty)
	time.sleep(1)		
#Zavershenie programmi po nazhatiyu CTRL+C
except KeyboardInterrupt:
	p.stop()
	GPIO.cleanup()
