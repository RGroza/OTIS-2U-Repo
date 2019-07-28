import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(5,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
counter=0
pin=0
cond=False
lastValue = GPIO.input(5)
while True:
  if GPIO.input(5) is not lastValue:
    lastValue = GPIO.input(5)
    counter+=1
    time.sleep(0.30)
  print(counter)
  
