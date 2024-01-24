import sys
import os
from PySide6.QtWidgets import *
from PySide6.QtGui import QPainter, QPen, QColor
from PySide6.QtCore import Qt, QPoint

class DrawingWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.isDrawing = False
        self.lastPoint = QPoint()
        self.penColor = QColor('black')
        self.penWidth = 3
        self.lines = []
        self.isEraserMode = False
        self.penStyle = Qt.SolidLine  # デフォルトのペンスタイル

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.isDrawing = True
            self.lastPoint = event.position().toPoint()

    def mouseMoveEvent(self, event):
        if event.buttons() & Qt.LeftButton and self.isDrawing:
            lineColor = self.penColor if not self.isEraserMode else self.palette().color(self.backgroundRole())
            lineSegment = (self.lastPoint, event.position().toPoint(), lineColor, self.penWidth, self.penStyle)
            self.lines.append(lineSegment)
            self.lastPoint = event.position().toPoint()
            self.update()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.isDrawing = False

    def paintEvent(self, event):
        painter = QPainter(self)
        for line in self.lines:
            pen = QPen(line[2], line[3])
            pen.setStyle(line[4])  # ペンスタイルを設定
            painter.setPen(pen)
            painter.drawLine(line[0], line[1])

    def saveDrawing(self, filePath):
        pixmap = self.grab()
        pixmap.save(filePath, 'PNG')
    
    def setPenStyle(self, style):
        self.penStyle = style

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("お絵描きアプリ")
        self.resize(1000, 600)

        self.drawingWidget = DrawingWidget(self)
        self.setCentralWidget(self.drawingWidget)

        self.initUi()  # UIを初期化する
        self.updateStatusBar()  # ステータスバーを更新する

    def initUi(self):
        self.statusBarWidget = self.statusBar()
        self.statusLabel = QLabel()
        self.statusBarWidget.addPermanentWidget(self.statusLabel)

        self.buttonLayout = QVBoxLayout()
        self.buttonLayout.setSpacing(10)
        self.buttonLayout.setContentsMargins(10, 10, 10, 10)

        self.buttonLayout.addStretch() 

        self.colorButton = QPushButton("色を選択")
        self.colorButton.clicked.connect(self.chooseColor)
        self.buttonLayout.addWidget(self.colorButton)

        self.penWidthLabel = QLabel("ペンの太さ")
        self.buttonLayout.addWidget(self.penWidthLabel)

        self.penWidthSpinBox = QSpinBox()
        self.penWidthSpinBox.setRange(1, 50)
        self.penWidthSpinBox.setValue(self.drawingWidget.penWidth)
        self.penWidthSpinBox.valueChanged.connect(self.changePenWidth)
        self.buttonLayout.addWidget(self.penWidthSpinBox)


        self.penWidthLabel = QLabel("ペンのスタイル")
        self.buttonLayout.addWidget(self.penWidthLabel)
        self.penStyleComboBox = QComboBox()
        self.penStyleComboBox.addItem("Solid", Qt.SolidLine)
        self.penStyleComboBox.addItem("Dash", Qt.DashLine)
        self.penStyleComboBox.addItem("Dot", Qt.DotLine)
        self.penStyleComboBox.addItem("Dash Dot", Qt.DashDotLine)
        self.penStyleComboBox.addItem("Dash Dot Dot", Qt.DashDotDotLine)
        self.penStyleComboBox.currentIndexChanged.connect(self.changePenStyle)
        self.buttonLayout.addWidget(self.penStyleComboBox)

        self.toggleButton = QPushButton("ペン/消しゴム切り替え")
        self.toggleButton.clicked.connect(self.toggleEraser)
        self.buttonLayout.addWidget(self.toggleButton)

        

        self.saveButton = QPushButton("絵を保存")
        self.saveButton.clicked.connect(self.saveDrawing)
        self.buttonLayout.addWidget(self.saveButton)

        self.buttonLayout.addStretch() 

        self.buttonDockWidget = QDockWidget("ツールバー", self)
        self.buttonWidget = QWidget(self)
        self.buttonWidget.setLayout(self.buttonLayout)
        self.buttonDockWidget.setWidget(self.buttonWidget)

        self.addDockWidget(Qt.DockWidgetArea.LeftDockWidgetArea, self.buttonDockWidget)
        self.buttonDockWidget.setFloating(False)

        self.toolbarMenu = self.menuBar().addMenu("ツールバー")
        self.toolbarMenu.addAction("ツールバーを表示", self.toggleToolbar)

    def chooseColor(self):
        self.drawingWidget.isEraserMode = False
        color = QColorDialog.getColor()
        if color.isValid():
            self.drawingWidget.penColor = color
            self.updateStatusBar()

    def changePenWidth(self, width):
        self.drawingWidget.penWidth = width
        self.updateStatusBar()

    def changePenStyle(self, index):
        style = self.penStyleComboBox.itemData(index)
        self.drawingWidget.setPenStyle(style)
        self.updateStatusBar()

    def toggleEraser(self):
        self.drawingWidget.isEraserMode = not self.drawingWidget.isEraserMode
        self.updateStatusBar()

    def saveDrawing(self):
        defaultDir = "./img/saved"
        defaultPath = os.path.join(defaultDir, "untitled.png")
        if not os.path.exists(defaultDir):
            os.makedirs(defaultDir)
        filePath, _ = QFileDialog.getSaveFileName(self, "絵を保存", defaultPath, "PNG Files (*.png);;JPEG Files (*.jpg);;All Files (*)")
        if filePath:
            self.drawingWidget.saveDrawing(filePath)

    def updateStatusBar(self):
        color = self.drawingWidget.penColor
        width = self.drawingWidget.penWidth
        tool = "消しゴム" if self.drawingWidget.isEraserMode else "ペン"
         # ペンスタイルの名前を取得してステータスバーに表示
        penStyleName = self.penStyleComboBox.currentText()
        self.statusLabel.setText(f"{tool} - 色: <span style='color: {color.name()};'>{color.name()}</span>, 太さ: {width}, スタイル: {penStyleName}")
        self.statusLabel.setTextFormat(Qt.RichText)

    def toggleToolbar(self):
        self.buttonDockWidget.setVisible(not self.buttonDockWidget.isVisible())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec())
