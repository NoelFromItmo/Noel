#import bibliotek
import RPi.GPIO as GPIO 
import time 
import signal
import math
from pizypwm import *

#ustanovka rezhimov pinov
GPIO.setmode(GPIO.BOARD)
GPIO.setup(8, GPIO.OUT) #S2
GPIO.setup(10, GPIO.OUT) #S3
GPIO.setup(12, GPIO.IN) #OUT
GPIO.setup(16, GPIO.OUT) #S0
GPIO.setup(18, GPIO.OUT) #S1

#Zamer chastoty; vse lomaetsa iz-za timera, navernoe
def PulseIn(pin, val):
	beg_impulse = 0
	end_impulse = 0
	#timer = 0
	while (GPIO.input(pin) == val): #and (timer<500):
		beg_impulse = time.time()
		#timer = timer + 1 
		#if timer>=500:
			#return -1
	#timer = 0
	while (GPIO.input(pin) != val): #and (timer<500) :
		end_impulse = time.time()
	#	timer = timer + 1
		#if timer>=500:
		#	return -1
	dur_impulse = end_impulse - beg_impulse
	return dur_impulse
		
#chtenie krasnogo
def ReadRed():
	GPIO.output(8, False)
	GPIO.output(10, False)
	RedColor = PulseIn(12, False)
	return RedColor
#chtenie zelenogo
def ReadGreen():
	GPIO.output(8, True)
	GPIO.output(10, True)
	GreenColor = PulseIn(12, True)
	return GreenColor
#chtenie ksinego
def ReadBlue():
	GPIO.output(8, False)
	GPIO.output(10, True)
	BlueColor = PulseIn(12, False)
	return BlueColor
#chtenie belogo
def ReadWhite():
	GPIO.output(8, True)
	GPIO.output(10, False)
	WhiteColor = PulseIn(12, False)
	return WhiteColor


while True: 
 #delenie i umnozhenie dlya privoda d udobovarimiy variant
	w = ReadWhite()/1455971442*255 
	r = ReadRed()/1455971442*255
	g = ReadGreen()/1455971442*255
	b = ReadBlue()/1455971442*255
	time.sleep(0.5)
	print("white:", w)
	print("red:  ", r)
	print("green:", g)
	print("blue: ", b)

	


		



	
	
