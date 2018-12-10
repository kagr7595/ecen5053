
#for graphing
from matplotlib.backends.backend_qt5agg import (FigureCanvasQTAgg as FigureCanvas, NavigationToolbar2QT as NavigationToolbar)
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import random

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(780, 650)
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

        #####REMEMBER TO COMMENT THE BELOW 3 LINES OUT
        self.label_password.setVisible(0)
        self.pushButton_password.setVisible(0)
        self.lineEdit_password.setVisible(0)

        
        #Larger 62 font items (ie. Status Value)
        font = QtGui.QFont()
        font.setFamily("DejaVu Math TeX Gyre")
        font.setPointSize(62)
        font.setBold(True)
        self.label_currentupdatevalue_open = QtWidgets.QLabel(self.centralwidget)
        self.label_currentupdatevalue_open.setGeometry(QtCore.QRect(100, 5, 600, 350))
        self.label_currentupdatevalue_open.setFont(font)
        self.label_currentupdatevalue_open.setObjectName("label_currentupdatevalue_open")
        self.label_currentupdatevalue_open.setStyleSheet('color: green')
        #self.label_currentupdatevalue_open.setVisible(0)
        self.label_currentupdatevalue_closed = QtWidgets.QLabel(self.centralwidget)
        self.label_currentupdatevalue_closed.setGeometry(QtCore.QRect(50, 5, 700, 350))
        self.label_currentupdatevalue_closed.setFont(font)
        self.label_currentupdatevalue_closed.setObjectName("label_currentupdatevalue_closed")
        self.label_currentupdatevalue_closed.setStyleSheet('color: red')
        self.label_currentupdatevalue_closed.setVisible(0)
        
        font = QtGui.QFont()
        font.setFamily("DejaVu Math TeX Gyre")
        font.setPointSize(32)
        font.setBold(False)
        self.pushButton_gate = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_gate.setGeometry(QtCore.QRect(160, 330, 450, 200))
        self.pushButton_gate.setObjectName("pushbutton_gate")
        self.pushButton_gate.setFont(font)
        #self.pushButton_gate.setVisible(0)
        
        #Smaller 10 font items (Timestamps)
        font = QtGui.QFont()
        font.setFamily("DejaVu Math TeX Gyre")
        font.setPointSize(10)
        self.label_currentupdatetime = QtWidgets.QLabel(self.centralwidget)
        self.label_currentupdatetime.setGeometry(QtCore.QRect(190, 250, 550, 20))
        self.label_currentupdatetime.setFont(font)
        self.label_currentupdatetime.setObjectName("label_currentupdatetime")
        #self.label_currentupdatetime.setVisible(0)
        
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
        MainWindow.setWindowTitle(_translate("MainWindow", "Super Project - Server Application"))
        self.pushButton_password.setText(_translate("MainWindow", "Enter"))
        self.label_password.setText(_translate("MainWindow", "Please enter the password:"))
        self.label_currentupdatevalue_closed.setText(_translate("MainWindow", "GATE CLOSED"))
        self.label_currentupdatevalue_open.setText(_translate("MainWindow", "GATE OPEN"))
        self.label_currentupdatetime.setText(_translate("MainWindow", "XX/XX/XXXX XX:XX"))
        self.pushButton_gate.setText(_translate("MainWindow", "CLOSE GATE"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    
    sys.exit(app.exec_())
