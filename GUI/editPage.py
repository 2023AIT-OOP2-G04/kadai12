# ここに編集ページのコードを書く
import sys
from PySide6.QtWidgets import *
from PySide6 import QtGui,QtCore

class EditPage(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(1000,600)
        #ラベルで上（メニューバー）、右下（キャンバス）
        #メニューバー
        self.labelMenu = QLabel(self)
        self.labelStyle = """QLabel {
            background-color: #FFAA00;  /* 背景色 */
        }"""
        self.labelMenu.setText("メニューバーが入ります")
        # 見た目の設定をラベルに反映させる
        self.labelMenu.setStyleSheet(self.labelStyle)

        #ツールバー
        self.labelTool = QLabel(self)
        self.labelStyle = """QLabel {
            background-color: #FF0000;  /* 背景色 */
        }"""
        self.labelTool.setText("ツールバーが入ります")
        # 見た目の設定をラベルに反映させる
        self.labelTool.setStyleSheet(self.labelStyle)

        #キャンバス
        self.labelCanvas = QLabel(self)
        self.labelStyle = """QLabel {
            background-color: #FFFFFF;  /* 背景色 */
        }"""
        self.labelCanvas.setText("キャンバスが入ります")
        # 見た目の設定をラベルに反映させる
        self.labelCanvas.setStyleSheet(self.labelStyle)

        #メニューバーを垂直方向に並べる
        layoutQV = QVBoxLayout()
        layoutQV.addWidget(self.labelMenu)
        #ツールバーとキャンバスを水平方向に並べる
        layoutQH = QHBoxLayout()
        layoutQH.addWidget(self.labelTool,1)
        layoutQH.addWidget(self.labelCanvas,5)
        #レイアウト同士を組み合わせる
        parentLayout = QVBoxLayout()
        parentLayout.addLayout(layoutQV,1)
        parentLayout.addLayout(layoutQH,5)

        self.setLayout(parentLayout)  


if __name__ == '__main__':
    app = QApplication(sys.argv)
    editPage = EditPage()
    editPage.show()
    sys.exit(app.exec_())