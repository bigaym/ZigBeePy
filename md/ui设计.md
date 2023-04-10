好的，这里是一个简单的示例程序，使用PyQt5实现GUI界面，并提供选择文件夹的对话框、串口打开/关闭按钮以及显示串口内容的文本框。

需要安装PyQt5库和pyserial库，可以使用以下命令进行安装：

```
pip install pyqt5 pyserial
```

以下是代码：

```Python
import sys
import os
import serial
import serial.tools.list_ports
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from PyQt5.QtCore import Qt, QThread, pyqtSignal
from PyQt5.QtGui import QTextCursor
from ui_mainwindow import Ui_MainWindow

BUFFER_SIZE = 1024  # 缓冲区大小，用于读取串口数据


class SerialThread(QThread):
    received = pyqtSignal(str)  # 自定义信号，用于发送接收到的数据

    def __init__(self, port, baudrate):
        super().__init__()
        self.port = port
        self.baudrate = baudrate
        self.stop = False

    def run(self):
        try:
            ser = serial.Serial(self.port, self.baudrate, timeout=0)
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


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # 初始化串口列表
        ports = [port.device for port in serial.tools.list_ports.comports()]
        self.comboBox_port.addItems(ports)
        if ports:
            self.comboBox_port.setCurrentIndex(0)

        # 绑定按钮事件
        self.pushButton_open.clicked.connect(self.open_serial)
        self.pushButton_close.clicked.connect(self.close_serial)
        self.pushButton_choose_dir.clicked.connect(self.choose_directory)

        # 初始化串口线程
        self.serial_thread = None

    def open_serial(self):
        if self.serial_thread and self.serial_thread.isRunning():
            return  # 串口已经打开，不重复打开

        port = self.comboBox_port.currentText()
        baudrate = int(self.comboBox_baud_rate.currentText())

        self.serial_thread = SerialThread(port, baudrate)
        self.serial_thread.received.connect(self.append_text)
        self.serial_thread.start()

        self.pushButton_open.setEnabled(False)
        self.pushButton_close.setEnabled(True)
        self.comboBox_port.setEnabled(False)
        self.comboBox_baud_rate.setEnabled(False)

    def close_serial(self):
        if self.serial_thread:
            self.serial_thread.stop_thread()
            self.serial_thread.wait()
            self.serial_thread = None

        self.pushButton_open.setEnabled(True)
        self.pushButton_close.setEnabled(False)
        self.comboBox_port.setEnabled(True)
        self.comboBox_baud_rate.setEnabled(True)

    def choose_directory(self):
        directory = QFileDialog.getExistingDirectory(self, "选择文件夹", os.getcwd())
        if directory:
            self.lineEdit_dir.setText(directory)

    def append_text(self, text):
        self.textEdit_output.moveCursor(QTextCursor.End)
        self.textEdit_output.insertPlainText(text)
        self.textEdit_output.moveCursor(QTextCursor.End)
```

这里的GUI界面是使用Qt Designer设计的，保存在`ui_mainwindow.py`文件中。你可以使用以下命令来转换.ui文件为.py文件：

```
pyuic5 ui_mainwindow.ui -o ui_mainwindow.py
```

这里是Qt Designer设计的UI界面示例图：

![UI界面示例图](https://i.imgur.com/p8W6bfG.png)

在代码中，我们定义了一个`SerialThread`类，用于读取串口数据并发送数据到主线程；定义了一个`MainWindow`类，继承自`QMainWindow`和UI界面的类，并在其中实现了选择文件夹、串口打开/关闭、串口读取和显示串口内容等功能。

在`SerialThread`类中，我们定义了一个`received`信号，用于将接收到的串口数据发送到主线程；在`run`方法中通过PySerial模块读取串口数据，并在读取到数据时发送`received`信号。

在`MainWindow`类中，我们初始化了串口列表、定义了打开/关闭串口的方法，并将串口读取线程的信号连接到`append_text`方法，该方法将接收到的数据添加到文本框中。

在这个示例程序中，我们使用了`QThread`类来实现读取串口数据的多线程，并通过自定义信号将接收到的数据传输到主线程，以更新界面。同时，我们还使用了PyQt5中提供的许多UI组件和事件处理机制，实现了一个简单的串口调试工具。



```python
import sys
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6 import uic
class MainWindow(QtWidgets.QMainWindow):    
    def __init__(self, *args, **kwargs):        
        super().__init__(*args, **kwargs)        
        uic.loadUi("mainwindow.ui", self)
        app = QtWidgets.QApplication(sys.argv)
        window = MainWindow()
        window.show()
        app.exec_()
```