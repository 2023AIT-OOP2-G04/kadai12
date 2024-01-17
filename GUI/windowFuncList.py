# ここに編集ページのコードを書く
import sys
from PySide6.QtWidgets import *
from PySide6 import QtGui,QtCore

class WindowFuncList(QWidget):

    def __init__(self):
        pass

    # イベントリスナー用の関数を定義
    def sayHello(self):
        print("Hello! from WindowFuncList")

if __name__ == '__main__':
    wfl=WindowFuncList()
    wfl.sayHello()