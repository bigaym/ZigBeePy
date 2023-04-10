from PyQt5.QtWidgets import QApplication
import sys
from GUI import Window, MainWindow

# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
  app = QApplication(sys.argv)
  window = MainWindow()
  window.show()
  sys.exit(app.exec())

# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
