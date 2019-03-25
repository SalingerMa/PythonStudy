import sys
from PyQt5.QtWidgets import *
from bug_system.config import Table
from bug_system.function import Common

class BugSys(QWidget):
    def __init__(self):
        super(BugSys, self).__init__()
        self.initUI()
    def table(self, table):


        columns = Common.get_table_column(table)

        TableWidget = QTableWidget(4, len(columns))

        # 设置水平方向的表头标签与垂直方向上的表头标签，注意必须在初始化行列之后进行，否则，没有效果
        TableWidget.setHorizontalHeaderLabels(columns)

        # newItem = QTableWidgetItem('张三')
        # TableWidget.setItem(0, 0, newItem)
        #
        # newItem = QTableWidgetItem('男')
        # TableWidget.setItem(0, 1, newItem)
        #
        # newItem = QTableWidgetItem('160')
        # TableWidget.setItem(0, 2, newItem)添加数据
        #

        return TableWidget




    def initUI(self):
        self.setWindowTitle("QTableWidget例子")
        self.resize(800, 700)

        self.frame = QFrame(self)
        layout = QHBoxLayout(self.frame)
        SubTableWidget = self.table(Table.sub_table.value)
        layout.addWidget(SubTableWidget)
        self.setLayout(layout)

        self.frame1 = QFrame(self)
        layout1 = QHBoxLayout(self.frame1)
        RestTableWidget = self.table(Table.rest_table.value)
        layout1.addWidget(RestTableWidget)
        self.setLayout(layout1)


        #Todo 优化1 设置垂直方向的表头标签
        #TableWidget.setVerticalHeaderLabels(['行1', '行2', '行3', '行4'])

        #TODO 优化 2 设置水平方向表格为自适应的伸缩模式
        ##TableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        #TODO 优化3 将表格变为禁止编辑
        #TableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)

        #TODO 优化 4 设置表格整行选中
        #TableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)

        #TODO 优化 5 将行与列的高度设置为所显示的内容的宽度高度匹配
        #QTableWidget.resizeColumnsToContents(TableWidget)
        #QTableWidget.resizeRowsToContents(TableWidget)

        #TODO 优化 6 表格头的显示与隐藏
        #TableWidget.verticalHeader().setVisible(False)
        #TableWidget.horizontalHeader().setVisible(False)

        #TOdo 优化7 在单元格内放置控件
        # comBox=QComboBox()
        # comBox.addItems(['男','女'])
        # comBox.addItem('未知')
        # comBox.setStyleSheet('QComboBox{margin:3px}')
        # TableWidget.setCellWidget(0,1,comBox)
        #
        # searchBtn=QPushButton('修改')
        # searchBtn.setDown(True)
        # searchBtn.setStyleSheet('QPushButton{margin:3px}')
        # TableWidget.setCellWidget(0,2,searchBtn)


if __name__ == '__main__':
    app=QApplication(sys.argv)
    win=BugSys()
    win.show()
    sys.exit(app.exec_())
