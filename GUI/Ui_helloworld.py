# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\BHJ\NSCC\PROG1700-w0411909\GUI\helloworld.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(510, 337)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButtonHello = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonHello.setGeometry(QtCore.QRect(120, 140, 191, 81))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.pushButtonHello.setFont(font)
        self.pushButtonHello.setObjectName("pushButtonHello")
        self.labelMessage = QtWidgets.QLabel(self.centralwidget)
        self.labelMessage.setGeometry(QtCore.QRect(10, 70, 91, 21))
        self.labelMessage.setObjectName("labelMessage")
        self.lineEditMessage = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditMessage.setGeometry(QtCore.QRect(110, 60, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEditMessage.setFont(font)
        self.lineEditMessage.setObjectName("lineEditMessage")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 510, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButtonHello.setText(_translate("MainWindow", "Say Hello"))
        self.labelMessage.setText(_translate("MainWindow", "Message:"))

