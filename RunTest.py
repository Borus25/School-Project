# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RunTest.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Run_Test(object):
    def setupUi(self, Run_Test):
        Run_Test.setObjectName("Run_Test")
        Run_Test.resize(553, 498)
        self.label = QtWidgets.QLabel(Run_Test)
        self.label.setGeometry(QtCore.QRect(20, 20, 521, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Run_Test)
        self.pushButton.setGeometry(QtCore.QRect(414, 402, 111, 71))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Run_Test)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 400, 111, 71))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Run_Test)
        self.pushButton_3.setGeometry(QtCore.QRect(150, 400, 111, 71))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Run_Test)
        self.pushButton_4.setGeometry(QtCore.QRect(280, 400, 111, 71))
        self.pushButton_4.setObjectName("pushButton_4")
        self.textEdit = QtWidgets.QTextEdit(Run_Test)
        self.textEdit.setGeometry(QtCore.QRect(20, 70, 521, 101))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(Run_Test)
        self.textEdit_2.setGeometry(QtCore.QRect(20, 180, 521, 201))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.textEdit_2.setFont(font)
        self.textEdit_2.setObjectName("textEdit_2")

        self.retranslateUi(Run_Test)
        QtCore.QMetaObject.connectSlotsByName(Run_Test)

    def retranslateUi(self, Run_Test):
        _translate = QtCore.QCoreApplication.translate
        Run_Test.setWindowTitle(_translate("Run_Test", "Прохождение теста"))
        self.label.setText(_translate("Run_Test", "Для названия теста)"))
        self.pushButton.setText(_translate("Run_Test", "Дальше"))
        self.pushButton_2.setText(_translate("Run_Test", "Назад"))
        self.pushButton_3.setText(_translate("Run_Test", "Ответить"))
        self.pushButton_4.setText(_translate("Run_Test", "Закончить"))