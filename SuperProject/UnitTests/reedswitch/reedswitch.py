# Used https://www.cl.cam.ac.uk/projects/raspberrypi/tutorials/robot/buttons_and_switches

#imports Raspberry Pi GPIO library
import RPi.GPIO as GPIO

#use time library to delay led light switch handle debouncing the switch
import time

#What board layout am I using
GPIO.setmode(GPIO.BCM)

#Using GPIO 19 as an INPUT
GPIO.setup(19,GPIO.IN)

prev_input = 0
input = GPIO.input(19)

while True:
    #take a reading
    input = GPIO.input(19)

    #if last reading was low and this one high, print
    if(input != prev_input):
        if(input == 1):
            print("Reed Switch closed")
        else:
            print("Reed Switch open")
        prev_input = input

    time.sleep(1)
            

