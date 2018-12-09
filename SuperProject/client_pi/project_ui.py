
#for graphing
from matplotlib.backends.backend_qt5agg import (FigureCanvasQTAgg as FigureCanvas, NavigationToolbar2QT as NavigationToolbar)
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import random

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(880, 750)
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

        
        self.graph = PlotCanvas(self.centralwidget, width=3, height=2)
        self.graph.setGeometry(QtCore.QRect(55, 200, 770, 450))
        self.graph.setObjectName("graph")
        #self.graph.setVisible(0)
        
        
        #Larger 14 font items (update pushbuttons)
        font = QtGui.QFont()
        font.setFamily("DejaVu Math TeX Gyre")
        font.setPointSize(14)
        self.pushButton_update = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_update.setGeometry(QtCore.QRect(55, 25, 200, 30))
        self.pushButton_update.setObjectName("pushbutton_update")
        self.pushButton_update.setFont(font)
        ##self.pushButton_update.setDisabled(True)
        #self.pushButton_update.setVisible(0)
        
        #12 font items (graph pushbuttons)
        font = QtGui.QFont()
        font.setFamily("DejaVu Math TeX Gyre")
        font.setPointSize(12)
        self.pushButton_today = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_today.setGeometry(QtCore.QRect(100, 660, 170, 25))
        self.pushButton_today.setObjectName("pushbutton_today")
        self.pushButton_today.setFont(font)
        #self.pushButton_today.setVisible(0)
        self.pushButton_multday = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_multday.setGeometry(QtCore.QRect(350, 660, 170, 25))
        self.pushButton_multday.setObjectName("pushbutton_multday")
        self.pushButton_multday.setFont(font)
        #self.pushButton_multday.setVisible(0)
        self.pushButton_week = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_week.setGeometry(QtCore.QRect(600, 660, 170, 25))
        self.pushButton_week.setObjectName("pushbutton_week")
        self.pushButton_week.setFont(font)
        #self.pushButton_week.setVisible(0)
        
        #Larger 22 font items (ie. Status Value)
        font = QtGui.QFont()
        font.setFamily("DejaVu Math TeX Gyre")
        font.setPointSize(22)
        font.setBold(True)
        self.label_currentupdatevalue = QtWidgets.QLabel(self.centralwidget)
        self.label_currentupdatevalue.setGeometry(QtCore.QRect(210, 100, 200, 50))
        self.label_currentupdatevalue.setFont(font)
        self.label_currentupdatevalue.setObjectName("label_currentupdatevalue")
        #self.label_currentupdatevalue.setVisible(0)
        font.setBold(False)
        self.pushButton_gate = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_gate.setGeometry(QtCore.QRect(600, 25, 200, 150))
        self.pushButton_gate.setObjectName("pushbutton_gate")
        self.pushButton_gate.setFont(font)
        #self.pushButton_gate.setVisible(0)
        
        #Larger 18 font items (ie. Status)
        font = QtGui.QFont()
        font.setFamily("DejaVu Math TeX Gyre")
        font.setPointSize(18)
        self.label_status = QtWidgets.QLabel(self.centralwidget)
        self.label_status.setGeometry(QtCore.QRect(80, 100, 120, 45))
        self.label_status.setFont(font)
        self.label_status.setObjectName("label_status")
        #self.label_status.setVisible(0)

        #Smaller 8 font items (Timestamps)
        font = QtGui.QFont()
        font.setFamily("DejaVu Math TeX Gyre")
        font.setPointSize(8)
        self.label_currentupdatetime = QtWidgets.QLabel(self.centralwidget)
        self.label_currentupdatetime.setGeometry(QtCore.QRect(215, 140, 550, 20))
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
        MainWindow.setWindowTitle(_translate("MainWindow", "Super Project - Client Application"))
        self.pushButton_password.setText(_translate("MainWindow", "Enter"))
        self.label_password.setText(_translate("MainWindow", "Please enter the password:"))
        self.pushButton_update.setText(_translate("MainWindow", "UPDATE"))
        self.label_currentupdatetime.setText(_translate("MainWindow", "Timestamp: DateTimeXX-XX-XX XX:XX"))
        self.label_currentupdatevalue.setText(_translate("MainWindow", "No Status"))
        self.pushButton_gate.setText(_translate("MainWindow", "CLOSE\nGATE"))
        self.label_status.setText(_translate("MainWindow", "STATUS:"))
        self.pushButton_today.setText(_translate("MainWindow", "Today"))
        self.pushButton_multday.setText(_translate("MainWindow", "Past 2 Days"))
        self.pushButton_week.setText(_translate("MainWindow", "Past Week"))


class PlotCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)

        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)        
        
        self.plot()

    def plot(self):
        data = [random.random() for i in range(25)]
        ax = self.figure.add_subplot(111)
        ax.plot(data, 'r-')
        ax.set_title('PyQt Matplotlib Example')
        self.draw()
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    
    sys.exit(app.exec_())
