import sys
import LogIn, MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow
import datahandle
import os
import PySide2

dirname_ = os.path.dirname(PySide2.__file__)
plugin_path = os.path.join(dirname_, 'plugins', 'platforms')
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = plugin_path

if __name__ == '__main__':
    app = QApplication(sys.argv)
    log_in = QMainWindow()

    ui_log_in = LogIn.Ui_LogIn()
    ui_log_in.setupUi(log_in)
    log_in.show()

    sys.exit(app.exec_())
