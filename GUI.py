"""
python -m PyQt5.uic.pyuic XXX.ui -o YYY.py
ui转py文件
"""

import sys
import os
import serial
import serial.tools.list_ports
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from PyQt5.QtGui import QTextCursor
from MainWindow import Ui_Dialog
from PyQt5 import uic
from PyQt5.QtCore import Qt, QThread, pyqtSignal

BUFFER_SIZE = 1024  # 缓冲区大小，用于读取串口数据

class Window:
    def __init__(self):
        self.ui = uic.loadUi("ZigBee2PC.ui")


# 串口控制类
class SerialThread(QThread):
    received = pyqtSignal(str)  # 自定义信号，用于发送接收到的数据

    def __init__(self, port, baudrate):
        super().__init__()
        self.port = port
        self.baudrate = baudrate
        self.stop = False

    def run(self):
        try:
            ser = serial.Serial(self.port, self.baudrate, timeout=0.5)
        except Exception as e:
            self.received.emit(str(e))
            return

        while not self.stop:
            data = ser.read(BUFFER_SIZE)
            if data:
                self.received.emit(data.decode())

        ser.close()

    def stop_thread(self):
        self.stop = True





class MainWindow(QMainWindow, Ui_Dialog):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        # 设置窗口大小和名字
        self.setFixedSize(926, 656)
        self.setWindowTitle("ZigBee2PC")

        # 初始化串口列表
        ports = [port.device for port in serial.tools.list_ports.comports()]
        self.comboBox.addItems(ports)
        if ports:
            self.comboBox.setCurrentIndex(0)

        # 绑定按钮事件
        self.port_open.clicked.connect(self.open_serial)
        self.port_close.clicked.connect(self.close_serial)
        self.select_folder.clicked.connect(self.choose_directory)

        # 初始化串口线程
        self.serial_thread = None

    def open_serial(self):
        if self.serial_thread and self.serial_thread.isRunning():
            return  # 串口已经打开，不重复打开

        port = self.comboBox.currentText()
        # baudrate = int(self.comboBox_baud_rate.currentText())
        baudrate = 115200

        self.serial_thread = SerialThread(port, baudrate)
        self.serial_thread.received.connect(self.append_text)
        self.serial_thread.start()

        self.port_open.setEnabled(False)
        self.port_close.setEnabled(True)
        self.comboBox.setEnabled(False)
        # self.comboBox_baud_rate.setEnabled(False)

    def close_serial(self):
        if self.serial_thread:
            self.serial_thread.stop_thread()
            self.serial_thread.wait()
            self.serial_thread = None

        self.port_open.setEnabled(True)
        self.port_close.setEnabled(False)
        self.comboBox.setEnabled(True)
        # self.comboBox_baud_rate.setEnabled(True)

    def choose_directory(self):
        directory = QFileDialog.getExistingDirectory(self, "选择文件夹", os.getcwd())
        if directory:
            self.folder_path.setText(directory)
            # self.lineEdit_dir.setText(directory)

    def append_text(self, text):
        self.serial_print.moveCursor(QTextCursor.End)
        self.serial_print.insertPlainText(text)
        self.serial_print.moveCursor(QTextCursor.End)


