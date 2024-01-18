import sys
from PySide6.QtWidgets import *
from PySide6 import QtGui,QtCore

# 画像を表示するウィンドウのクラス
class ImageWindow(QLabel):
    def __init__(self, filename=None, parent=None):
        super(ImageWindow, self).__init__(parent)
        if filename:
            self.imagePath=filename
            self.setImage(filename)

    def setImage(self, filename=None):
        if filename:
            self.imagePath=filename
        self.Image=QtGui.QImage(self.imagePath)
        # 写真のサイズが800*600になるように元のアスペクト比を保ったままリサイズ
        self.Image=self.Image.scaled(800,600,QtCore.Qt.KeepAspectRatio)


class DebugWindow(QWidget):
    def __init__(self, parent=None):
        super(DebugWindow, self).__init__(parent)
        self.setWindowTitle("デバッグ用ウィンドウ")
        self.resize(800, 600)
        filename="./img/edit/20240111_141517.jpg"
        self.imageWindow=ImageWindow(filename=filename,parent=self)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    debugWindow = DebugWindow()
    debugWindow.show()
    sys.exit(app.exec_())