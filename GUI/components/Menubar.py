import sys
from PySide6.QtWidgets import *
from PySide6 import QtGui, QtCore


class Menubar(QMenuBar):
    def __init__(self, parent: QWidget):
        super().__init__(parent=parent)

        # 　メニュー１：　ファイル
        self.Menubar1 = self.addMenu("ファイル")
        # 　メニュー２：　TopPageに戻る
        self.Menubar2 = self.addMenu("TopPageに戻る")
        # 　メニュー１にアクションを追加
        self.Menubar1.addAction("画像を保存", self.save_image)
        self.Menubar1.addAction("エクスポート", self.export)
        # 　メニュー２にアクションを追加
        self.Menubar2.addAction("TopPageに戻る", self.go_to_toppage)

    def save_image(self):
        print("Hello! from gazouwohozonn")

    def go_to_toppage(self):
        print("Hello! from TopPageに戻る")

    def export(self):
        print("Hello! from export")


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
