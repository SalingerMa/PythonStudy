# -*- coding: utf-8 -*-
from gui_pyqt5.bug1_ui import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from common.function import Common
from common.config import TableName
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.init_table(table_obj=self.submit_table,table_name=TableName.table1.value)

        self.submit_table.cellChanged.connect(self.on_table_show)

    def init_table(self, table_obj, table_name):
        columns = Common.get_table_column(table_name)
        table_data = Common.get_table_data(table_name)
        rows = []
        for key, value in table_data.items():
            rows.append(key)
        self.init_table_head(table_obj, columns, rows)


    def on_table_show(self, p_int, p_int_1):
        print(p_int, p_int_1)

    def write_table(self):
        pass

    def init_table_head(self, table_obj,columns, rows):
        table_obj.setColumnCount(len(columns))
        table_obj.setRowCount(len(rows))

        table_obj.setHorizontalHeaderLabels(columns)
        table_obj.setVerticalHeaderLabels(rows)


    # def onChinaClicked(self):
    #     self.Title.setText("Hello China")
    # def onlineEditTextChanged(self, p_str):
    #     self.Title.setText(p_str)