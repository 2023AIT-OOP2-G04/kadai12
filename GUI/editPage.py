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
from components.paintImageWindow import DrawingWidget,PenSettingsDialog,EraserSettingsDialog
# 1つ上の階層のフォルダをモジュールパスに追加
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from module.ppManager import PPManager

class EditPage(QMainWindow):
    closed = Signal()  # Signal to indicate the window is closed

    def __init__(self):
        super().__init__()
        self.ppManager = PPManager()
        self.resize(1000,600)
        self.setWindowTitle("PostProcesser")

        self.createMenuBar()
        self.createDockBar()
        self.initUI()
    
    def initUI(self):



        # 上部のメッセージエリア
        messageArea = QLabel('''    
                            <p style="font-size: 14px;">画像を保存する場合はメニューバーの「ファイル」 >> 「画像を保存」から</p>
                            <p style="font-size: 14px;">トップページに戻る場合はメニューバーの「移動」 >> 「TopPageに戻る」からできます</p>
                             ''')
        messageArea.setStyleSheet("background-color: gray;")
        messageArea.setAlignment(Qt.AlignCenter)

        

        # #キャンバス
        self.drawingWidget = DrawingWidget(imagePath=self.getEditImagePath(),parent=self)
        self.scrollArea = QScrollArea()  # スクロールエリアを作成
        self.scrollArea.setWidget(self.drawingWidget)  # DrawingWidgetをスクロールエリアに設定
        self.scrollArea.setWidgetResizable(True)  # スクロールエリアのサイズ変更を可能にする

         # メインレイアウト
        layoutMain = QVBoxLayout()
        layoutMain.addWidget(messageArea,1)
        layoutMain.addWidget(self.scrollArea,6)
        

        # メインウィジェットにメインレイアウトを設定
        self.mainWidget = QWidget()
        self.mainWidget.setLayout(layoutMain)
        self.setCentralWidget(self.mainWidget)  # スクロールエリアをメインウィンドウの中央のウィジェットとして設定

    def createDockBar(self):
        #ツールバー
        self.toolDock = QDockWidget("tool",self)
        self.toolBarWidget = QWidget()
        self.toolBar=ToolBar(self.toolBarWidget,mainWindow=self)

        # スタイル設定
        # ボタンのスタイルを設定するためのメソッド
        self.setStyleForButton(self.toolBar.penButton, False)
        self.setStyleForButton(self.toolBar.eraserButton, False)
        self.setStyleForButton(self.toolBar.noneButton, True)

        # 部品にアクションを追加
        self.toolBar.toolButtonGroup.buttonClicked.connect(self.changeTool)
        self.toolBar.clearButton.clicked.connect(self.clearDrawing)
        self.toolBar.scaleSpinBox.valueChanged.connect(self.changeScale)
        # 画像処理ツールのアクション
        self.toolBar.imageGrayButton.clicked.connect(lambda x=None: self.ppManager.k20114.grayScale())


        self.toolDock.setWidget(self.toolBarWidget)
        self.addDockWidget(Qt.LeftDockWidgetArea, self.toolDock)

    def createMenuBar(self):
        self.menuBars = Menubar(self)

        # メニューバーの設定
        self.menuBars.closeAction = lambda x=None: self.close()
        self.menuBars.saveAction = lambda x=None: self.SaveImage()
        self.menuBars.exportAction = lambda x=None: self.SaveImage(exportFlg=True)
        self.menuBars.toolbarAction = lambda x=None: self.toggleToolbar()
        
        self.menuBars.updateAction()

        self.setMenuBar(self.menuBars)

    def getEditImagePath(self)->str:
        for f in os.listdir("./img/edit"):
            if os.path.isfile(os.path.join("./img/edit", f)) and f != ".gitignore" and f != ".DS_Store":
                return os.path.join("./img/edit", f)
        return None

    def get_download_folder_path(self):
        # 一般的なOSでのダウンロードフォルダのパスを返す
        if os.name == 'nt':  # Windowsの場合
            return os.path.join(os.path.expanduser('~'), 'Downloads')
        else:  # macOSやLinuxの場合
            return os.path.expanduser('~/Downloads')

    def clearDrawing(self):
        self.drawingWidget.clearImage()

    def toggleToolbar(self):
        self.toolDock.setVisible(not self.toolDock.isVisible())

    def setStyleForButton(self, button:QPushButton, isSelected:bool):
        if isSelected:
            button.setStyleSheet("""
                QPushButton {
                    background-color:  #42A5F5;
                    border-radius: 5px;  /* 角を丸くする */
                    padding: 5px;        /* パディングを追加 */
                }
            """)
        else:
            button.setStyleSheet("")

    def changeTool(self, button):
        id = self.toolBar.toolButtonGroup.id(button)
        if id == 2:
            self.drawingWidget.setTool('pen')
            # ペン設定ウィンドウを表示
            dialog = PenSettingsDialog(self)
            if dialog.exec():
                self.drawingWidget.setPenStyle(dialog.styleComboBox.currentData())
                self.drawingWidget.setPenWidth(dialog.widthSpinBox.value())
                self.drawingWidget.setPenColor(dialog.color)
        elif id == 3:
            self.drawingWidget.setTool('eraser')
            # 消しゴム設定ウィンドウを表示
            dialog = EraserSettingsDialog(self)
            if dialog.exec():
                self.drawingWidget.setPenWidth(dialog.widthSpinBox.value())
        else:
            # どのツールも選択されていない
            self.drawingWidget.setTool('none')
            self.drawingWidget.setCurrentImage()
        
        # 選択されたボタンのスタイルを更新
        self.setStyleForButton(self.toolBar.penButton, button == self.toolBar.penButton)
        self.setStyleForButton(self.toolBar.eraserButton, button == self.toolBar.eraserButton)
        self.setStyleForButton(self.toolBar.noneButton, button == self.toolBar.noneButton)

    def changeScale(self, value):
        scaleFactor = value / 100.0  # スピンボックスの値をスケールファクタに変換
        self.drawingWidget.setScaleFactor(scaleFactor)

    def saveDrawing(self):
        imagePath = self.getEditImagePath()
        self.drawingWidget.saveImage(imagePath)

    def SaveImage(self,exportFlg=False):
        imagePath = self.getEditImagePath()
        self.saveDrawing()
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