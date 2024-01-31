import sys
from PySide6.QtWidgets import *
from PySide6 import QtGui, QtCore


class Menubar(QMenuBar):
    def __init__(self, parent: QWidget):
        super().__init__(parent=parent)

        # 　メニュー１：　ファイル
        self.Menubar1 = self.addMenu("ファイル")
        # 　メニュー２：　TopPageに戻る
        self.Menubar2 = self.addMenu("移動")
        # 　メニュー１にアクションを追加
        self.saveAction=lambda x=None: print("Hello! from saveAction")
        self.exportAction=lambda x=None: print("Hello! from export")

        self.Menubar1.addAction("画像を保存", self.saveAction)
        self.Menubar1.addAction("エクスポート", self.exportAction)
        # 　メニュー２にアクションを追加
        self.closeAction=lambda x=None: print("Hello! from closeAction")
        self.Menubar2.addAction("TopPageに戻る", self.closeAction)
    
    def updateAction(self):
        self.Menubar1.clear()
        self.Menubar1.addAction("画像を保存", self.saveAction)
        self.Menubar1.addAction("エクスポート", self.exportAction)
        self.Menubar2.clear()
        self.Menubar2.addAction("TopPageに戻る", self.closeAction)


class DebugWindow(QMainWindow):
    def __init__(self, parent=None):
        super(DebugWindow, self).__init__(parent)
        self.setWindowTitle("デバッグ用ウィンドウ")
        self.resize(500, 500)

        # メニューバーを作成し、メインウィンドウに設定
        self.menu_bar = Menubar(self)
        self.setMenuBar(self.menu_bar)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    DebugWindow = DebugWindow()
    DebugWindow.show()
    sys.exit(app.exec_())
