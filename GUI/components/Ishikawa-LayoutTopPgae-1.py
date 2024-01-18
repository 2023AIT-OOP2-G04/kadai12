import sys
from PySide6.QtWidgets import QApplication,QWidget,QLabel,QPushButton,QHBoxLayout,QGridLayout,QVBoxLayout,QScrollArea
from PySide6 import QtGui,QtCore
from PySide6.QtGui import QImage,QPixmap
import os

class MainWidget(QWidget):
    def __init__(self):
        super().__init__()
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


app = QApplication(sys.argv)
app.setStyleSheet('QLabel{border: 1px solid black;}')
main_widget = MainWidget()
main_widget.show()
app.exec()