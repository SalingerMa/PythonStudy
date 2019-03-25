# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QToolTip, QPushButton, QMessageBox
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import QCoreApplication


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.setUI()

    def setUI(self):
        QToolTip.setFont(QFont('SansSerif', 10))
        self.resize(500, 150)
        self.move(100, 100)
        self.setWindowIcon(QIcon('./Title.ico'))
        self.setWindowTitle("Hello world")

        self.setToolTip("<b>this is widget</b>")

        btn = QPushButton("quit Button", self)  # self类似于C++ this指针
        btn.setToolTip("This is a button will quit itself")
        btn.clicked.connect(QCoreApplication.instance().quit)
        btn.resize(btn.sizeHint())
        btn.move(0, 0)

        self.show()

    def closeEvent(self, event):

        reply = QMessageBox.question(self, 'Message',
                                     "Are you sure to quit?", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    ex = Example()

    sys.exit(app.exec_())
