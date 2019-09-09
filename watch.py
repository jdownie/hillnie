#!/usr/bin/python3

import RPi.GPIO as GPIO
from time import sleep
import sys

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(32, GPIO.IN)

while True:
  v = GPIO.input(32)
  print(v, end = "")
  sys.stdout.flush()
  sleep(0.01)

