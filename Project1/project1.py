#!/usr/bin/python3

import sys

#if I can get graph working
import matplotlib.pyplot as plt

# getting Adafruit_DHT library and renaming to dht for purposes of this program
import Adafruit_DHT as dht

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow

#connecting ui that was mostly generated to this program in project1.py
from project1_ui import Ui_MainWindow

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
            #Set Visibility for password related information to 0
            self.pushButton_password.setVisible(0)
            self.lineEdit_password.setVisible(0)
            self.label_password.setVisible(0)
            
            #Set Visibility for non-password related information to 1
            self.pushButton_update.setVisible(1)
            self.label_temp.setVisible(1)
            self.label_hum.setVisible(1)
            self.textEdit_tempvalue.setVisible(1)
            self.textEdit_humvalue.setVisible(1)
    
    def update_temp_n_hum(self):
        #Check if sensor is connected ????
        
        #if connected, get reading from sensor
        h,t = dht.read_retry(dht.DHT22, 4)
        
        #convert to Fahrenheit
        t = t * 9/5.0 + 32
        
        #put output onto screen in temp and hum value label/txt boxes
        self.lineEdit_tempvalue.text(t)
        self.lineEdit_humvalue.text(h)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()

    project1 = Project1Program(window)

    window.show()
    sys.exit(app.exec())


###if __name__ == '__main__':
###    app = QApplication(sys.argv)
###    window = QWidget()
###    window.resize(250, 150)
###    window.move(300, 300)
###    window.setWindowTitle('Simple')
###    window.show()
###    
###    sys.exit(app.exec_())
###

### getting Adafruit_DHT library and renaming to dht for purposes of this program
##import Adafruit_DHT as dht
##    
###using Adafruit_DHT function to read the data coming from GPIO pin 4 of the raspberry pi
##h,t = dht.read_retry(dht.DHT22, 4)
##
###Out of subprocess (no longer need to be in home directory)
###changing the temperature to Fahrenheit
##t = t * 9/5.0 + 32
##    
###printing Temp and Humidity output to terminal
##print('Temp={0:0.1f}*F  Humidity={1:0.1f}%'.format(t, h))


###SAVE FOR WHEN NEEDING TO REGENERATE THE GUI

###if __name__ == "__main__":
###    import sys
###    app = QtWidgets.QApplication(sys.argv)
###    MainWindow = QtWidgets.QMainWindow()
###    ui = Ui_MainWindow()
###    ui.setupUi(MainWindow)
###    MainWindow.show()
###    
###    sys.exit(app.exec_())
