# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'project1.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(450, 200)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        font = QtGui.QFont()
        font.setFamily("DejaVu Math TeX Gyre")
        font.setPointSize(14)
        self.lineEdit_password = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_password.setGeometry(QtCore.QRect(50, 55, 150, 30))
        self.lineEdit_password.setFont(font)
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.pushButton_password = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_password.setGeometry(QtCore.QRect(205, 50, 111, 40))
        self.pushButton_password.setFont(font)
        self.pushButton_password.setObjectName("pushButton_password")
        self.label_password = QtWidgets.QLabel(self.centralwidget)
        self.label_password.setGeometry(QtCore.QRect(10, 20, 331, 20))
        self.label_password.setFont(font)
        self.label_password.setObjectName("label_password")

        
        font = QtGui.QFont()
        font.setFamily("DejaVu Math TeX Gyre")
        font.setPointSize(12)
        self.pushButton_update = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_update.setGeometry(QtCore.QRect(10, 20, 87, 25))
        self.pushButton_update.setObjectName("pushbutton_update")
        self.pushButton_update.setFont(font)
        self.pushButton_update.setVisible(0)
        self.label_temp = QtWidgets.QLabel(self.centralwidget)
        self.label_temp.setGeometry(QtCore.QRect(30, 50, 250, 17))
        self.label_temp.setObjectName("label_temp")
        self.label_temp.setFont(font)
        self.label_temp.setVisible(0)
        self.label_hum = QtWidgets.QLabel(self.centralwidget)
        self.label_hum.setGeometry(QtCore.QRect(30, 100, 250, 17))
        self.label_hum.setObjectName("label_hum")
        self.label_hum.setFont(font)
        self.label_hum.setVisible(0)
        self.lineEdit_tempvalue = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_tempvalue.setGeometry(QtCore.QRect(300, 50, 104, 31))
        self.lineEdit_tempvalue.setObjectName("lineEdit_tempvalue")
        self.lineEdit_tempvalue.setFont(font)
        self.lineEdit_tempvalue.setVisible(0)
        self.lineEdit_humvalue = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_humvalue.setGeometry(QtCore.QRect(300, 100, 104, 31))
        self.lineEdit_humvalue.setObjectName("lineEdit_humvalue")
        self.lineEdit_humvalue.setFont(font)
        self.lineEdit_humvalue.setVisible(0)

        font = QtGui.QFont()
        font.setFamily("DejaVu Math TeX Gyre")
        font.setPointSize(12)
        self.label_nocon = QtWidgets.QLabel(self.centralwidget)
        self.label_nocon.setGeometry(QtCore.QRect(10, 100, 300, 100))
        self.label_nocon.setFont(font)
        self.label_nocon.setObjectName("label_nocon")
        self.label_nocon.setVisible(0)
        
        font = QtGui.QFont()
        font.setFamily("DejaVu Math TeX Gyre")
        font.setPointSize(8)
        self.label_updatetime = QtWidgets.QLabel(self.centralwidget)
        self.label_updatetime.setGeometry(QtCore.QRect(10, 160, 400, 20))
        self.label_updatetime.setFont(font)
        self.label_updatetime.setObjectName("label_updatetime")
        self.label_updatetime.setVisible(0)
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 450, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Project 1"))
        self.pushButton_password.setText(_translate("MainWindow", "Enter"))
        self.label_password.setText(_translate("MainWindow", "Please enter the password:"))
        self.pushButton_update.setText(_translate("MainWindow", "Update"))
        self.label_temp.setText(_translate("MainWindow", "Current Temperature (*F):  "))
        self.label_hum.setText(_translate("MainWindow", "Current Humidity (%):  "))
        self.label_nocon.setText(_translate("MainWindow", "Sensor NOT connected"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    
    sys.exit(app.exec_())
