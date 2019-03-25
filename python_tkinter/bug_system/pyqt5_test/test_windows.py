# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
from bug_system.pyqt5_test.test import Ui_MainWindow
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.Title.setText("hello Python")
        self.world.clicked.connect(self.onWorldClicked)
        self.china.clicked.connect(self.onChinaClicked)
        self.lineEdit.textChanged.connect(self.onlineEditTextChanged)

    def onWorldClicked(self, remark):
        print(remark)
        self.Title.setText("Hello World")

    def onChinaClicked(self):
        self.Title.setText("Hello China")
    def onlineEditTextChanged(self, p_str):
        self.Title.setText(p_str)