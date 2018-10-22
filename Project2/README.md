# V1.0
# Author: Kathy Grimes
# Last Edited: October 22, 2018

####General Project Description
Remote Websocket/Web Page UI [1]
This project runs on two RPi3s - one is the sensor, 
the other is a client using a remote web-based display

The project uses Project1 as a base and expands from it.

#Required Hardware for Project to run:
(2) Raspberry Pi 3 (or 3+) running Raspbian Stretch
(1) DHT22 Temperature/Humidity Sensor
(2) Keyboard/Mouse/Monitor(Remote Desktop with connection to Raspberry Pi 3)

#Required Software installed on Raspbian Stretch:
Python 3.x
QT5
Pip
Matplotlib
Adafruit_DHT Library [4]
Git
Tornado [7]
Json
Redis/Redis Server
Chromium-Browser (or browser of your choice)

#Required Hardware install
The DHT22 data pin must be connected to the GPIO 4 pin on the Raspberry Pi 3
The DHT22 must have a 10kOhm resistor connected to pins 1 and 2


####Project Requirements
1. Server Raspberry Pi 3 B+
    - GUI is updated with Current, Average, Lowest, Highest Temp and Humidity Data as well as Timestamps
    - Data is kept in a database (mine uses Redis DB and JSON for formatting)
    - Websockets used between server and client
2. Client Raspberry Pi 3 B
    - HTML/JavaScript/JQuery Webpage with:
        - Indications for Connection errors (closing)
        - Eight buttons to request data and update webpage with:
              -Current, Average, Lowest, Highest Temp/Humidity with Timestamps


####Project Additions
#From Project1
1. Password Screen -- use password 'kathy'

#From Project2
1. Sensor Disconnected Indicator on Webpage
2. Resizing GUI on server PI desktop for additional data


####Project Run Instructions
git clone https://github.com/kagr7595/ecen5053
cd ecen5053/Project2

##PI Server Specific
cd server
ifconfig #Get your host ip -- you will need to enter it on the client side

#Terminal 1
python3 project2.py  #If any errors occur, please make sure to resolve the required software first
#In UI, please use 'kathy' as the password

#Terminal 2
python3 server.py

##PI Client Specific
cd client
#Use browser of your choice -- I used chromium-browser
chromium-browser client_socket.html &


####Citations

#From Project1
[1]  The required Project Title and Descriptions are found in the ECEN 5053-002 Project 2 Slides
[2]  https://forum.qt.io/topic/65799/how-to-display-label-for-30-seconds-and-then-hide-it/3
[3]  http://projects.skylogic.ca/blog/how-to-install-pyqt5-and-build-your-first-gui-in-python-3-4/
[4]  https://github.com/adafruit/Adafruit_Python_DHT 
[5]  https://github.com/adafruit/Adafruit_Python_DHT/blob/master/examples/AdafruitDHT.py
[6]  http://zetcode.com/gui/pyqt5/datetime/
#From Project2
[7]  https://os.mbed.com/cookbook/Websockets-Server
[8]  https://www.programcreek.com/python/example/99607/PyQt5.QtCore.QTimer
[9]  https://www.fullstackpython.com/blog/install-redis-use-python-3-ubuntu-1604.html
[10] https://redis.io/commands/hset
[11] https://stackoverflow.com/questions/1305532/convert-nested-python-dict-to-object
[12] https://stackoverflow.com/questions/43295958/python-serialize-object-to-json
[13] https://stackoverflow.com/questions/4488714/change-label-text-using-javascript
[14] https://github.com/mdn/samples-server/blob/master/s/websocket-chat/chatclient.js
[15] https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API/Writing_WebSocket_client_applications

