# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\barankrky\CodingWorkspace\string-encode-decode\main.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(560, 280)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 10, 251, 251))
        self.groupBox.setObjectName("groupBox")
        self.encodeTxt = QtWidgets.QLineEdit(self.groupBox)
        self.encodeTxt.setGeometry(QtCore.QRect(60, 30, 171, 21))
        self.encodeTxt.setObjectName("encodeTxt")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 30, 41, 21))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.encryptButton = QtWidgets.QPushButton(self.groupBox)
        self.encryptButton.setGeometry(QtCore.QRect(60, 60, 171, 31))
        self.encryptButton.setObjectName("encryptButton")
        self.encryptOutput = QtWidgets.QTextEdit(self.groupBox)
        self.encryptOutput.setGeometry(QtCore.QRect(10, 130, 231, 111))
        self.encryptOutput.setReadOnly(True)
        self.encryptOutput.setObjectName("encryptOutput")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(10, 110, 51, 21))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(290, 10, 251, 251))
        self.groupBox_2.setObjectName("groupBox_2")
        self.decryptOutput = QtWidgets.QTextEdit(self.groupBox_2)
        self.decryptOutput.setGeometry(QtCore.QRect(10, 130, 231, 111))
        self.decryptOutput.setReadOnly(True)
        self.decryptOutput.setObjectName("decryptOutput")
        self.decryptButton = QtWidgets.QPushButton(self.groupBox_2)
        self.decryptButton.setGeometry(QtCore.QRect(60, 60, 171, 31))
        self.decryptButton.setObjectName("decryptButton")
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(10, 30, 41, 21))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(10, 110, 51, 21))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.decodeTxt = QtWidgets.QLineEdit(self.groupBox_2)
        self.decodeTxt.setGeometry(QtCore.QRect(60, 30, 171, 21))
        self.decodeTxt.setObjectName("decodeTxt")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "Encode"))
        self.label.setText(_translate("MainWindow", "Text :"))
        self.encryptButton.setText(_translate("MainWindow", "Encrypt"))
        self.label_3.setText(_translate("MainWindow", "Output :"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Decode"))
        self.decryptButton.setText(_translate("MainWindow", "Decrypt"))
        self.label_2.setText(_translate("MainWindow", "Text :"))
        self.label_4.setText(_translate("MainWindow", "Output :"))