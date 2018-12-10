#!/usr/bin/python3

#The MQTT Over Websockets was almost completely generated by following the Readme for https://github.com/aws/aws-iot-device-sdk-python
#I did need to update the version installed by pip to v1.4.2 due to an update from AWS with ats in the endpoint
#I used this command: sudo pip3 install -e git://github.com/aws/aws-iot-device-sdk-python.git@v1.4.2#egg=AWS_python_ver_ats_tag_fix

# Import SDK packages
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient


# Used https://www.cl.cam.ac.uk/projects/raspberrypi/tutorials/robot/buttons_and_switches
#imports Raspberry Pi GPIO library
import RPi.GPIO as GPIO

#use time library to delay led light switch handle debouncing the switch
import time
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QSizePolicy, QTableWidget,QTabWidget, QTextEdit, QHBoxLayout, QGridLayout, QDialog, QLabel,QComboBox, QStyleFactory, QRadioButton, QVBoxLayout
from PyQt5.QtCore import QDate, QTime, Qt, QDateTime, QTimer

# Used [3] as a general reference for pyqt
from project_ui_server import Ui_MainWindow

#needed for the database[9]
import redis
import json
#my created json dictionary
from shared_classes import *


#What board layout am I using
GPIO.setmode(GPIO.BCM)

GPIO.setwarnings(False)

#Using GPIO 19 as an INPUT   ##THIS IS THE REED SWITCH
GPIO.setup(19,GPIO.IN)

#Using GPIO 18 as an OUTPUT  ##THIS IS THE LED
GPIO.setup(18,GPIO.OUT)

#create a connection to the localhost Redis server instance, by default it runs on port 6379
redis_db = redis.StrictRedis(host="localhost", port=6379, db=0)

#####flush database  #don't flush database so I can collect some data
####redis_db.flushdb()

# Custom MQTT message callback
def customCallback(client, userdata, message):
    print("Received a new message: ")
    print(message.payload)
    print("from topic: ")
    print(message.topic)
    print("--------------\n\n")

#Server Topic
server_topic = "RPiServer1"

#Client Topic (requests to Server?)
client_topic = "RPiClient1"

#Drop oldest messages if over queue request offline limit
AWSIoTMQTTClient.DROP_OLDEST = 1
AWSIoTMQTTClient.DROP_NEWEST = 0

# For Websocket connection
myMQTTClient = AWSIoTMQTTClient("myClientID", useWebsocket=True)

# Configurations
# For Websocket
myMQTTClient.configureEndpoint("afmi9oh8t5vtj-ats.iot.us-east-1.amazonaws.com", 443)

# For Websocket, we only need to configure the root CA
myMQTTClient.configureCredentials("/home/pi/class/Server1/AmazonRootCA1_Server1.pem")

myMQTTClient.configureOfflinePublishQueueing(-1)  # Infinite offline Publish queueing
myMQTTClient.configureDrainingFrequency(2)  # Draining: 2 Hz
myMQTTClient.configureConnectDisconnectTimeout(10)  # 10 sec
myMQTTClient.configureMQTTOperationTimeout(5)  # 5 sec



# Loop forever
# Check for change in reedswitch, if change then publish a message with the updated redis information

#Interval Definitions
#Current requested interval time is 1 seconds (in ms)
time_interval = 1000


