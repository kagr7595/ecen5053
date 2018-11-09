# Used https://thepihut.com/blogs/raspberry-pi-tutorials/27968772-turning-on-an-led-with-your-raspberry-pis-gpio-pins

#imports Raspberry Pi GPIO library
import RPi.GPIO as GPIO

#use time library to delay led light switch
import time

#What board layout am I using
GPIO.setmode(GPIO.BCM)

GPIO.setwarnings(False)

#Using GPIO 18 as an OUTPUT
GPIO.setup(18,GPIO.OUT)

#Turning on LED
print("LED on")
GPIO.output(18,GPIO.HIGH)

#wait 1 second
time.sleep(1)

#Turning off LED
print("LED off")
GPIO.output(18, GPIO.LOW)
