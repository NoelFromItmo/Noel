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

#servo datapin
GPIO.setup(3, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)

#funkcia dlya raboty s 1 motorom
#power zadaet skorost vrasheniya i napravlenie
def MotorA(power1): #power ot -100 do 100 
	global p1
	if power1 < 0:  
		p1 = PiZyPwm(100, 16, GPIO.BOARD)
		p1.start(math.fabs(power1))
		time.sleep(0.1)
		p1.changeDutyCycle(math.fabs(power1))

	if power1 == 0:
		p1 = PiZyPwm(100, 16, GPIO.BOARD)
		p1.start(math.fabs(power1))
		time.sleep(0.1)
		p1.changeDutyCycle(math.fabs(power1))

	if power1 > 0:
		p1 = PiZyPwm(100, 18, GPIO.BOARD)
		p1.start(math.fabs(power1))
		time.sleep(0.1)
		p1.changeDutyCycle(math.fabs(power1))

	

#funkcia dlya raboty s 2 motorom
#power zadaet skorost vrasheniya i napravlenie
def MotorB(power2): #power ot -100 do 100 
	global p2
	if power2 < 0:
		p2 = PiZyPwm(100, 13, GPIO.BOARD)
		p2.start(math.fabs(power2))
		time.sleep(0.1)
		p2.changeDutyCycle(math.fabs(power2))

	if power2 == 0:
		p2 = PiZyPwm(100, 13, GPIO.BOARD)
		p2.start(math.fabs(power2))
		time.sleep(0.1)
		p2.changeDutyCycle(math.fabs(power2))

	if power2 > 0:
		p2 = PiZyPwm(100, 11, GPIO.BOARD)
		p2.start(math.fabs(power2))
		time.sleep(0.1)
		p2.changeDutyCycle(math.fabs(power2))

#funkcia dlya raboty s servomotorami
#deg zadaet znachenie povorota v gradusah; dataPin nomer pina s dannymi
def Servo(deg, dataPin):
	global p3
	p3 = PiZyPwm(50, dataPin, GPIO.BOARD)
	p3.start(2.5)
	duty = 0
	duty = (deg / 20) +2.5
	p3.changeDutyCycle(duty)
	time.sleep(1)	

#funkcia dlya ostanovki motorov
def endProcess(signalnum = None, handler = None):
	global p1, p2, p3	
	p1.stop()
	p2.stop()
	p3.stop()
	exit(0)
	
GPIO.output(15, True)
GPIO.output(22, True)

#signal.signal(signal.SIGTERM, endProcess)
#signal.signal(signal.SIGINT, endProcess)

Servo(0, 3) 
		
Servo(0, 5)
try:

	while True:	
		
		MotorA(10) #power ot -100 do 100
 
		MotorB(10) #power ot -100 do 100 

#Vihod po nazhatyu CTRL+C
except  KeyboardInterrupt: 
	GPIO.output(15, False)
	GPIO.output(22, False)
	endProcess()
	GPIO.cleanup()
