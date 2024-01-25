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
        self.fileNames = []
        self.folderPath = "./img/saved/"
        self.getFileNames()
        self.initUI()


    def initUI(self):
        
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

        layout_buttons = QHBoxLayout()
        layout_buttons.addLayout(layout_upload)
        layout_buttons.addLayout(layout_download)

        self.layout = QVBoxLayout()
        self.layout.setSpacing(60)
        self.layout.addLayout(layout_message)
        self.layout.addLayout(layout_buttons)
        self.layoutImages=QVBoxLayout()
        self.layoutImages.setSpacing(100)
        self.layoutImages.addStretch()
        

        for count,fileName in enumerate(self.fileNames):
            if count%2==0:
                self.layoutImagesTmp=QHBoxLayout()
                self.layoutImagesTmp.addLayout(self.showImage(self.folderPath+fileName))
            else:
                self.layoutImagesTmp.addLayout(self.showImage(self.folderPath+fileName))
                self.layoutImages.addLayout(self.layoutImagesTmp)
                self.layoutImages.addStretch()
        
        # もし画像の数が奇数ならレイアウトを調整
        if len(self.fileNames)%2==1:
            # 架空の画像を生成してレイアウトを埋める
            layoutFillSpace = self.showImage()
            self.layoutImagesTmp.addLayout(layoutFillSpace)
            self.layoutImages.addLayout(self.layoutImagesTmp)
            self.layoutImages.addStretch()
    
        self.layout.addLayout(self.layoutImages)

        
        self.setLayout(self.layout)


    #画像の表示関数
    def showImage(self,imagePath:str=None) -> QHBoxLayout:
        if imagePath:
            beforeimg = QImage(imagePath)
            afterimg = beforeimg.scaled(500,500,QtCore.Qt.AspectRatioMode.KeepAspectRatio)
            image = QLabel()
            image.setPixmap(QPixmap.fromImage(afterimg))
        else:
            image = QLabel()
            image.setFixedSize(500,500)
        layout_image = QHBoxLayout()
        layout_image.addWidget(image,alignment=QtGui.Qt.AlignHCenter)
        return layout_image
        
    #フォルダ内のファイル名を取得
    def getFileNames(self) :
            # savedフォルダ内から.gitignoreと.DS_Storeを除いたファイル名の配列を取得
            self.fileNames = [f for f in os.listdir(self.folderPath) if os.path.isfile(os.path.join(self.folderPath, f)) and f != ".gitignore" and f != ".DS_Store"]
            # print(self.fileNames)
                
                        
        
        
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      

if __name__ == "__main__":
    app = QApplication(sys.argv)
    # app.setStyleSheet('QLabel{border: 1px solid black;}')
    main_widget = LayoutTopPage()
    main_widget.show()
    app.exec()