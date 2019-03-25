# -*- coding: utf-8 -*-
from bug_system.gui_pyqt5.bug1_ui import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.submit_table.cellChanged.connect(self.on_table_show)

    def on_table_show(self, p_int, p_int_1):
        print(p_int, p_int_1)


    # def onChinaClicked(self):
    #     self.Title.setText("Hello China")
    # def onlineEditTextChanged(self, p_str):
    #     self.Title.setText(p_str)