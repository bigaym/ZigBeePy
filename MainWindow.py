# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ZigBee2PC.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        self.title = QtWidgets.QLabel(Dialog)
        self.title.setGeometry(QtCore.QRect(370, 30, 181, 51))
        font = QtGui.QFont()
        font.setFamily("Adobe 宋体 Std L")
        font.setPointSize(14)
        self.title.setFont(font)
        self.title.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.title.setObjectName("title")
        self.select_folder = QtWidgets.QPushButton(Dialog)
        self.select_folder.setGeometry(QtCore.QRect(600, 110, 261, 41))
        font = QtGui.QFont()
        font.setFamily("Adobe 宋体 Std L")
        font.setPointSize(14)
        self.select_folder.setFont(font)
        self.select_folder.setObjectName("select_folder")
        self.serial_print = QtWidgets.QTextBrowser(Dialog)
        self.serial_print.setGeometry(QtCore.QRect(90, 220, 331, 201))
        self.serial_print.setObjectName("serial_print")
        self.title_2 = QtWidgets.QLabel(Dialog)
        self.title_2.setGeometry(QtCore.QRect(670, 180, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Adobe 宋体 Std L")
        font.setPointSize(14)
        self.title_2.setFont(font)
        self.title_2.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.title_2.setObjectName("title_2")
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(660, 230, 111, 41))
        self.comboBox.setObjectName("comboBox")
        self.port_open = QtWidgets.QPushButton(Dialog)
        self.port_open.setGeometry(QtCore.QRect(590, 310, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Adobe 宋体 Std L")
        font.setPointSize(14)
        self.port_open.setFont(font)
        self.port_open.setObjectName("port_open")
        self.port_close = QtWidgets.QPushButton(Dialog)
        self.port_close.setGeometry(QtCore.QRect(760, 310, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Adobe 宋体 Std L")
        font.setPointSize(14)
        self.port_close.setFont(font)
        self.port_close.setObjectName("port_close")
        self.folder_path = QtWidgets.QLineEdit(Dialog)
        self.folder_path.setGeometry(QtCore.QRect(90, 110, 491, 41))
        self.folder_path.setObjectName("folder_path")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.title.setText(_translate("Dialog", "ZigBee上位机"))
        self.select_folder.setText(_translate("Dialog", "选择保存数据的文件夹"))
        self.title_2.setText(_translate("Dialog", "选择串口"))
        self.port_open.setText(_translate("Dialog", "打开串口"))
        self.port_close.setText(_translate("Dialog", "关闭串口"))

