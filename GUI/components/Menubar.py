import sys
from PySide6.QtWidgets import *
from PySide6 import QtGui, QtCore


class Menubar:
    def __init__(self, parent: QWidget):
        # 以下はテスト
        self.button1 = QPushButton("画像を保存")
        self.button2 = QPushButton("TopPageに戻る")
        self.button3 = QPushButton("Download")

        self.button1.clicked.connect(lambda x: print("Hello! from gazouhozon"))
        self.button2.clicked.connect(lambda x: print("Hello! from TopPage"))
        self.button3.clicked.connect(lambda x: print("Hello! from download"))
        layout = QHBoxLayout()
        layout.addWidget(self.button1, alignment=QtCore.Qt.AlignTop)
        layout.addWidget(self.button2, alignment=QtCore.Qt.AlignTop)
        layout.addWidget(self.button3, alignment=QtCore.Qt.AlignTop)  # ボタンが上部に配置される
        # layout.addWidget(self.button1)
        # layout.addWidget(self.button2)　　　ボタンが中央に配置される
        parent.setLayout(layout)


class DebugWindow(QWidget):
    def __init__(self, parent=None):
        super(DebugWindow, self).__init__(parent)
        self.setWindowTitle("デバッグ用ウィンドウ")
        self.resize(500, 500)
        self.Menubar = Menubar(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    DebugWindow = DebugWindow()
    DebugWindow.show()
    sys.exit(app.exec_())
