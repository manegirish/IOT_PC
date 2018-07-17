import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)
GPIO.setup(14,GPIO.OUT)
print "LED on"
GPIO.output(18,GPIO.HIGH)
time.sleep(1)
GPIO.output(15,GPIO.HIGH)
time.sleep(2)
GPIO.output(14,GPIO.HIGH)
time.sleep(4)
print "LED off"
GPIO.output(14,GPIO.LOW)
time.sleep(2)
GPIO.output(15,GPIO.LOW)
time.sleep(1)
GPIO.output(18,GPIO.LOW)
