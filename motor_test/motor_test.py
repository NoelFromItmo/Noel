#Primer raboty s motorshield L298 Author: Gilmitdinov Noel

#import bibliotek
import RPi.GPIO as GPIO 
import time 
import signal
import math
from pizypwm import *

#ustanovka rezhimov pinov
GPIO.setmode(GPIO.BOARD)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)


#funkcia dlya raboty s 1 motorom
#power zadaet skorost vrasheniya i napravlenie
def MotorA(power1): #power ot -100 do 100 
	global p1
	if power1 < 0:  
		p1 = PiZyPwm(100, 16, GPIO.BOARD)
		p1.start(math.fabs(power1))
		p1.changeDutyCycle(math.fabs(power1))

	if power1 == 0:
		p1 = PiZyPwm(100, 16, GPIO.BOARD)
		p1.start(math.fabs(power1))
		p1.changeDutyCycle(math.fabs(power1))

	if power1 > 0:
		p1 = PiZyPwm(100, 18, GPIO.BOARD)
		p1.start(math.fabs(power1))
		p1.changeDutyCycle(math.fabs(power1))

	

#funkcia dlya raboty s 2 motorom
#power zadaet skorost vrasheniya i napravlenie
def MotorB(power2): #power ot -100 do 100 
	global p2
	if power2 < 0:
		p2 = PiZyPwm(100, 13, GPIO.BOARD)
		p2.start(math.fabs(power2))
		p2.changeDutyCycle(math.fabs(power2))

	if power2 == 0:
		p2 = PiZyPwm(100, 13, GPIO.BOARD)
		p2.start(math.fabs(power2))
		p2.changeDutyCycle(math.fabs(power2))

	if power2 > 0:
		p2 = PiZyPwm(100, 11, GPIO.BOARD)
		p2.start(math.fabs(power2))
		p2.changeDutyCycle(math.fabs(power2))


#funkcia dlya ostanovki motorov
def endProcess(signalnum = None, handler = None):
	global p1, p2	
	p1.stop()
	p2.stop()
	exit(0)
	


signal.signal(signal.SIGTERM, endProcess)
signal.signal(signal.SIGINT, endProcess)

try:
	while True:
		MotorA(10) #power ot -100 do 100 
		MotorB(-20) #power ot -100 do 100 
		time.sleep(0.1)
#Vihod po nazhatyu CTRL+C
except  (KeyboardInterrupt, SystemExit): 
	endProcess()
	GPIO.cleanup()
	
