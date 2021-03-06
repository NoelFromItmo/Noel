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

GPIO.output(16, True)
GPIO.output(18, False)


def PulseIn(val):
	beg_impulse = 0
	end_impulse = 0
	while GPIO.input(12) == val:
		beg_impulse = time.time()
	while GPIO.input(12) != val :
		end_impulse = time.time()
	dur_impulse = end_impulse - beg_impulse
	return dur_impulse
		
def ReadRed():
	GPIO.output(8, False)
	GPIO.output(10, False)
	RedColor = PulseIn(False)
	return RedColor

def ReadGreen():
	GPIO.output(8, True)
	GPIO.output(10, True)
	GreenColor = PulseIn(False)
	return GreenColor

def ReadBlue():
	GPIO.output(8, False)
	GPIO.output(10, True)
	BlueColor = PulseIn(False)
	return BlueColor

def ReadWhite():
	GPIO.output(8, True)
	GPIO.output(10, False)
	WhiteColor = PulseIn(False)
	return WhiteColor


w0 = ReadWhite()/1455971442*255
r0 = ReadRed() /1455971442*255
g0 = ReadGreen()/1455971442*255
b0 = ReadBlue() /1455971442*255
while True:  
	w = (ReadWhite()/1455971442*255 - w0) * 10000000000
	r = (ReadRed()/1455971442*255 - r0)  * 1000000000000
	g = (ReadGreen()/1455971442*255 - g0) * 1000000000000
	b = (ReadBlue()/1455971442*255 - b0) * 1000000000000

	if (w>=100) or (w<=-100):
		w = 10
	if (r>=100) or (r<=-100):
		r = 10
	if (g>=100) or (g<=-100):
		g = 10
	if (b>=100) or (b<=-100):
		b = 10


	print("white:", w)
	print("red:  ", r)
	print("green:", g)
	print("blue: ", b)
	time.sleep(0.1)
	
	if (b > -35 ) and (b < -28 ) and (g > -39) and (g < -33):
		print "red"
	if (g >-54 ) and (g <-40 ) and (b > -33 ) and (b < -26 ):
		print "green"
	if (g > -50 ) and (g < -40 ) and (b > -50 ) and (b < -40 ):
		print "blue"
