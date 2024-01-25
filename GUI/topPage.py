# ここにトップページのコードを書く
import sys
from PySide6.QtWidgets import *
from PySide6 import QtGui,QtCore

from components.scroll import ScrollArea
from components.IshikawaLayoutTopPgae1 import TopPage

class TopPage(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent=parent)
        
        self.scrollArea = ScrollArea(self)  # スクロールエリアを作成
        self.layout = QVBoxLayout(self) # レイアウトを作成
        self.layout.addWidget(self.scrollArea)  # レイアウトにスクロールエリアを追加
          # スクロールエリアに追加するウィジェットを作成
        self.scrollArea.addWidget(TopPage(self)) # スクロールエリアにウィジェットを追加

if __name__ == '__main__':
    app = QApplication(sys.argv)
    topPage = TopPage()
    topPage.show()
    sys.exit(app.exec_())