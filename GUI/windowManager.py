# 2つの画面の遷移を管理する
import sys
from PySide6.QtWidgets import *
from PySide6 import QtGui,QtCore

from topPage import TopPage
from editPage import EditPage

class WindowManager(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("アプリの名前")

        self.topPage = TopPage()
        self.editPage = EditPage()
        self.stack = QStackedLayout()
        self.stack.addWidget(self.topPage)
        self.stack.addWidget(self.editPage)
        self.setLayout(self.stack)

        # 画面遷移を行うイベントリスナーを設定
        self.topPage.button.clicked.connect(self.changePage)
        self.editPage.button.clicked.connect(self.changePage)

    # 画面遷移を行う関数
    def changePage(self):
        self.stack.setCurrentIndex(1-self.stack.currentIndex())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    windowManager = WindowManager()
    windowManager.show()
    sys.exit(app.exec_())