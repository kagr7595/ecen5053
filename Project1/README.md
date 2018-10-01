# V1.0
# Author: Kathy Grimes
# Last Edited: October 1, 2018

####General Project Description
Local QT-based UI [1]
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
Pip
Matplotlib
Adafruit_DHT Library [4]
Git

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
1. Password Screen -- use password 'kathy'


####Project Run Instructions
git clone https://github.com/kagr7595/ecen5053
cd ecen5053/Project1
python3 project1.py  #If any errors occur, please make sure to resolve the required software first
#In UI, please use 'kathy' as the password


####Citations
[1]  The required Project Title and Descriptions are found in the ECEN 5053-002 Project 1 - HWK 1 Slides
[2]  https://forum.qt.io/topic/65799/how-to-display-label-for-30-seconds-and-then-hide-it/3
[3]  http://projects.skylogic.ca/blog/how-to-install-pyqt5-and-build-your-first-gui-in-python-3-4/
[4]  https://github.com/adafruit/Adafruit_Python_DHT 
[5]  https://github.com/adafruit/Adafruit_Python_DHT/blob/master/examples/AdafruitDHT.py
[6]  http://zetcode.com/gui/pyqt5/datetime/
