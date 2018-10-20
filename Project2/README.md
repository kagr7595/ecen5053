# V1.0
# Author: Kathy Grimes
# Last Edited: October 19, 2018

####General Project Description
Local QT-based UI [1]
This project demonstrates development of a rapid prototype of a 
stand-alone temperature monitoring device with a local user interface

This project creates a standard class setup for the RPi3 with other 
hardware and system elements

#Required Hardware for Project to run:
(2) Raspberry Pi 3 (or 3+) running Raspbian Stretch
(1) DHT22 Temperature/Humidity Sensor
(1) Keyboard/Mouse/Monitor(Remote Desktop with connection to Raspberry Pi 3)

#Required Software installed on Raspbian Stretch:
Python 3.x
QT5
Pip
Matplotlib
Adafruit_DHT Library [4]
Git
Tornado [7]

#Required Hardware install
The DHT22 data pin must be connected to the GPIO 4 pin on the Raspberry Pi 3
The DHT22 must have a 10kOhm resistor connected to pins 1 and 2


####Project Requirements
1.
2.
    - 


####Project Additions
#From Project1
1. Password Screen -- use password 'kathy'

#From Project2


####Project Run Instructions
git clone https://github.com/kagr7595/ecen5053
cd ecen5053/Project1
python3 project2.py  #If any errors occur, please make sure to resolve the required software first
#In UI, please use 'kathy' as the password


####Citations

#From Project1
[1]  The required Project Title and Descriptions are found in the ECEN 5053-002 Project 1 - HWK 1 Slides
[2]  https://forum.qt.io/topic/65799/how-to-display-label-for-30-seconds-and-then-hide-it/3
[3]  http://projects.skylogic.ca/blog/how-to-install-pyqt5-and-build-your-first-gui-in-python-3-4/
[4]  https://github.com/adafruit/Adafruit_Python_DHT 
[5]  https://github.com/adafruit/Adafruit_Python_DHT/blob/master/examples/AdafruitDHT.py
[6]  http://zetcode.com/gui/pyqt5/datetime/
#From Project2
[7]  https://os.mbed.com/cookbook/Websockets-Server
[8]  https://www.programcreek.com/python/example/99607/PyQt5.QtCore.QTimer

