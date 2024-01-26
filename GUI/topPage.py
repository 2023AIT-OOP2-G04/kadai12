# ここにトップページのコードを書く
import sys
import shutil
import os
from PySide6.QtWidgets import *
from PySide6 import QtGui,QtCore

from components.scroll import ScrollArea
from components.IshikawaLayoutTopPgae1 import LayoutTopPage
# from editPage import EditPage
from components.WindowTest import SecondWindow as EditPage

class TopPage(QMainWindow):
    def __init__(self):
        super().__init__()

        # ウィンドウの設定
        self.setWindowTitle("PostProcesser")
        self.setGeometry(100, 100, 1600, 1000)
        self.initUI()

    def initUI(self):

        # menuバーの設定
        self.fileMenu = self.menuBar().addMenu("ファイル")
        self.fileMenu.addAction("新規作成", self.toEditWindowFromNewFile)
        self.fileMenu.addAction("開く", self.toEditWindowFromOpenFile)

        
        self.scrollArea = ScrollArea(self)  # スクロールエリアを作成
        self.layoutTopPage = LayoutTopPage(self)    # スクロールエリアに追加するウィジェットを作成
        self.scrollArea.addWidget(self.layoutTopPage)   # スクロールエリアにウィジェットを追加

        self.setCentralWidget(self.scrollArea)

        # 部品にアクションを追加
        self.layoutTopPage.buttonOpen.clicked.connect(self.toEditWindowFromOpenFile)
        for pixImage in self.layoutTopPage.pixImages:
            pixImage.openAction=lambda x=pixImage: self.toEditWindowFromSavedFile(x.imagePath)
            pixImage.saveAction=lambda x=pixImage: self.toExportImageFromSavedFile(x.imagePath)


    def toEditWindowFromNewFile(self):
        print("new file")
    
    def toEditWindowFromOpenFile(self):
        # print("open file")
        # QFileDialogを作成して画像ファイルのファイルパスを取得
        filePath = QFileDialog.getOpenFileName(self, "画像を開く", "./", "Image Files (*.png *.jpg *.bmp)")[0]
        print(filePath)
        # ファイルパスが空でなければ画像を./img/savedと./img/editにコピー
        if filePath !="":
            shutil.copy(filePath,"./img/saved")
            shutil.copy(filePath,"./img/edit")
            self.openEditWindow()

    def toEditWindowFromSavedFile(self,imagePath=None):
        # print(f"open {imagePath}")
        if imagePath!="":
            shutil.copy(imagePath,"./img/edit")
            self.openEditWindow()
    
    def get_download_folder_path(self):
        # 一般的なOSでのダウンロードフォルダのパスを返す
        if os.name == 'nt':  # Windowsの場合
            return os.path.join(os.path.expanduser('~'), 'Downloads')
        else:  # macOSやLinuxの場合
            return os.path.expanduser('~/Downloads')

    def toExportImageFromSavedFile(self,imagePath=None):
        # print(f"export {imagePath}")
        if imagePath!="":
            defaultDir = self.get_download_folder_path()
            defaultPath = os.path.join(defaultDir, imagePath.split("/")[-1].split(".")[0]+"_export."+imagePath.split("/")[-1].split(".")[1])
            print(defaultPath)
            filePath, _ = QFileDialog.getSaveFileName(self, "画像をエクスポート", defaultPath, "PNG Files (*.png);;JPEG Files (*.jpg);;All Files (*)")
            if filePath:
                shutil.copy(imagePath,filePath)
        


    def openEditWindow(self):
        self.hide()  # Hide the main window
        self.editWindow=EditPage()
        self.editWindow.closed.connect(self.show)  # Connect to the closed signal
        self.editWindow.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    topPage = TopPage()
    topPage.show()
    sys.exit(app.exec_())