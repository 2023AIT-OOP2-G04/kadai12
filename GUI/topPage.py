# ここにトップページのコードを書く
import sys
import shutil
import os
from PySide6.QtWidgets import *
from PySide6 import QtGui,QtCore
from PySide6.QtCore import Qt
from PySide6.QtCore import Signal, Slot
from PySide6.QtGui import QPixmap
from components.scroll import ScrollArea
from components.IshikawaLayoutTopPgae1 import LayoutTopPage
from editPage import EditPage
# from components.WindowTest import SecondWindow as EditPage

class TopPage(QMainWindow):
    def __init__(self):
        super().__init__()

        # ウィンドウの設定
        self.setWindowTitle("PostProcesser")
        self.setGeometry(100, 100, 1600, 1000)
        self.createMenuBar()
        self.initUI()


    def createMenuBar(self):
        # menuバーの設定

        self.fileMenu = self.menuBar().addMenu("ファイル")
        self.fileMenu.setStyleSheet("""
            QMenu {
                font-size: 16pt;
                padding: 10px;
            }
            QMenu::item {
                padding: 10px 20px;
                background-color: transparent;
            }
            QMenu::item:selected, QMenu::item:hover {
                background-color: #0078d7; /* ハイライト時の背景色 */
                color: white;              /* ハイライト時のテキスト色 */
            }
        """)

        self.fileMenu.addAction("新規作成", self.toEditWindowFromNewFile)
        self.fileMenu.addAction("開く", self.toEditWindowFromOpenFile)


    def initUI(self):

        
        self.scrollArea = ScrollArea(self)  # スクロールエリアを作成
        self.layoutTopPage = LayoutTopPage(self)    # スクロールエリアに追加するウィジェットを作成
        self.scrollArea.addWidget(self.layoutTopPage)   # スクロールエリアにウィジェットを追加

        self.setCentralWidget(self.scrollArea)

        # 部品にアクションを追加
        self.layoutTopPage.buttonOpen.clicked.connect(self.toEditWindowFromOpenFile)
        for pixImage in self.layoutTopPage.pixImages:
            pixImage.openAction=lambda x=pixImage: self.toEditWindowFromSavedFile(x.imagePath)
            pixImage.saveAction=lambda x=pixImage: self.toExportImageFromSavedFile(x.imagePath)


    # editフォルダ内の画像をリセットする関数
    def resetEditFolder(self):
        # editフォルダ内の.gitingoreと.DS_Storeを除いたファイルを削除
        for f in os.listdir("./img/edit"):
            if os.path.isfile(os.path.join("./img/edit", f)) and f != ".gitignore" and f != ".DS_Store":
                os.remove(os.path.join("./img/edit", f))

    def toEditWindowFromNewFile(self):
        self.resetEditFolder()
        self.openEditWindow()
    
    def toEditWindowFromOpenFile(self):
        # print("open file")
        # QFileDialogを作成して画像ファイルのファイルパスを取得
        filePath = QFileDialog.getOpenFileName(self, "画像を開く", "./", "Image Files (*.png *.jpg *.bmp)")[0]
        print(filePath)
        # ファイルパスが空でなければ画像を./img/savedと./img/editにコピー
        if filePath !="":
            shutil.copy(filePath,"./img/saved")
            self.resetEditFolder()
            shutil.copy(filePath,"./img/edit")
            self.openEditWindow()

    def toEditWindowFromSavedFile(self,imagePath=None):
        # print(f"open {imagePath}")
        if imagePath!="":
            self.resetEditFolder()
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
            filePath, _ = QFileDialog.getSaveFileName(self, "画像をエクスポート", defaultPath, "All Files (*);;PNG Files (*.png);;JPEG Files (*.jpg)")
            if filePath:
                shutil.copy(imagePath,filePath)
        


    def openEditWindow(self):
        self.hide()  # Hide the main window
        self.editWindow=EditPage()
        self.editWindow.closed.connect(self.show)  # Connect to the closed signal
        self.editWindow.show()

    def showEvent(self, event):
        self.initUI()
        super().showEvent(event)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    topPage = TopPage()
    topPage.show()
    sys.exit(app.exec_())