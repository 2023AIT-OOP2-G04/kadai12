# ここに編集ページのコードを書く
import sys
from typing import Optional
from PySide6.QtCore import Qt
from PySide6.QtWidgets import *
from PySide6 import QtGui,QtCore
from PySide6.QtWidgets import QWidget

#ツールバーのGUI
class ToolBar():
    def __init__(self,parent:QDockWidget,mainWindow:QMainWindow=None):
        
        self.buttonLayout = QVBoxLayout()
        self.buttonLayout.setSpacing(10)
        self.buttonLayout.setContentsMargins(10, 10, 10, 10)
        
        self.buttonLayout.addStretch()
        self.buttonLayout.addWidget(QLabel("お絵描きツール"))

        # ペンと消しゴムの選択のためのボタン
        # ボタングループの設定
        self.toolButtonGroup = QButtonGroup()
        self.noneButton = QPushButton("選択ツール")
        self.penButton = QPushButton("ペン")
        self.eraserButton = QPushButton("消しゴム")
        self.noneButton.setChecked(True)

        toolLayout = QVBoxLayout()  # QVBoxLayoutを使用
        toolLayout.addWidget(self.noneButton)
        toolLayout.addWidget(self.penButton)
        toolLayout.addWidget(self.eraserButton)

        self.buttonLayout.addLayout(toolLayout)
        
        self.toolButtonGroup.addButton(self.noneButton, 1)
        self.toolButtonGroup.addButton(self.penButton, 2)
        self.toolButtonGroup.addButton(self.eraserButton, 3)
        # self.toolButtonGroup.buttonClicked.connect(self.changeTool)

        # 全消去ボタン
        self.clearButton = QPushButton("全消去")
        # self.clearButton.clicked.connect(self.clearDrawing)
        self.buttonLayout.addWidget(self.clearButton)

        self.buttonLayout.addStretch()
        self.buttonLayout.addWidget(QLabel("画像加工ツール"))

        #白黒加工ツール
        self.button = QPushButton("白黒加工")
        self.button.clicked.connect(lambda x: print("白黒加工ツール"))
        self.buttonLayout.addWidget(self.button)

        # #顔・物体検出して色変更ツール
        # self.button = QPushButton("顔・物体検出して色変更")
        # self.button.clicked.connect(lambda x: print("顔・物体検出して色変更ツール"))
        # self.buttonLayout.addWidget(self.button)

        # #顔・物体検出して切り取りツール
        # self.button = QPushButton("顔・物体検出して切り取り")
        # self.button.clicked.connect(lambda x: print("顔・物体検出して切り取りツール"))
        # self.buttonLayout.addWidget(self.button)

        #画像色変更ツール
        self.button = QPushButton("画像色変更")
        self.button.clicked.connect(lambda x: print("画像色変更ツール"))
        self.buttonLayout.addWidget(self.button)

        #縦横比変更ツール
        self.button = QPushButton("縦横比変更")
        self.button.clicked.connect(lambda x: print("縦横比変更ツール"))
        self.buttonLayout.addWidget(self.button)

        # #画像イラスト挿入ツール
        # self.button = QPushButton("画像イラスト挿入")
        # self.button.clicked.connect(lambda x: print("画像イラスト挿入ツール"))
        # self.buttonLayout.addWidget(self.button)

        #拡大縮小ツール
        self.button = QPushButton("拡大縮小")
        self.button.clicked.connect(lambda x: print("拡大縮小ツール"))
        self.buttonLayout.addWidget(self.button)


        self.buttonLayout.addStretch()
        # 拡大・縮小のスライダーまたはスピンボックスの設定
        self.scaleSpinBox = QSpinBox()
        self.scaleSpinBox.setRange(10, 400)  # 10% から 400% の範囲
        self.scaleSpinBox.setValue(100)  # 初期値は 100%
        # self.scaleSpinBox.valueChanged.connect(self.changeScale)
        scaleLayout = QHBoxLayout()
        scaleLayout.addWidget(QLabel("スケール:"))
        scaleLayout.addWidget(self.scaleSpinBox)
        self.buttonLayout.addLayout(scaleLayout)

        self.buttonLayout.addStretch()

        parent.setLayout(self.buttonLayout)

class DebugWindow(QMainWindow):
    def __init__(self, parent=None):
        super(DebugWindow, self).__init__(parent)
        self.setWindowTitle("デバッグ用ウィンドウ")
        self.resize(100, 500)
        self.toolDock = QDockWidget("aaa",self)
        self.toolBar = QWidget()
        ToolBar(self.toolBar)
        self.toolDock.setWidget(self.toolBar)

        self.addDockWidget(Qt.LeftDockWidgetArea, self.toolDock)
        
    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    debugWindow = DebugWindow()
    debugWindow.show()
    sys.exit(app.exec_())