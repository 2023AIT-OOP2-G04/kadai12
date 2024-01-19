import sys
import os
from PySide6.QtWidgets import *
from PySide6.QtGui import QPixmap
from PySide6 import QtGui, QtCore
from imageWindow import ImageWindow

class ScrollArea(QScrollArea):
    def __init__(self, parent=None):
        super(ScrollArea, self).__init__(parent)

        # スクロールバーのポリシーを設定
        self.setWidgetResizable(True)
        self.widget = QWidget()
        self.setWidget(self.widget)
        self.layout = QVBoxLayout(self.widget)
        self.layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)
       
       
    # スクロールエリアにウィジェットを追加する
    def addWidget(self, widget):
        self.layout.insertWidget(self.layout.count() - 1, widget)


class DebugWindow(QWidget):
    def __init__(self, parent=None):
        super(DebugWindow, self).__init__(parent)
        self.setWindowTitle("デバッグ用ウィンドウ")
        self.resize(1600, 1200)

        # 以下は使い方の例
        self.scrollArea = ScrollArea(self)  # スクロールエリアを作成
        self.layout = QVBoxLayout(self) # レイアウトを作成
        self.layout.addWidget(self.scrollArea)  # レイアウトにスクロールエリアを追加
        self.imageWindow = ImageWindow(self,width=4000,height=3000)    # スクロールエリアに追加するウィジェットを作成
        self.scrollArea.addWidget(self.imageWindow) # スクロールエリアにウィジェットを追加

if __name__ == "__main__":
    app = QApplication(sys.argv)
    DebugWindow = DebugWindow()
    DebugWindow.show()
    sys.exit(app.exec_())
