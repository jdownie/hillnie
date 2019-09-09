#!/usr/bin/python

import RPi.GPIO as GPIO
from random import random
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW)

while True:
 GPIO.output(8, GPIO.HIGH)
 sleep(0.1)
 GPIO.output(8, GPIO.LOW)
 sleep(2 + random())
