# V1.0
# Author: Kathy Grimes

####General Project Description
Gate Reminder SuperProject
See the Super_Project_Report.pdf in the Google Drive folder

#Required Hardware for Project to run:
(2) Raspberry Pi 3 (or 3+) running Raspbian Stretch
(1) Reed Sensor
(1) LED
(2) Keyboard/Mouse/Monitor(Remote Desktop with connection to Raspberry Pi 3)

#Required Software installed on Raspbian Stretch:
Python 3.x
QT5
Pip
Matplotlib
Git
Json
MQTT 
Websockets  *** Please see note in server.py code at the top for how to get the correct tag installed
Boto3
Redis/Redis Server
Chromium-Browser (or browser of your choice)
AWS connections and acount

#Required Hardware install
Reed Sensor needs to be in a pull-up circuit and connected to pin 19
LED needs a resistor and a connection to pin 18


####Project Requirements
1. Server Raspberry Pi 3 B+
    - GUI is updated with Current gate status as well as Timestamp
    - Data is kept in a database (mine uses Redis DB and JSON for formatting)
    - MQTT Websockets used between server and AWS
2. Client Raspberry Pi 3 B or anything with an internet connection
    - HTML/JavaScript Webpage with:
	- Graph (JS Charts)
	- SQS (SNS was setup to be used but not integrated with the GUI - some information on console.log)
	- QTGUI was set up for the python code but I couldn't get the fifo multi-message to work correctly
	   - GUI has multiple grid formats and canvas layouts (This is where I spent too much time as I couldn't figure out how to do the graph portion correctly)
3. Unfortunately AMQP/AWS MQ I didn't have time to work on -- just as I mentioned in the report design update.  I did have SNS working for the mid-report (please see videos I linked in slack) 
SNS was in the html code, but I couldn't get it set up for the gate control button in time
4. Cloudwatch is working in AWS and sends a text to my phone when an alert message is sent through MQTT and hits the Lambda function

####Project Additions


####Project Run Instructions
git clone https://github.com/kagr7595/ecen5053
cd ecen5053/SuperProject

##PI Server Specific
cd server_pi
You will need to set up your own iot core thing with AWS lambda code/sqs to get this working properly

#Terminal 1
python3 server.py  #If any errors occur, please make sure to resolve the required software first

##PI Client Specific
cd website_need_internet
#Use browser of your choice -- I used chromium-browser
chromium-browser client_webpage_aws.html &
Click on Update after there are some messages sent from server side.

#Please take a look at the GUI I made for the client side pi even if I was unable to attach the client code in time.  
#ALL QT5 UI were completely done without the QT5 creator.
cd client_pi
python3 project_ui.py

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

#From SuperProject
Not Labeled due to there being so many links
https://docs.aws.amazon.com/iot/latest/developerguide/config-and-test-rules.html
https://docs.aws.amazon.com/iot/latest/developerguide/iot-sdks.html
https://github.com/aws/aws-iot-device-sdk-js/issues/97
https://aws.amazon.com/lambda/
https://docs.aws.amazon.com/lambda/latest/dg/lambda-dg.pdf
https://docs.aws.amazon.com/iot/latest/developerguide/iot-lambda-rule.html
https://docs.aws.amazon.com/IAM/latest/APIReference/API_CreatePolicy.html
https://medium.com/tensoriot/aws-iot-creating-your-first-cloud-bound-device-d8dca0695f43
https://docs.aws.amazon.com/lambda/latest/dg/lambda-api-permissions-ref.html
https://docs.aws.amazon.com/lambda/latest/dg/with-sqs-create-package.html#with-sqs-example-deployment-pkg-nodejs
https://docs.aws.amazon.com/sns/latest/dg/sns-http-https-endpoint-as-subscriber.html
https://docs.aws.amazon.com/sns/latest/dg/sns-message-and-json-formats.html#http-header

https://www.raspberrypi.org/documentation/remote-access/ssh/scp.md

https://iotbytes.wordpress.com/aws-iot-cli-on-raspberry-pi/

https://matplotlib.org/api/_as_gen/matplotlib.pyplot.xlim.html
https://www.geeksforgeeks.org/graph-plotting-in-python-set-1/
https://matplotlib.org/gallery/user_interfaces/embedding_in_qt_sgskip.html

https://stackoverflow.com/questions/36768033/pyqt-how-to-open-new-window
http://doc.qt.io/qt-5/qtwidgets-mainwindows-mainwindow-example.html
http://doc.qt.io/qt-5/qgridlayout.html


https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/getting-started-browser.html

https://www.w3schools.com/howto/howto_js_toggle_hide_show.asp

More sources can be found in the code especially if they had a very significant effect on the code.
