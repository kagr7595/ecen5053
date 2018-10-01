# V1.0
# Author: Kathy Grimes
# Last Edited: October 1, 2018

####General Project Description
[1] Local QT-based UI 
This project demonstrates development of a rapid prototype of a 
stand-alone temperature monitoring device with a local user interface

This project creates a standard class setup for the RPi3 with other 
hardware and system elements

#Required Hardware for Project to run:
Raspberry Pi 3 (or 3+) running Raspbian Stretch
DHT22 Temperature/Humidity Sensor
Keyboard/Mouse/Monitor(Remote Desktop with connection to Raspberry Pi 3)

#Required Software installed on Raspbian Stretch:
Python 3.x
QT5
Adafruit_DHT Library
Git (Optional - you can also directly copy the code project files from the link provided)

#Required Hardware install
The DHT22 data pin must be connected to the GPIO 4 pin on the Raspberry Pi 3
The DHT22 must have a 10kOhm resistor connected to pins 1 and 2

####Project Requirements
1. Use QT5 to develop a QT UI for a Python Application
2. UI should allow for:
   - request of current humidity/temperature values from the DHT22
   - should display the values as well as the time of the request
   - should handle not receiving data when requested (ie. if sensor is disconnected)

####Project Additions
1. Login Screen -- use password 'kathy'


####Install Instructions



####Citations
[1]  The required Project Title and Descriptions are found in the ECEN 5053-002 Project 1 - HWK 1 Slides
[2]  
[3]  
[4]  
