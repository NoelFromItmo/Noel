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


def PulseIn(pin, val):
	beg_impulse = 0
	end_impulse = 0
	while GPIO.input(pin) == val:
		beg_impulse = time.time()
	while GPIO.input(pin) != val :
		end_impulse = time.time()
	dur_impulse = end_impulse - beg_impulse
	return dur_impulse
		

def ReadRed():
	GPIO.output(8, False)
	GPIO.output(10, False)
	RedColor = PulseIn(12, False)
	return RedColor

def ReadGreen():
	GPIO.output(8, True)
	GPIO.output(10, True)
	GreenColor = PulseIn(12, True)
	return GreenColor

def ReadBlue():
	GPIO.output(8, False)
	GPIO.output(10, True)
	BlueColor = PulseIn(12, False)
	return BlueColor

def ReadWhite():
	GPIO.output(8, True)
	GPIO.output(10, False)
	WhiteColor = PulseIn(12, False)
	return WhiteColor


while True:  
	w = ReadWhite()
	r = ReadRed()
	g = ReadGreen()
	b = ReadBlue()

	print("white:", w)
	print("red:  ", r)
	print("green:", g)
	print("blue: ", b)
	


		



	
	
