# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
from bug_system.pyqt5_test.test_windows import MainWindow
import sys

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())