###################################################################################################################################################################
#Main Program
class ProjectSuperProgram(Ui_MainWindow):
    def __init__(self, window):
        Ui_MainWindow.__init__(self)
        self.setupUi(window)

        self.empty_dict = P_dict(current_status=0,
                  current_timestamp_str="",
                  day_num_open=0,
                  day_array_hour_num_open=[0,0,0,0,0,0,0,0,0,0,0,0,
                                           0,0,0,0,0,0,0,0,0,0,0,0],
                  day2_num_open=0,
                  day2_array_hour_num_open=[0,0,0,0,0,0,0,0,0,0,0,0,
                                            0,0,0,0,0,0,0,0,0,0,0,0],
                  day3_num_open=0,
                  day3_array_hour_num_open=[0,0,0,0,0,0,0,0,0,0,0,0,
                                            0,0,0,0,0,0,0,0,0,0,0,0],
                  day4_num_open=0,
                  day4_array_hour_num_open=[0,0,0,0,0,0,0,0,0,0,0,0,
                                            0,0,0,0,0,0,0,0,0,0,0,0],
                  day5_num_open=0,
                  day5_array_hour_num_open=[0,0,0,0,0,0,0,0,0,0,0,0,
                                            0,0,0,0,0,0,0,0,0,0,0,0],
                  day6_num_open=0,
                  day6_array_hour_num_open=[0,0,0,0,0,0,0,0,0,0,0,0,
                                            0,0,0,0,0,0,0,0,0,0,0,0],
                  day7_num_open=0,
                  day7_array_hour_num_open=[0,0,0,0,0,0,0,0,0,0,0,0,
                                            0,0,0,0,0,0,0,0,0,0,0,0])
                  
        self.seven_day_dict = self.empty_dict
        
        #reset
        reset_program = 1
        self.main_program(reset_program)
        
        reset_program = 0
        #Using [8] as an example for QTimer
        self.timer = QTimer()
        self.timer.timeout.connect(self.main_program)
        self.timer.start(time_interval)

        #Connect pushbuttons/labels/textedits with custom functions
        self.pushButton_password.clicked.connect(self.checkpassword)
        self.pushButton_gate.clicked.connect(self.gate_opener_led)
        #self.plot_graph()

    #############################################################################################
    #Main program that runs every second
    def main_program(self, reset = 0):
        if(reset):
            #setting up variables
            self.loopCount = 0
            self.new_day_countdown = 2
            self.last_connected_datetime = QDateTime.currentDateTime()
            self.time_between_messages_sec = 0    
            
            input = GPIO.input(19)
            self.prev_input = ~input
        else:
            #take a reading from RPi
            input = GPIO.input(19)

        send_message_new_day = 0

        if((self.new_day_countdown < 0) | reset):
            if(self.new_day_countdown < 0):
                #move data in dictionaries
                self.get_redis_current()
                self.move_day_data()
                
            current_datetime = QDateTime.currentDateTime()
            current_datetime_str = current_datetime.toString(Qt.DefaultLocaleLongDate)
            tomorrow_datetime = current_datetime.addDays(1)
            tomorrow_datetime_00 = QDateTime(QDate(tomorrow_datetime.date().year(), tomorrow_datetime.date().month(), tomorrow_datetime.date().day()), QTime(0,0))
            self.new_day_countdown = current_datetime.secsTo(tomorrow_datetime_00)
            print('seconds until new day: %d\n' % (self.new_day_countdown))
            
            #send a new message after moving all the data
            send_message_new_day = 1
            
        #For Debug
        ##print('send_message_new_day: %d\ninput: %d\nprev_input: %d\nreset: %d\n ' % (send_message_new_day, input, self.prev_input, reset))
        
        #if last reading was low and this one high, print and send message
        if((input != self.prev_input) | send_message_new_day):        
            #get current datetime / Used [6] for reference
            current_datetime = QDateTime.currentDateTime()
            current_datetime_str = current_datetime.toString(Qt.DefaultLocaleLongDate)
            tomorrow_datetime = current_datetime.addDays(1)
            tomorrow_datetime_00 = QDateTime(QDate(tomorrow_datetime.date().year(), tomorrow_datetime.date().month(), tomorrow_datetime.date().day()), QTime(0,0))
            self.new_day_countdown = current_datetime.secsTo(tomorrow_datetime_00)
            print('seconds until new day: %d\n' % (self.new_day_countdown))
            
            if(reset == 0):
                #no true previous time between messages when reset
                self.time_between_messages_sec = self.last_connected_datetime.secsTo(current_datetime)
                print('Seconds between messages: %d\n' % (self.time_between_messages_sec))

            if(input != self.prev_input):
                #update the dictionary (and database)
                self.get_redis_current() ## This updates the self.seven_day_dict
                #self.seven_day_dict.print_obj()

                #Is the gate open or closed?  If closed, no need to update num_open fields
                if(input == 0):
                    #Open        
                    print("Reed Switch open")        
                    self.seven_day_dict.day_num_open             = self.seven_day_dict.day_num_open + 1
                    current_hour = current_datetime.time().hour()
                    self.seven_day_dict.day_array_hour_num_open[current_hour] = self.seven_day_dict.day_array_hour_num_open[current_hour] + 1
                    self.seven_day_dict.current_status           = 1
                    self.label_currentupdatevalue_open.setVisible(1)
                    self.label_currentupdatevalue_closed.setVisible(0)
                    self.pushButton_gate.setText("CLOSE GATE")
                else:
                    print("Reed Switch closed")
                    self.seven_day_dict.current_status              = 0
                    self.label_currentupdatevalue_open.setVisible(0)
                    self.label_currentupdatevalue_closed.setVisible(1)
                    self.pushButton_gate.setText("OPEN GATE")
                    
                self.seven_day_dict.current_timestamp_str    = current_datetime_str
                
                self.label_currentupdatetime.setText("Last Change: " + current_datetime_str)
                self.dict_redis(self.seven_day_dict)
                #self.seven_day_dict.print_obj()
                
            
            if((self.time_between_messages_sec > 240) | reset):
                #try reconnecting as you may have been disconnected
                #connect and subscribe
                myMQTTClient.connect()
                ##myMQTTClient.subscribe(server_topic, 1, customCallback)
                ##myMQTTClient.subscribe(client_topic, 1, customCallback)


            #MESSAGE CREATION    
            message = {}
            message['current_status']           = self.seven_day_dict.current_status
            message['current_timestamp_str']    = self.seven_day_dict.current_timestamp_str
            message['day_num_open']             = self.seven_day_dict.day_num_open
            message['day_array_hour_num_open']  = self.seven_day_dict.day_array_hour_num_open
            message['day2_num_open']            = self.seven_day_dict.day2_num_open
            message['day2_array_hour_num_open'] = self.seven_day_dict.day2_array_hour_num_open
            message['day3_num_open']            = self.seven_day_dict.day3_num_open
            message['day3_array_hour_num_open'] = self.seven_day_dict.day3_array_hour_num_open
            message['day4_num_open']            = self.seven_day_dict.day4_num_open
            message['day4_array_hour_num_open'] = self.seven_day_dict.day4_array_hour_num_open
            message['day5_num_open']            = self.seven_day_dict.day5_num_open
            message['day5_array_hour_num_open'] = self.seven_day_dict.day5_array_hour_num_open
            message['day6_num_open']            = self.seven_day_dict.day6_num_open
            message['day6_array_hour_num_open'] = self.seven_day_dict.day6_array_hour_num_open
            message['day7_num_open']            = self.seven_day_dict.day7_num_open
            message['day7_array_hour_num_open'] = self.seven_day_dict.day7_array_hour_num_open
            message['datetime'] = [current_datetime.date().year(), current_datetime.date().month(), current_datetime.date().day(), current_datetime.time().hour(), current_datetime.time().minute(), current_datetime.time().second()]
            message['sequence'] = self.loopCount
            message['program_reset'] = reset
            messageJson = json.dumps(message)
            myMQTTClient.publish(server_topic, messageJson, 1)
            print('Published topic %s: %s\n' % (server_topic, messageJson))
            self.loopCount += 1

            self.last_connected_datetime = current_datetime
            reset = 0
            print('datetime array: %s' % (message['datetime']))
        
        self.prev_input = input
        time.sleep(1)
        self.new_day_countdown = self.new_day_countdown - 1

    ##########################################################################################
    #Write to database -- 'current' is rewritten every time
    #as all data I want to keep for the seven days is in this dictionary
    def dict_redis(self, currentdict):

        #change to a string via json
        p_string = currentdict.serialize()
        
        #send to redis
        redis_db.set('current', p_string)



    ##########################################################################################
    #Retrieve 'current' dictionary from database
    def get_redis_current(self):
        if(redis_db.exists('current') == False):
            print("FALSE")
            self.seven_day_dict = empty_dict
        else:
            print("TRUE")
            lval = redis_db.get('current')
            v1 = lval.decode()
            v = json.loads(v1)
            self.seven_day_dict = P_dict(**v)
            #self.seven_day_dict.print_obj()


    ##########################################################################################
    #Update data when midnight occurs (new day)
    def move_day_data(self):
        self.seven_day_dict.day7_array_hour_num_open = self.seven_day_dict.day6_array_hour_num_open
        self.seven_day_dict.day7_num_open            = self.seven_day_dict.day6_num_open
        self.seven_day_dict.day6_array_hour_num_open = self.seven_day_dict.day5_array_hour_num_open
        self.seven_day_dict.day6_num_open            = self.seven_day_dict.day5_num_open
        self.seven_day_dict.day5_array_hour_num_open = self.seven_day_dict.day4_array_hour_num_open
        self.seven_day_dict.day5_num_open            = self.seven_day_dict.day4_num_open
        self.seven_day_dict.day4_array_hour_num_open = self.seven_day_dict.day3_array_hour_num_open
        self.seven_day_dict.day4_num_open            = self.seven_day_dict.day3_num_open
        self.seven_day_dict.day3_array_hour_num_open = self.seven_day_dict.day2_array_hour_num_open
        self.seven_day_dict.day3_num_open            = self.seven_day_dict.day2_num_open
        self.seven_day_dict.day2_array_hour_num_open = self.seven_day_dict.day_array_hour_num_open
        self.seven_day_dict.day2_num_open            = self.seven_day_dict.day_num_open
        self.seven_day_dict.day_array_hour_num_open  = self.empty_dict.day_array_hour_num_open
        self.seven_day_dict.day_num_open             = self.empty_dict.day_num_open
        self.seven_day_dict.current_status           = 0
        self.seven_day_dict.current_timestamp_str    = current_datetime_str


    ##########################################################################################
    #This function is pretending to be connected to a gate opener where you hold the signal for a second and let go
    def gate_opener_led(self):    
        #Turning on LED
        print("LED on")
        GPIO.output(18,GPIO.HIGH)
        
        #wait 1 second
        time.sleep(1)

        #Turning off LED
        print("LED off")
        GPIO.output(18, GPIO.LOW)

        


    ##########################################################################################
    #Check Password 
    def checkpassword(self):
        txt = self.lineEdit_password.text()
        password = "kathy"
        if password == txt:
            #resize window to make room for all the data
            window.resize(900, 350)
            
            #Set Visibility for password related information to 0 / Used [2] for reference
            self.pushButton_password.setVisible(0)
            self.lineEdit_password.setVisible(0)
            self.label_password.setVisible(0)
            


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()

    project_super = ProjectSuperProgram(window)
    
    window.show()
    sys.exit(app.exec())
