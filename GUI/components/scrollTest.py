import sys
import os
from PySide6.QtWidgets import *
from PySide6.QtGui import QPixmap
from PySide6 import QtGui, QtCore
from imageWindow import ImageWindow

class MainWidget(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setWindowTitle('トップページ') # ウィンドウのタイトル
        self.setGeometry(100,100,600,600) # ウィンドウの位置(x,y)と大きさ(w,h)


        # メッセージボックスを作成
        message = QLabel("ここにメッセージを書きます。",alignment = QtCore.Qt.AlignCenter)
        message.setFixedSize(300,200)
        layout_message = QHBoxLayout()
        layout_message.addWidget(message)

        # アップロードボタンを作成
        self.button = QPushButton("アップロード")
        self.button.clicked.connect(lambda x: print("uploaded"))
        layout_upload = QHBoxLayout()
        layout_upload.addWidget(self.button)

        # ダウンロードボタンを作成
        self.button = QPushButton("ダウンロード")
        self.button.clicked.connect(lambda x: print("downloaded"))
        layout_download = QHBoxLayout()
        layout_download.addWidget(self.button)


        #画像の表示関数
        def showImages(name):
            image = QLabel()
            image.setPixmap(QPixmap(name))
            layout_image = QHBoxLayout()
            layout_image.addWidget(image)
            return layout_image
        
        #フォルダ内のファイル名を取得
        def showFilesName(path) :
             for fileName in os.listdir(path):
                 if fileName != ".gitignore":
                    if fileName != ".DS_Store":
                        print(fileName)
                        self.layout.addLayout(showImages(path+fileName))
        
        layout_buttons = QHBoxLayout()
        layout_buttons.addLayout(layout_upload)
        layout_buttons.addLayout(layout_download)

        self.layout = QVBoxLayout()
        self.layout.addLayout(layout_message)
        self.layout.addLayout(layout_buttons)
        showFilesName("./img/edit/")
        # self.layout.addLayout(showFilesName("./img/edit/"))


        self.setLayout(self.layout)


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
        self.layout.addStretch(1)


        self.topPage = MainWidget(self)
        self.addWidget(self.topPage)
        

    def addWidget(self, widget):
        self.layout.insertWidget(self.layout.count() - 1, widget)

class DebugWindow(QWidget):
    def __init__(self, parent=None):
        super(DebugWindow, self).__init__(parent)
        self.setWindowTitle("デバッグ用ウィンドウ")
        self.resize(1600, 1200)
        self.scrollArea = ScrollArea(self)
        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.scrollArea)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    DebugWindow = DebugWindow()
    DebugWindow.show()
    sys.exit(app.exec_())