# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Result.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Result(object):
    def setupUi(self, Result):
        Result.setObjectName("Result")
        Result.resize(521, 338)
        self.label = QtWidgets.QLabel(Result)
        self.label.setGeometry(QtCore.QRect(36, 32, 331, 71))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Result)
        self.label_2.setGeometry(QtCore.QRect(40, 140, 261, 91))
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(Result)
        self.pushButton.setGeometry(QtCore.QRect(154, 262, 181, 41))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Result)
        QtCore.QMetaObject.connectSlotsByName(Result)

    def retranslateUi(self, Result):
        _translate = QtCore.QCoreApplication.translate
        Result.setWindowTitle(_translate("Result", "Form"))
        self.label.setText(_translate("Result", "Для логина"))
        self.label_2.setText(_translate("Result", "Для баллов"))
        self.pushButton.setText(_translate("Result", "Перейти в главное меню "))
