#!/usr/bin/python3

import sys
import RPi.GPIO as GPIO

#if I can get graph working
import matplotlib.pyplot as plt

# getting Adafruit_DHT library and renaming to dht for purposes of this program
import Adafruit_DHT as dht

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5.QtCore import QDate, QTime, QDateTime, Qt

#connecting ui that was mostly generated to this program in project1.py
# Used [3] as a general reference for pyqt
from project1_ui import Ui_MainWindow

#Pin Definitions:
data_pin = 4

class Project1Program(Ui_MainWindow):
    def __init__(self, window):
        Ui_MainWindow.__init__(self)
        self.setupUi(window)

        #Connect pushbuttons/labels/textedits with custom functions
        self.pushButton_password.clicked.connect(self.checkpassword)
        self.pushButton_update.clicked.connect(self.update_temp_n_hum)

    def checkpassword(self):
        txt = self.lineEdit_password.text()
        password = "kathy"
        if password == txt:
            #Set Visibility for password related information to 0 / Used [2] for reference
            self.pushButton_password.setVisible(0)
            self.lineEdit_password.setVisible(0)
            self.label_password.setVisible(0)
            
            #Set Visibility for non-password related information to 1
            self.pushButton_update.setVisible(1)
            self.label_temp.setVisible(1)
            self.label_hum.setVisible(1)
            self.lineEdit_tempvalue.setVisible(1)
            self.lineEdit_humvalue.setVisible(1)
    
    def update_temp_n_hum(self):   
        self.label_nocon.setStyleSheet('color: orange') 
        self.label_nocon.setText("Updating...") 
        self.label_nocon.setVisible(1)
        self.label_nocon.repaint()

        #Used Adafruit Example[5]
        h,t = dht.read_retry(dht.DHT22, data_pin)
        
        #if connected, get reading from sensor
        if h is not None and t is not None:
            self.label_nocon.setVisible(0)
            
            #convert to Fahrenheit
            t = t * 9/5.0 + 32
            
            #create string value of h and t
            temp = "%0.1f" % t
            hum  = "%0.1f" % h
            
            #put output onto screen in temp and hum value label/txt boxes
            self.lineEdit_tempvalue.setText(temp)
            self.lineEdit_humvalue.setText(hum)

            #get current datetime / Used [6] for reference
            datetime = QDateTime.currentDateTime()
            
            #output datetime
            self.label_updatetime.setText("Last Updated: " + datetime.toString(Qt.DefaultLocaleLongDate))
            self.label_updatetime.setVisible(1)
        else:
            #Show Sensor NOT Connected Warning
            self.label_nocon.setStyleSheet('color: red')
            self.label_nocon.setText("Sensor NOT connected")
            self.label_nocon.setVisible(1)
            

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()

    project1 = Project1Program(window)

    window.show()
    sys.exit(app.exec())


