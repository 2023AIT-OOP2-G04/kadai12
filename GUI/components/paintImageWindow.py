import sys
import os
from PySide6.QtWidgets import *
from PySide6.QtGui import QPainter, QPen, QColor, QPixmap
from PySide6.QtCore import Qt, QPoint,QRect,QSize

class DrawingWidget(QWidget):
    def __init__(self,imagePath=None, parent=None):
        super().__init__(parent)


        self.isDrawing = False
        self.lastPoint = QPoint()
        self.penColor = QColor('black')
        self.penWidth = 3
        self.lines = []
        self.isEraserMode = False
        self.penStyle = Qt.SolidLine  # デフォルトのペンスタイル
        self.tool = 'none' # 現在選択されているツール（'pen', 'eraser', None）
        self.scaleFactor = 1.0  # 拡大・縮小率の初期値
        self.imagePath = imagePath

        # 範囲選択用の変数
        self.currentImage = None    # 現在の画像のお絵描き状態を保持
        self.dragStartPos:QPoint = None    # 範囲選択の開始位置
        self.dragEndPos:QPoint = None      # 範囲選択の終了位置
        self.isSelectionConfirmed = False  # 範囲選択が確定したかどうかのフラグ
        # 座標を保持する変数
        self.startX = 0
        self.startY = 0
        self.endX = 0
        self.endY = 0
        


        if imagePath:
            self.openImage(imagePath)
            self.setCurrentImage()
            self.setMinimumSize(self.image.size())  # イメージのサイズに基づいて最小サイズを設定
        else:
            # デフォルトの名前
            self.imagePath = "./img/edit/untitled.png"
            self.originalImage = QPixmap(800, 600)  # デフォルトの画像サイズ
            self.originalImage.fill(Qt.white)
            self.image = QPixmap(self.originalImage)
            self.image.save(self.imagePath, 'PNG')
            self.setCurrentImage()
            self.setMinimumSize(800, 600)  # ウィジェットの最小サイズを設定

    def setCurrentImage(self):
        self.currentImage = self.image.copy()

    def setTool(self, tool):
        self.tool = tool

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            # print("press")
            self.isDrawing = True
            # self.lastPoint = event.position().toPoint()
            # マウスイベントの位置をスケーリング
            self.lastPoint = event.position().toPoint() / self.scaleFactor
            if self.tool=='none':
                # 初期化
                self.image = QPixmap(self.currentImage)
                self.dragStartPos = self.lastPoint
                self.dragEndPos = None
                self.update()
                # print(self.dragStartPos)
                


    def mouseMoveEvent(self, event):
        if event.buttons() & Qt.LeftButton and self.isDrawing:
            newPoint = event.position().toPoint() / self.scaleFactor
            if self.tool in ['pen', 'eraser']:
                painter = QPainter(self.image)
                if self.tool == 'eraser':
                    # 消しゴムモードの描画
                    eraserRect = QRect(self.lastPoint, QSize(self.penWidth, self.penWidth))
                    painter.drawPixmap(eraserRect, self.originalImage, eraserRect)
                else:
                    # ペンモードの描画
                    pen = QPen(self.penColor, self.penWidth, self.penStyle)
                    painter.setPen(pen)
                    painter.drawLine(self.lastPoint, newPoint)
                self.lastPoint = newPoint
            elif self.tool == 'none':
                # 範囲選択のみの場合
                self.dragEndPos = newPoint
            self.update()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.isDrawing = False
            if self.tool == 'none' and self.dragStartPos and self.dragEndPos:
                # self.dragStartPos = None
                # self.dragEndPos = None
                self.isSelectionConfirmed = True  # 範囲選択を確定
                self.update()
                # 範囲選択の座標を取得
                self.startX=min(self.dragStartPos.x(), self.dragEndPos.x())
                self.startY=min(self.dragStartPos.y(), self.dragEndPos.y())
                self.endX=max(self.dragStartPos.x(), self.dragEndPos.x())
                self.endY=max(self.dragStartPos.y(), self.dragEndPos.y())
                # 画像のサイズに合わせて座標を補正
                imageWidth = self.image.width()
                imageHeight = self.image.height()
                self.startX = max(0, min(self.startX, imageWidth))
                self.startY = max(0, min(self.startY, imageHeight))
                self.endX = max(0, min(self.endX, imageWidth))
                self.endY = max(0, min(self.endY, imageHeight))


                # print(f"選択範囲: 開始位置({self.startX}, {self.startY}), 終了位置({self.endX}, {self.endY})")

    def paintEvent(self, event):
        painter = QPainter(self)
        scaledImage = self.image.scaled(self.image.size() * self.scaleFactor, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        painter.drawPixmap(QPoint(), scaledImage)
        if self.isSelectionConfirmed and self.dragStartPos and self.dragEndPos:
            # 確定された範囲選択に赤い枠を描画
            scaledDragStartPos = self.dragStartPos * self.scaleFactor
            scaledDragEndPos = self.dragEndPos * self.scaleFactor
            rect = QRect(scaledDragStartPos, scaledDragEndPos)
            painter.setPen(QPen(QColor('red'), 2, Qt.SolidLine))
            painter.drawRect(rect)

        # 範囲選択の描画
        if self.tool == 'none' and self.dragStartPos and self.dragEndPos:
            scaledDragStartPos = self.dragStartPos * self.scaleFactor
            scaledDragEndPos = self.dragEndPos * self.scaleFactor
            rect = QRect(scaledDragStartPos, scaledDragEndPos)
            painter.setPen(QPen(QColor('red'), 2, Qt.SolidLine))
            painter.drawRect(rect)
        else:
            painter.drawPixmap(QPoint(), scaledImage)

    def saveDrawing(self, filePath):
        pixmap = self.grab()
        pixmap.save(filePath, 'PNG')
    
    def setPenColor(self, color:QColor):
        self.penColor = color

    def setPenWidth(self, width):
        self.penWidth = width

    def setPenStyle(self, style):
        self.penStyle = style
    
    def openImage(self, imagePath):
        self.originalImage = QPixmap(imagePath)  # 元の画像を保持
        self.image = QPixmap(self.originalImage)  # 描画用のコピー
        if not self.image.isNull():
            self.resize(self.image.size())  # ウィジェットのサイズを画像のサイズに更新
            self.update()  # ウィジェットを再描画

    def saveImage(self, imagePath):
        self.image.save(imagePath)

    def clearImage(self):
        # 画像を初期状態に戻す
        self.image = QPixmap(self.originalImage)
        self.update()

    def setScaleFactor(self, scale):
        self.scaleFactor = scale
        self.update()  # ウィジェットを再描画

class PenSettingsDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("ペン設定")
        self.setFixedSize(400, 400)  # ウィンドウサイズを設定

        layout = QVBoxLayout(self)

        # デフォルトの色を設定
        self.color = QColor('black')
        
        # スタイル設定の水平レイアウト
        styleLayout = QHBoxLayout()
        styleLayout.addWidget(QLabel("線の種類:"))
        self.styleComboBox = QComboBox()
        self.styleComboBox.addItem("Solid", Qt.SolidLine)
        self.styleComboBox.addItem("Dash", Qt.DashLine)
        self.styleComboBox.addItem("Dot", Qt.DotLine)
        self.styleComboBox.addItem("Dash Dot", Qt.DashDotLine)
        self.styleComboBox.addItem("Dash Dot Dot", Qt.DashDotDotLine)
        styleLayout.addWidget(self.styleComboBox)
        layout.addLayout(styleLayout)  # 水平レイアウトを垂直レイアウトに追加

        # 太さ設定の水平レイアウト
        widthLayout = QHBoxLayout()
        widthLayout.addWidget(QLabel("太さ:"))
        self.widthSpinBox = QSpinBox()
        self.widthSpinBox.setRange(1, 50)
        widthLayout.addWidget(self.widthSpinBox)
        layout.addLayout(widthLayout)  # 水平レイアウトを垂直レイアウトに追加

        # カラー設定
        self.colorButton = QPushButton("色を選択")
        self.colorButton.clicked.connect(self.chooseColor)
        layout.addWidget(self.colorButton)

        # 決定ボタンを追加
        self.okButton = QPushButton("決定")
        self.okButton.clicked.connect(self.accept)
        layout.addWidget(self.okButton)

    def chooseColor(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.color = color

class EraserSettingsDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("消しゴム設定")
        self.setFixedSize(400, 200)  # ウィンドウサイズを設定

        layout = QVBoxLayout(self)

       # 太さ設定の水平レイアウト
        widthLayout = QHBoxLayout()
        widthLayout.addWidget(QLabel("太さ:"))
        self.widthSpinBox = QSpinBox()
        self.widthSpinBox.setRange(1, 99)
        widthLayout.addWidget(self.widthSpinBox)
        layout.addLayout(widthLayout)  # 水平レイアウトを垂直レイアウトに追加
        
        # 決定ボタンを追加
        self.okButton = QPushButton("決定")
        self.okButton.clicked.connect(self.accept)
        layout.addWidget(self.okButton)

class ObjectDetectionDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("マスク対象の設定")
        self.setFixedSize(400, 200)  # ウィンドウサイズを設定

        layout = QVBoxLayout(self)

       # 太さ設定の水平レイアウト
        objectDetectionLayout = QHBoxLayout()
        objectDetectionLayout.addWidget(QLabel("ラベルの番号:"))
        self.objectDetectionSpinBox = QSpinBox()
        self.objectDetectionSpinBox.setRange(0, 300)
        objectDetectionLayout.addWidget(self.objectDetectionSpinBox)
        layout.addLayout(objectDetectionLayout)  # 水平レイアウトを垂直レイアウトに追加
        
        # 決定ボタンを追加
        self.okButton = QPushButton("決定")
        self.okButton.clicked.connect(self.accept)
        layout.addWidget(self.okButton)

class ImageResizeDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("縦横比の設定")
        self.setFixedSize(400, 200)  # ウィンドウサイズを設定

        layout = QVBoxLayout(self)

       # 太さ設定の水平レイアウト
        ResizeLayout = QHBoxLayout()
        ResizeLayout.addWidget(QLabel("縦に対する横の比率(%):"))
        self.ResizeSpinBox = QSpinBox()
        self.ResizeSpinBox.setRange(0, 1000)
        ResizeLayout.addWidget(self.ResizeSpinBox)
        layout.addLayout(ResizeLayout)  # 水平レイアウトを垂直レイアウトに追加
        
        # 決定ボタンを追加
        self.okButton = QPushButton("決定")
        self.okButton.clicked.connect(self.accept)
        layout.addWidget(self.okButton)

class ImageColorDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("画像色設定")
        self.setFixedSize(400, 400)  # ウィンドウサイズを設定

        layout = QVBoxLayout(self)

       # 彩度設定の水平レイアウト
        saidoLayout = QHBoxLayout()
        saidoLayout.addWidget(QLabel("彩度(%):"))
        self.saidoSpinBox = QSpinBox()
        self.saidoSpinBox.setRange(0, 200)
        saidoLayout.addWidget(self.saidoSpinBox)
        layout.addLayout(saidoLayout)  # 水平レイアウトを垂直レイアウトに追加
        # 明度設定の水平レイアウト
        meidoLayout = QHBoxLayout()
        meidoLayout.addWidget(QLabel("明度(%):"))
        self.meidoSpinBox = QSpinBox()
        self.meidoSpinBox.setRange(0, 200)
        meidoLayout.addWidget(self.meidoSpinBox)
        layout.addLayout(meidoLayout)  # 水平レイアウトを垂直レイアウトに追加
        
        # 決定ボタンを追加
        self.okButton = QPushButton("決定")
        self.okButton.clicked.connect(self.accept)
        layout.addWidget(self.okButton)

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("お絵描きアプリ")
        self.resize(1000, 600)

        

        

        self.drawingWidget = DrawingWidget(imagePath="./img/edit/aaa.jpg",parent=self)
        self.scrollArea = QScrollArea()  # スクロールエリアを作成
        self.scrollArea.setWidget(self.drawingWidget)  # DrawingWidgetをスクロールエリアに設定
        self.scrollArea.setWidgetResizable(True)  # スクロールエリアのサイズ変更を可能にする
        self.setCentralWidget(self.scrollArea)  # スクロールエリアをメインウィンドウの中央のウィジェットとして設定

        self.initUi()  # UIを初期化する

        self.openImageButton = QPushButton("画像を開く")
        self.openImageButton.clicked.connect(self.openImage)
        self.buttonLayout.addWidget(self.openImageButton)

        self.saveImageButton = QPushButton("画像を保存")
        self.saveImageButton.clicked.connect(self.saveImage)
        self.buttonLayout.addWidget(self.saveImageButton)

        self.clearButton = QPushButton("全消去")
        self.clearButton.clicked.connect(self.clearDrawing)
        self.buttonLayout.addWidget(self.clearButton)

    def initUi(self):
        self.statusBarWidget = self.statusBar()
        self.statusLabel = QLabel()
        self.statusBarWidget.addPermanentWidget(self.statusLabel)

        self.buttonLayout = QVBoxLayout()
        self.buttonLayout.setSpacing(10)
        self.buttonLayout.setContentsMargins(10, 10, 10, 10)

        self.buttonLayout.addStretch() 

        # ペンと消しゴムの選択のためのボタン
        # ボタングループの設定
        self.toolButtonGroup = QButtonGroup(self)
        self.noneButton = QPushButton("選択ツール")
        self.penButton = QPushButton("ペン")
        self.eraserButton = QPushButton("消しゴム")
        self.noneButton.setChecked(True)

        toolLayout = QVBoxLayout()  # QVBoxLayoutを使用
        toolLayout.addWidget(self.noneButton)
        toolLayout.addWidget(self.penButton)
        toolLayout.addWidget(self.eraserButton)

        self.buttonLayout.addLayout(toolLayout)
        
        self.toolButtonGroup.addButton(self.noneButton, 1)
        self.toolButtonGroup.addButton(self.penButton, 2)
        self.toolButtonGroup.addButton(self.eraserButton, 3)
        self.toolButtonGroup.buttonClicked.connect(self.changeTool)
        # ボタンのスタイルを設定するためのメソッド
        self.setStyleForButton(self.penButton, False)
        self.setStyleForButton(self.eraserButton, False)
        self.setStyleForButton(self.noneButton, True)

        

        self.saveButton = QPushButton("絵を保存")
        self.saveButton.clicked.connect(self.saveDrawing)
        self.buttonLayout.addWidget(self.saveButton)

        self.buttonLayout.addStretch() 

        # 拡大・縮小のスライダーまたはスピンボックスの設定
        self.scaleSpinBox = QSpinBox()
        self.scaleSpinBox.setRange(10, 400)  # 10% から 400% の範囲
        self.scaleSpinBox.setValue(100)  # 初期値は 100%
        self.scaleSpinBox.valueChanged.connect(self.changeScale)
        self.buttonLayout.addWidget(QLabel("スケール:"))
        self.buttonLayout.addWidget(self.scaleSpinBox)

        self.buttonDockWidget = QDockWidget("ツールバー", self)
        self.buttonWidget = QWidget(self)
        self.buttonWidget.setLayout(self.buttonLayout)
        self.buttonDockWidget.setWidget(self.buttonWidget)

        self.addDockWidget(Qt.DockWidgetArea.LeftDockWidgetArea, self.buttonDockWidget)
        self.buttonDockWidget.setFloating(False)

        self.toolbarMenu = self.menuBar().addMenu("ツールバー")
        self.toolbarMenu.addAction("ツールバーを表示", self.toggleToolbar)

    def saveDrawing(self):
        defaultDir = "./img/saved"
        defaultPath = os.path.join(defaultDir, "untitled.png")
        if not os.path.exists(defaultDir):
            os.makedirs(defaultDir)
        filePath, _ = QFileDialog.getSaveFileName(self, "絵を保存", defaultPath, "PNG Files (*.png);;JPEG Files (*.jpg);;All Files (*)")
        if filePath:
            self.drawingWidget.saveDrawing(filePath)

    def clearDrawing(self):
        self.drawingWidget.clearImage()

    def toggleToolbar(self):
        self.buttonDockWidget.setVisible(not self.buttonDockWidget.isVisible())

    def openImage(self):
        imagePath, _ = QFileDialog.getOpenFileName(self, "Open Image", "", "Image Files (*.png *.jpg *.bmp)")
        if imagePath:
            self.drawingWidget.openImage(imagePath)

    def saveImage(self):
        imagePath, _ = QFileDialog.getSaveFileName(self, "Save Image", "", "PNG Files (*.png);;JPEG Files (*.jpg);;All Files (*)")
        if imagePath:
            self.drawingWidget.saveImage(imagePath)

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
        id = self.toolButtonGroup.id(button)
        # 範囲選択の座標を初期化
        self.startX = 0
        self.startY = 0
        self.endX = 0
        self.endY = 0
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
        self.setStyleForButton(self.penButton, button == self.penButton)
        self.setStyleForButton(self.eraserButton, button == self.eraserButton)
        self.setStyleForButton(self.noneButton, button == self.noneButton)

    def changeScale(self, value):
        scaleFactor = value / 100.0  # スピンボックスの値をスケールファクタに変換
        self.drawingWidget.setScaleFactor(scaleFactor)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec())
