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
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit_password = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_password.setGeometry(QtCore.QRect(350, 10, 271, 40))
        font = QtGui.QFont()
        font.setFamily("DejaVu Math TeX Gyre")
        font.setPointSize(16)
        self.lineEdit_password.setFont(font)
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.pushButton_password = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_password.setGeometry(QtCore.QRect(630, 10, 111, 40))
        font = QtGui.QFont()
        font.setFamily("DejaVu Math TeX Gyre")
        font.setPointSize(16)
        self.pushButton_password.setFont(font)
        self.pushButton_password.setObjectName("pushButton_password")
        self.label_password = QtWidgets.QLabel(self.centralwidget)
        self.label_password.setGeometry(QtCore.QRect(10, 20, 331, 20))
        font = QtGui.QFont()
        font.setFamily("DejaVu Math TeX Gyre")
        font.setPointSize(18)
        self.label_password.setFont(font)
        self.label_password.setObjectName("label_password")
        self.pushButton_update = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_update.setGeometry(QtCore.QRect(40, 70, 87, 25))
        self.pushButton_update.setObjectName("pushbutton_update")
        self.pushButton_update.setVisible(0)
        self.label_temp = QtWidgets.QLabel(self.centralwidget)
        self.label_temp.setGeometry(QtCore.QRect(40, 110, 191, 17))
        self.label_temp.setObjectName("label_temp")
        self.label_temp.setVisible(0)
        self.label_hum = QtWidgets.QLabel(self.centralwidget)
        self.label_hum.setGeometry(QtCore.QRect(360, 110, 161, 17))
        self.label_hum.setObjectName("label_hum")
        self.label_hum.setVisible(0)
        self.lineEdit_tempvalue = QtWidgets.QTextEdit(self.centralwidget)
        self.lineEdit_tempvalue.setGeometry(QtCore.QRect(220, 110, 104, 31))
        self.lineEdit_tempvalue.setObjectName("lineEdit_tempvalue")
        self.lineEdit_tempvalue.setVisible(0)
        self.lineEdit_humvalue = QtWidgets.QTextEdit(self.centralwidget)
        self.lineEdit_humvalue.setGeometry(QtCore.QRect(520, 110, 104, 31))
        self.lineEdit_humvalue.setObjectName("lineEdit_humvalue")
        self.lineEdit_humvalue.setVisible(0)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
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
        self.label_temp.setText(_translate("MainWindow", "Current Temperature (F):  "))
        self.label_hum.setText(_translate("MainWindow", "Current Humidity (%):  "))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    
    sys.exit(app.exec_())
