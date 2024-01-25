import sys
from PySide6.QtWidgets import QApplication,QWidget,QLabel,QPushButton,QHBoxLayout,QGridLayout,QVBoxLayout,QScrollArea
from PySide6 import QtGui,QtCore
from PySide6.QtGui import QImage,QPixmap
import os


class LayoutTopPage(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent=parent)
        self.setWindowTitle('トップページ') # ウィンドウのタイトル
        self.setGeometry(100,100,1600,1200) # ウィンドウの位置(x,y)と大きさ(w,h)
        self.names = []


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
            beforeimg = QImage(name)
            afterimg = beforeimg.scaled(300,500,QtCore.Qt.AspectRatioMode.KeepAspectRatio)

            image = QLabel()
            image.setPixmap(QPixmap.fromImage(afterimg))
            layout_image = QHBoxLayout()
            layout_image.addWidget(image,alignment=QtGui.Qt.AlignHCenter)
            return layout_image
        
        #フォルダ内のファイル名を取得
        def showFilesName(path) :
             for fileName in os.listdir(path):
                 if fileName != ".gitignore":
                    if fileName != ".DS_Store":
                        print(fileName)
                        self.names.append(fileName)
                        layout_image = QHBoxLayout()
                        layout_image.addLayout(showImages(path+fileName))
                        self.layout.addLayout(layout_image)
        
        layout_buttons = QHBoxLayout()
        layout_buttons.addLayout(layout_upload)
        layout_buttons.addLayout(layout_download)

        self.layout = QVBoxLayout()
        self.layout.addLayout(layout_message)
        self.layout.addLayout(layout_buttons)

        showFilesName("./img/saved/")

        # layout_v = QVBoxLayout() 
        # layout_h = QHBoxLayout()
        # for i in range(len(self.names)):
        #     if i%2 == 1:
        #         showFilesName("./img/saved/")
        #     else:
        #         showFilesName("./img/saved/")
        # # layout_images = QHBoxLayout()
        # layout_images.addLayout(layout_v)
        # layout_images.addLayout(layout_h)

        # self.layout.addLayout(showFilesName("./img/edit/"))
        self.setLayout(self.layout)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      

if __name__ == "__main__":
    app = QApplication(sys.argv)
    # app.setStyleSheet('QLabel{border: 1px solid black;}')
    main_widget = LayoutTopPage()
    main_widget.show()
    app.exec()