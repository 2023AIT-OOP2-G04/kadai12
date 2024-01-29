import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import Qt
from PySide6 import QtGui,QtCore
import os

# 画像を表示するウィンドウのクラス
class ImageWindow(QLabel):
    # 画像のサイズはデフォルトで800x600
    def __init__(self,parent: QDockWidget| None=None,width:int=800,height:int=600):
        super(ImageWindow, self).__init__(parent)
        self.imagePath=None
        self.width=width
        self.height=height
        self.updateImage()

    def setImage(self, filename=None):
        if filename:
            self.imagePath=filename
        self.Image=QtGui.QImage(self.imagePath)
        # 写真のサイズが規定のサイズになるように元のアスペクト比を保ったままリサイズ
        self.Image=self.Image.scaled(self.width,self.height,QtCore.Qt.AspectRatioMode.KeepAspectRatio)
        self.setPixmap(QtGui.QPixmap.fromImage(self.Image))

    def resizeImage(self,width:int,height:int):
        self.width=width
        self.height=height
        self.updateImage()

    def updateImage(self):
        folderPath="./img/edit/"
        filename=[fileName for fileName in os.listdir(folderPath) if fileName!=".gitignore" and fileName!=".DS_Store" ]
        if len(filename)>0:
            self.imagePath=folderPath+filename[0]
            self.setImage()
        else:
            # print("画像が見つかりませんでした")
            self.setText("画像が見つかりませんでした")

class DebugWindow(QMainWindow):
    def __init__(self, parent=None):
        super(DebugWindow, self).__init__(parent)
        self.setWindowTitle("デバッグ用ウィンドウ")
        self.resize(800, 600)
        #self.imageWindow=ImageWindow(parent=self)
        self.imageDock = QDockWidget("canvas",self)
        self.imageWindow = QWidget()
        ImageWindow(self.imageWindow)
        self.imageDock.setWidget(self.imageWindow)

        self.addDockWidget(Qt.RightDockWidgetArea, self.imageDock)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    debugWindow = DebugWindow()
    debugWindow.show()
    sys.exit(app.exec_())