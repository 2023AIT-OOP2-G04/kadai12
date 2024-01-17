# ここに編集ページのコードを書く
import sys
from PySide6.QtWidgets import *
from PySide6 import QtGui,QtCore

class EditPage(QWidget):
    def __init__(self):
        super().__init__()
        # 以下はテスト
        self.button = QPushButton("Click me")
        self.button.clicked.connect(lambda x: print("Hello! from EditPage"))
        layout = QHBoxLayout()
        layout.addWidget(self.button)
        self.setLayout(layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    editPage = EditPage()
    editPage.show()
    sys.exit(app.exec_())