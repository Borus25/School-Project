# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AdminTests.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AdminTests(object):
    def setupUi(self, AdminTests):
        AdminTests.setObjectName("AdminTests")
        AdminTests.resize(849, 449)
        self.label = QtWidgets.QLabel(AdminTests)
        self.label.setGeometry(QtCore.QRect(30, 10, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(33)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(AdminTests)
        self.pushButton.setGeometry(QtCore.QRect(30, 82, 141, 51))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(AdminTests)
        self.pushButton_2.setGeometry(QtCore.QRect(30, 360, 151, 51))
        self.pushButton_2.setObjectName("pushButton_2")
        self.tableWidget = QtWidgets.QTableWidget(AdminTests)
        self.tableWidget.setGeometry(QtCore.QRect(210, 70, 611, 341))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.label_2 = QtWidgets.QLabel(AdminTests)
        self.label_2.setGeometry(QtCore.QRect(220, 12, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.comboBox = QtWidgets.QComboBox(AdminTests)
        self.comboBox.setGeometry(QtCore.QRect(290, 11, 101, 31))
        self.comboBox.setObjectName("comboBox")
        self.pushButton_3 = QtWidgets.QPushButton(AdminTests)
        self.pushButton_3.setGeometry(QtCore.QRect(420, 10, 141, 51))
        self.pushButton_3.setObjectName("pushButton_3")

        self.retranslateUi(AdminTests)
        QtCore.QMetaObject.connectSlotsByName(AdminTests)

    def retranslateUi(self, AdminTests):
        _translate = QtCore.QCoreApplication.translate
        AdminTests.setWindowTitle(_translate("AdminTests", "Для админа: Тесты"))
        self.label.setText(_translate("AdminTests", "Тесты"))
        self.pushButton.setText(_translate("AdminTests", "Добавить"))
        self.pushButton_2.setText(_translate("AdminTests", "Назад"))
        self.label_2.setText(_translate("AdminTests", "Класс:"))
        self.pushButton_3.setText(_translate("AdminTests", "Показать"))
