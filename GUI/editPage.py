# ここに編集ページのコードを書く
import sys
from PySide6.QtWidgets import *
from PySide6 import QtGui,QtCore
from PySide6.QtCore import Qt
from components.toolBar import ToolBar
from components.imageWindow import ImageWindow
from components.scroll import ScrollArea

class EditPage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(1000,600)

        # 上部のメッセージエリア
        messageArea = QLabel("上部のメッセージエリア")
        messageArea.setStyleSheet("background-color: lightgray;")
        messageArea.setAlignment(Qt.AlignCenter)

        #ツールバー
        self.toolDock = QDockWidget("tool",self)
        self.toolBar = QWidget()
        ToolBar(self.toolBar)
        self.toolDock.setWidget(self.toolBar)
        self.addDockWidget(Qt.LeftDockWidgetArea, self.toolDock)

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
        


if __name__ == '__main__':
    app = QApplication(sys.argv)
    editPage = EditPage()
    editPage.show()
    sys.exit(app.exec_())