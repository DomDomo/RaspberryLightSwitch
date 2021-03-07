'''
Used for debugging relay by testing if signal is being sent from the GPIO pins
'''
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(18, GPIO.OUT)

print("1")
GPIO.output(18, GPIO.LOW)
print("2")
time.sleep(5)
print("3")
GPIO.output(18, GPIO.HIGH)
print("4")
time.sleep(5)
print("5")
GPIO.cleanup()
