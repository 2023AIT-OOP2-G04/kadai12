# ここにトップページのコードを書く
import sys
from PySide6.QtWidgets import *
from PySide6 import QtGui,QtCore

from components.scroll import ScrollArea
from components.IshikawaLayoutTopPgae1 import LayoutTopPage

class TopPage(QWidget):
    def __init__(self):
        super().__init__()

        # ウィンドウの設定
        self.setWindowTitle("トップページ")
        self.resize(1600, 1200)
        
        self.scrollArea = ScrollArea(self)  # スクロールエリアを作成
        self.layout = QVBoxLayout(self) # レイアウトを作成
        self.layout.addWidget(self.scrollArea)  # レイアウトにスクロールエリアを追加
        self.layoutTopPage = LayoutTopPage(self)    # スクロールエリアに追加するウィジェットを作成
        self.scrollArea.addWidget(self.layoutTopPage)   # スクロールエリアにウィジェットを追加

if __name__ == '__main__':
    app = QApplication(sys.argv)
    topPage = TopPage()
    topPage.show()
    sys.exit(app.exec_())