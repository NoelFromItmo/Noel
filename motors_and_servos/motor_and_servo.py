#Primer raboty s motorshield MC33932 Author: Gilmitdinov Noel

#import bibliotek
import RPi.GPIO as GPIO 
import time 
import signal
import math
from pizypwm import *

#ustanovka rezhimov pinov
GPIO.setmode(GPIO.BOARD)
#silovie
GPIO.setup(16, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)

GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)

GPIO.setup(15, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)

GPIO.output(15, True)
GPIO.output(22, True)

#servo datapin
GPIO.setup(3, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)

#funkcia dlya zapuska 1 motora
def MotorAInit(power1): 
	global p1
	if power1 < 0:  
		p1 = PiZyPwm(100, 16, GPIO.BOARD)
		p1.start(math.fabs(power1))

	if power1 >= 0:
		p1 = PiZyPwm(100, 18, GPIO.BOARD)
		p1.start(math.fabs(power1))


def PlusMinus(a):
	if a>0: 
		return 1
	else:
		return 0

		
		
	

#funkcia dlya vrasheniya 1 motora
#power zadaet skorost vrasheniya i napravlenie
def MotorAGo(power1): #power ot -100 do 100 
	global p1
	p1.changeDutyCycle(math.fabs(power1))


	

#funkcia dlya zapuska 2 motora
def MotorBInit(power2): #power ot -100 do 100 
	global p2
	if power2 < 0:
		p2 = PiZyPwm(100, 13, GPIO.BOARD)
		p2.start(math.fabs(power2))


	if power2 >= 0:
		p2 = PiZyPwm(100, 11, GPIO.BOARD)
		p2.start(math.fabs(power2))

#funkcia dlya vrasheniya 2 motora
#power zadaet skorost vrasheniya i napravlenie
def MotorBGo(power2): #power ot -100 do 100 
	global p2
	p2.changeDutyCycle(math.fabs(power2))


#funkcii dlya raboty s servomotorami
#deg zadaet znachenie povorota v gradusah;
def ServoAInit():
	global p3	
	p3 = GPIO.PWM (3, 50)
	p3.start(2.5)
	
def ServoBInit():
	global p4	
	p4 = GPIO.PWM (5,50)
	p4.start(2.5)
		

def ServoAGo(deg):
	global p3	
	duty = (deg / 20) +2.5
	p3.ChangeDutyCycle(duty)

def ServoBGo(deg):
	global p4	
	duty = (deg / 20) +2.5
	p4.ChangeDutyCycle(duty)
	

#funkcia dlya ostanovki motorov
def endProcess(signalnum = None, handler = None):
	global p1, p2, p3, p4
	p1.stop()
	p2.stop()
	p3.stop()
	p4.stop()
	exit(0)
	



try:


	value = 0
	MotorAInit(value) #power ot -100 do 100
	MotorBInit(value)
	ServoAInit()
	ServoBInit()
	ServoAGo(0)
	ServoBGo(0)

	while value<100:
		
		#print value		

		MotorAGo(value) 
	
		MotorBGo(value) 

		ServoAGo(value*1.8)

		ServoBGo(value*1.8)

		value += 1
		time.sleep(0.1)
		print value

	old_value = PlusMinus(value)

	while value>-100:		

		if PlusMinus(value) != old_value:
			p1.stop()
			p2.stop()
			MotorAInit(value)
			MotorBInit(value)
			

		print value
		

		MotorAGo(value)
 
		MotorBGo(value) 	

		ServoAGo(math.fabs(value*1.8)) 

		ServoBGo(math.fabs(value*1.8))	


		value -= 1 
		time.sleep(0.1)

	while value<=0:

		#print value
		
		MotorAGo(value) 
 
		MotorBGo(value) 

		ServoAGo(math.fabs(value*1.8)) 

		ServoBGo(math.fabs(value*1.8))
		
		value += 1
		time.sleep(0.1) 

	GPIO.output(3, False)
	GPIO.output(5, False)
	GPIO.output(15, False)
	GPIO.output(22, False)
#Vihod po nazhatyu CTRL+C
except  KeyboardInterrupt: 
	GPIO.output(3, False)
	GPIO.output(5, False)
	GPIO.output(15, False)
	GPIO.output(22, False)
	endProcess()
	GPIO.cleanup()
