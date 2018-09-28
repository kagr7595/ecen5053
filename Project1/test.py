#!/usr/bin/python3
###from contextlib import contextmanager
###import os
###
###@contextmanager
###def cd(newdir):
###    prevdir = os.getcwd()
###    os.chdir(os.path.expanduser(newdir))
###    try:
###        yield
###    finally:
###        os.chdir(prevdir)
###
        
###import subprocess
###
####in subprocess to get to correct folder
###with cd("~"):
# getting Adafruit_DHT library and renaming to dht for purposes of this program
import Adafruit_DHT as dht
    
#using Adafruit_DHT function to read the data coming from GPIO pin 4 of the raspberry pi
h,t = dht.read_retry(dht.DHT22, 4)

#Out of subprocess (no longer need to be in home directory)
#changing the temperature to Fahrenheit
t = t * 9/5.0 + 32
    
#printing Temp and Humidity output to terminal
print('Temp={0:0.1f}*F  Humidity={1:0.1f}%'.format(t, h))


