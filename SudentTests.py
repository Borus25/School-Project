# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SudentTests.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_StudentTests(object):
    def setupUi(self, StudentTests):
        StudentTests.setObjectName("StudentTests")
        StudentTests.resize(808, 545)
        self.label = QtWidgets.QLabel(StudentTests)
        self.label.setGeometry(QtCore.QRect(660, 30, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(32)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.tableWidget = QtWidgets.QTableWidget(StudentTests)
        self.tableWidget.setGeometry(QtCore.QRect(20, 100, 641, 421))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.pushButton = QtWidgets.QPushButton(StudentTests)
        self.pushButton.setGeometry(QtCore.QRect(20, 20, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.comboBox = QtWidgets.QComboBox(StudentTests)
        self.comboBox.setGeometry(QtCore.QRect(160, 20, 191, 51))
        self.comboBox.setObjectName("comboBox")
        self.pushButton_2 = QtWidgets.QPushButton(StudentTests)
        self.pushButton_2.setGeometry(QtCore.QRect(360, 20, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(StudentTests)
        self.pushButton_3.setGeometry(QtCore.QRect(510, 20, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")

        self.retranslateUi(StudentTests)
        QtCore.QMetaObject.connectSlotsByName(StudentTests)

    def retranslateUi(self, StudentTests):
        _translate = QtCore.QCoreApplication.translate
        StudentTests.setWindowTitle(_translate("StudentTests", "Тесты"))
        self.label.setText(_translate("StudentTests", "Тесты"))
        self.pushButton.setText(_translate("StudentTests", "Начать"))
        self.pushButton_2.setText(_translate("StudentTests", "Показать"))
        self.pushButton_3.setText(_translate("StudentTests", "Назад"))
