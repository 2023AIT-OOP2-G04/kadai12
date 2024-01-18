# ここに編集ページのコードを書く
import sys
from typing import Optional
from PySide6.QtCore import Qt
from PySide6.QtWidgets import *
from PySide6 import QtGui,QtCore
from PySide6.QtWidgets import QWidget

#ツールバーのGUI
class ToolBar():
    def __init__(self,parent:QWidget):
        
        layout = QVBoxLayout()

        #ペンツール
        self.button = QPushButton("ペン")
        self.button.clicked.connect(lambda x: print("ペンツール"))
        layout.addWidget(self.button)

        #消しゴムツール
        self.button = QPushButton("消しゴム")
        self.button.clicked.connect(lambda x: print("消しゴムツール"))
        layout.addWidget(self.button)

        #白黒加工ツール
        self.button = QPushButton("白黒加工")
        self.button.clicked.connect(lambda x: print("白黒加工ツール"))
        layout.addWidget(self.button)

        #顔・物体検出して色変更ツール
        self.button = QPushButton("顔・物体検出して色変更")
        self.button.clicked.connect(lambda x: print("顔・物体検出して色変更ツール"))
        layout.addWidget(self.button)

        #顔・物体検出して切り取りツール
        self.button = QPushButton("顔・物体検出して切り取り")
        self.button.clicked.connect(lambda x: print("顔・物体検出して切り取りツール"))
        layout.addWidget(self.button)

        #画像色変更ツール
        self.button = QPushButton("画像色変更")
        self.button.clicked.connect(lambda x: print("画像色変更ツール"))
        layout.addWidget(self.button)

        #縦横比変更ツール
        self.button = QPushButton("縦横比変更")
        self.button.clicked.connect(lambda x: print("縦横比変更ツール"))
        layout.addWidget(self.button)

        #画像イラスト挿入ツール
        self.button = QPushButton("画像イラスト挿入")
        self.button.clicked.connect(lambda x: print("画像イラスト挿入ツール"))
        layout.addWidget(self.button)

        #拡大縮小ツール
        self.button = QPushButton("拡大縮小")
        self.button.clicked.connect(lambda x: print("拡大縮小ツール"))
        layout.addWidget(self.button)

        parent.setLayout(layout)

class DebugWindow(QWidget):
    def __init__(self, parent=None):
        super(DebugWindow, self).__init__(parent)
        self.setWindowTitle("デバッグ用ウィンドウ")
        self.resize(100, 500)
        self.toolBar=ToolBar(self)
        
    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    debugWindow = DebugWindow()
    debugWindow.show()
    sys.exit(app.exec_())