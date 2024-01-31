# ここに編集ページのコードを書く
import sys
import shutil
import os
from PySide6.QtWidgets import *
from PySide6 import QtGui,QtCore
from PySide6.QtCore import Qt
from PySide6.QtCore import Signal, Slot

from components.Menubar import Menubar
from components.toolBar import ToolBar
from components.imageWindow import ImageWindow
from components.scroll import ScrollArea

class EditPage(QMainWindow):
    closed = Signal()  # Signal to indicate the window is closed

    def __init__(self):
        super().__init__()
        self.resize(1000,600)
        self.setWindowTitle("PostProcesser")

        self.createMenuBar()
        self.createDockBar()
        self.initUI()
    
    def initUI(self):



        # 上部のメッセージエリア
        messageArea = QLabel("上部のメッセージエリア")
        messageArea.setStyleSheet("background-color: lightgray;")
        messageArea.setAlignment(Qt.AlignCenter)

        

        #キャンバス
        self.imageWindow = ImageWindow()  # キャンバスを作成
        self.setCentralWidget(self.imageWindow) # キャンバスをセントラルウィジェットに設定
        self.scrollArea = ScrollArea(self)  # スクロールエリアを作成
        self.layout = QVBoxLayout(self) # レイアウトを作成
        self.layout.addWidget(self.scrollArea)  # レイアウトにスクロールエリアを追加
        self.imageWindow = ImageWindow(self,width=4000,height=3000)    # スクロールエリアに追加するウィジェットを作成
        self.scrollArea.addWidget(self.imageWindow) # スクロールエリアにウィジェットを追加

         # メインレイアウト
        layoutMain = QVBoxLayout()
        layoutMain.addWidget(messageArea,1)
        layoutMain.addWidget(self.scrollArea,4)
        

        # メインウィジェットにメインレイアウトを設定
        widgetMain = QWidget()
        widgetMain.setLayout(layoutMain)
        self.setCentralWidget(widgetMain)

    def createDockBar(self):
        #ツールバー
        self.toolDock = QDockWidget("tool",self)
        self.toolBar = QWidget()
        ToolBar(self.toolBar)
        self.toolDock.setWidget(self.toolBar)
        self.addDockWidget(Qt.LeftDockWidgetArea, self.toolDock)

    def createMenuBar(self):
        self.menuBars = Menubar(self)

        # メニューバーの設定
        self.menuBars.closeAction = lambda x=None: self.close()
        self.menuBars.saveAction = lambda x=None: self.SaveImage()
        self.menuBars.exportAction = lambda x=None: self.SaveImage(exportFlg=True)
        
        self.menuBars.updateAction()

        self.setMenuBar(self.menuBars)

    def getEditImagePath(self)->str:
        for f in os.listdir("./img/edit"):
            if os.path.isfile(os.path.join("./img/edit", f)) and f != ".gitignore" and f != ".DS_Store":
                return os.path.join("./img/edit", f)

    def get_download_folder_path(self):
        # 一般的なOSでのダウンロードフォルダのパスを返す
        if os.name == 'nt':  # Windowsの場合
            return os.path.join(os.path.expanduser('~'), 'Downloads')
        else:  # macOSやLinuxの場合
            return os.path.expanduser('~/Downloads')

    def SaveImage(self,exportFlg=False):
        imagePath = self.getEditImagePath()
        savedForlderPath = "./img/saved"
        if imagePath!="":
            shutil.copy(imagePath,savedForlderPath)
            # print("save")
            if exportFlg:
                newImagePath = os.path.join(savedForlderPath, imagePath.split("/")[-1].split(".")[0]+"."+imagePath.split("/")[-1].split(".")[1])
                print(newImagePath)
                self.toExportImageFromEditFile(newImagePath)
        

    def toExportImageFromEditFile(self,imagePath=None):
        # print(f"export {imagePath}")
        if imagePath!="":
            defaultDir = self.get_download_folder_path()
            defaultPath = os.path.join(defaultDir, imagePath.split("/")[-1].split(".")[0]+"_export."+imagePath.split("/")[-1].split(".")[1])
            print(defaultPath)
            filePath, _ = QFileDialog.getSaveFileName(self, "画像をエクスポート", defaultPath, "All Files (*);;PNG Files (*.png);;JPEG Files (*.jpg)")
            if filePath:
                shutil.copy(imagePath,filePath)


    def showEvent(self, event):
        self.initUI()
        super().showEvent(event)

    def closeEvent(self, event):
        self.closed.emit()  # Emit the closed signal
        event.accept()

        


if __name__ == '__main__':
    app = QApplication(sys.argv)
    editPage = EditPage()
    editPage.show()
    sys.exit(app.exec_())