#!/usr/bin/python3

import sys
import RPi.GPIO as GPIO

#if I can get graph working
import matplotlib.pyplot as plt

# getting Adafruit_DHT library and renaming to dht for purposes of this program
import Adafruit_DHT as dht

import time

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5.QtCore import QDate, QTime, Qt, QDateTime, QTimer

#connecting ui that was mostly generated to this program in project2.py
# Used [3] as a general reference for pyqt
from project2_ui import Ui_MainWindow

#Pin Definitions:
data_pin = 4

#Interval Definitions
#Current requested interval time is 5 seconds
time_interval = 50

#initial unit setting is celsius
unit_c = 0

#initializing dictionary
value_dict = dict(reading_value_number=0,
                  current_temp_f=(0,0),
                  current_hum=(0,0),
                  lowest_temp_f=(300.0,0),
                  lowest_hum=(110.0,0),
                  highest_temp_f=(-300.0,0),
                  highest_hum=(-1.0,0),
                  average_temp_f=(0,0),
                  average_hum=(0,0))

class Project2Program(Ui_MainWindow):
    def __init__(self, window):
        Ui_MainWindow.__init__(self)
        self.setupUi(window)
        self.update_temp_n_hum()
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_temp_n_hum)
        self.timer.start(5000)

        #Connect pushbuttons/labels/textedits with custom functions
        self.pushButton_password.clicked.connect(self.checkpassword)
        self.pushButton_update.clicked.connect(self.change_unit_c_f)

    #Update GUI
    def update_gui(self):
        if unit_c == 0:
            #update gui screen with Fahrenheit units
            #values are already stored in Fahrenheit so directly update
            current_temp = "%0.1f" % value_dict['current_temp_f'][0]
            lowest_temp  = "%0.1f" %  value_dict['lowest_temp_f'][0]
            highest_temp = "%0.1f" % value_dict['highest_temp_f'][0]
            average_temp = "%0.1f" % value_dict['average_temp_f'][0]     
            self.label_currenttemp.setText("Current Temperature (*F)")   
            self.label_lowesttemp.setText("Lowest Temperature (*F)") 
            self.label_highesttemp.setText("Highest Temperature (*F)") 
            self.label_averagetemp.setText("Average Temperature (*F)")  
        else:
            current_temp = "%0.1f" % ((value_dict['current_temp_f'][0]-32)*5/9.0)
            lowest_temp  = "%0.1f" % (( value_dict['lowest_temp_f'][0]-32)*5/9.0)
            highest_temp = "%0.1f" % ((value_dict['highest_temp_f'][0]-32)*5/9.0)
            average_temp = "%0.1f" % ((value_dict['average_temp_f'][0]-32)*5/9.0)
            self.label_currenttemp.setText("Current Temperature (C)")   
            self.label_lowesttemp.setText("Lowest Temperature (C)")  
            self.label_highesttemp.setText("Highest Temperature (C)")  
            self.label_averagetemp.setText("Average Temperature (C)")  
            
        current_hum  = "%0.1f" %  value_dict['current_hum'][0]
        lowest_hum   = "%0.1f" %   value_dict['lowest_hum'][0]
        highest_hum  = "%0.1f" %  value_dict['highest_hum'][0]
        average_hum  = "%0.1f" %  value_dict['average_hum'][0]
        
        self.lineEdit_currenttempvalue.setText(current_temp)
        self.lineEdit_currenthumvalue.setText(current_hum)
        self.lineEdit_lowesttempvalue.setText(lowest_temp)
        self.lineEdit_lowesthumvalue.setText( lowest_hum)
        self.lineEdit_highesttempvalue.setText(highest_temp)
        self.lineEdit_highesthumvalue.setText( highest_hum)
        self.lineEdit_averagetempvalue.setText(average_temp)
        self.lineEdit_averagehumvalue.setText( average_hum)
                
    #Update Values
    def update_temp_n_hum(self):   
        #get current datetime / Used [6] for reference
        datetime = QDateTime.currentDateTime()

        #Used Adafruit Example[5]
        h,t = dht.read_retry(dht.DHT22, data_pin)
        
        #if connected, get reading from sensor
        if h is not None and t is not None:
            self.label_nocon.setVisible(0)
            

            #increment reading_value_number
            value_dict['reading_value_number'] = value_dict['reading_value_number'] + 1
            
            #convert to Fahrenheit
            t = t * 9/5.0 + 32

            value_dict['current_temp_f'] = (t,datetime)
            value_dict['current_hum'] = (h,datetime)             
            
            #checking for lowest temperature
            if value_dict['current_temp_f'][0] < value_dict['lowest_temp_f'][0] :
                value_dict['lowest_temp_f'] = value_dict['current_temp_f']

            #checking for highest temperature
            if value_dict['current_temp_f'][0] > value_dict['highest_temp_f'][0] :
                value_dict['highest_temp_f'] = value_dict['current_temp_f']
                
            #checking for lowest humidity
            if value_dict['current_hum'][0] < value_dict['lowest_hum'][0] :
                value_dict['lowest_hum'] = value_dict['current_hum']

            #checking for highest humidity
            if value_dict['current_hum'][0] > value_dict['highest_hum'][0] :
                value_dict['highest_hum'] = value_dict['current_hum']

            #computing average temperature with past temperature values
            value_dict['average_temp_f'] = ((value_dict['average_temp_f'][0]*(value_dict['reading_value_number']-1)+value_dict['current_temp_f'][0])/value_dict['reading_value_number'],datetime)

            #computing average humidity with past humidity values
            value_dict['average_hum'] = ((value_dict['average_hum'][0]*(value_dict['reading_value_number']-1)+value_dict['current_hum'][0])/value_dict['reading_value_number'],datetime)
		  
            
            #update GUI
            self.update_gui()

            #output datetime
            self.label_currentupdatetime.setText("Last Updated: " + datetime.toString(Qt.DefaultLocaleLongDate))
            self.label_templowestupdatetime.setText( "Obtained: " + value_dict['lowest_temp_f'][1].toString(Qt.DefaultLocaleLongDate))
            self.label_temphighestupdatetime.setText("Obtained: " + value_dict['highest_temp_f'][1].toString(Qt.DefaultLocaleLongDate))
            self.label_humlowestupdatetime.setText(  "Obtained: " + value_dict['lowest_hum'][1].toString(Qt.DefaultLocaleLongDate))
            self.label_humhighestupdatetime.setText( "Obtained: " + value_dict['highest_hum'][1].toString(Qt.DefaultLocaleLongDate))
        else:
            #Show Sensor NOT Connected Warning
            self.label_nocon.setStyleSheet('color: red')
            self.label_nocon.setText("Sensor NOT connected")
            self.label_nocon.setVisible(1)
            value_dict['current_temp_f'] = (-5000,datetime)
            value_dict['current_hum'] = (-5000,datetime)    


    #Check Password and then start collecting data
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
            
            #Set Visibility for non-password related information to 1
            self.pushButton_update.setVisible(1)
            self.label_currenttemp.setVisible(1)
            self.label_currenthum.setVisible(1)
            self.label_lowesttemp.setVisible(1)
            self.label_lowesthum.setVisible(1)
            self.label_highesttemp.setVisible(1)
            self.label_highesthum.setVisible(1)
            self.label_averagetemp.setVisible(1)
            self.label_averagehum.setVisible(1)
            self.lineEdit_currenttempvalue.setVisible(1)
            self.lineEdit_currenthumvalue.setVisible(1)
            self.lineEdit_lowesttempvalue.setVisible(1)
            self.lineEdit_lowesthumvalue.setVisible(1)
            self.lineEdit_highesttempvalue.setVisible(1)
            self.lineEdit_highesthumvalue.setVisible(1)
            self.lineEdit_averagetempvalue.setVisible(1)
            self.lineEdit_averagehumvalue.setVisible(1)
            self.label_currentupdatetime.setVisible(1)
            self.label_templowestupdatetime.setVisible(1)
            self.label_temphighestupdatetime.setVisible(1)
            self.label_humlowestupdatetime.setVisible(1)
            self.label_humhighestupdatetime.setVisible(1)


    #Change GUI Units
    def change_unit_c_f(self):
        global unit_c
        if unit_c == 0:
            #convert to Celsius
            unit_c = 1
        else:
            #convert to Fahrenheit
            unit_c = 0
        self.update_gui()

    
    
    

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()

    project2 = Project2Program(window)

    window.show()
    sys.exit(app.exec())


