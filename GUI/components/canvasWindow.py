import sys
import os
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QColorDialog, QDockWidget
from PySide6.QtGui import QPainter, QPen, QColor
from PySide6.QtCore import Qt, QPoint

class DrawingWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.drawing = False
        self.last_point = QPoint()
        self.pen_color = QColor('black')
        self.pen_width = 3
        self.lines = []

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drawing = True
            self.last_point = event.position().toPoint()

    def mouseMoveEvent(self, event):
        if event.buttons() & Qt.LeftButton and self.drawing:
            line_segment = (self.last_point, event.position().toPoint(), self.pen_color, self.pen_width)
            self.lines.append(line_segment)
            self.last_point = event.position().toPoint()
            self.update()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drawing = False

    def paintEvent(self, event):
        painter = QPainter(self)
        for line in self.lines:
            pen = QPen(line[2], line[3], Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin)
            painter.setPen(pen)
            painter.drawLine(line[0], line[1])

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.drawing_widget = DrawingWidget()
        self.setCentralWidget(self.drawing_widget)
import sys
import os
from PySide6.QtWidgets import (QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QColorDialog, QDockWidget, QLabel, QSpinBox, QFileDialog)
from PySide6.QtGui import QPainter, QPen, QColor
from PySide6.QtCore import Qt, QPoint

class DrawingWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.drawing = False
        self.last_point = QPoint()
        self.pen_color = QColor('black')
        self.pen_width = 3
        self.lines = []
        self.eraser_mode = False

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drawing = True
            self.last_point = event.position().toPoint()

    def mouseMoveEvent(self, event):
        if event.buttons() & Qt.LeftButton and self.drawing:
            line_color = self.pen_color if not self.eraser_mode else self.palette().color(self.backgroundRole())
            line_segment = (self.last_point, event.position().toPoint(), line_color, self.pen_width)
            self.lines.append(line_segment)
            self.last_point = event.position().toPoint()
            self.update()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drawing = False

    def paintEvent(self, event):
        painter = QPainter(self)
        for line in self.lines:
            pen = QPen(line[2], line[3], Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin)
            painter.setPen(pen)
            painter.drawLine(line[0], line[1])

    def save_drawing(self, file_path):
        pixmap = self.grab()
        pixmap.save(file_path, 'PNG')

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("お絵描きアプリ")
        self.resize(1000, 600)

        self.drawing_widget = DrawingWidget(self)
        self.setCentralWidget(self.drawing_widget)

        self.initUI()

    def initUI(self):
        self.status_bar = self.statusBar()
        self.status_label = QLabel()
        self.status_bar.addPermanentWidget(self.status_label)
        self.update_status_bar()

        self.button_layout = QVBoxLayout()
        self.button_layout.setSpacing(10)
        self.button_layout.setContentsMargins(10, 10, 10, 10)
        self.button_layout.addStretch() 

        self.color_button = QPushButton("色を選択")
        self.color_button.clicked.connect(self.choose_color)
        self.button_layout.addWidget(self.color_button)

        

        self.pen_width_label = QLabel("ペンの太さ")
        self.button_layout.addWidget(self.pen_width_label)

        self.pen_width_spinbox = QSpinBox()
        self.pen_width_spinbox.setRange(1, 50)
        self.pen_width_spinbox.setValue(self.drawing_widget.pen_width)
        self.pen_width_spinbox.valueChanged.connect(self.change_pen_width)
        self.button_layout.addWidget(self.pen_width_spinbox)

        

        self.toggle_button = QPushButton("ペン/消しゴム切り替え")
        self.toggle_button.clicked.connect(self.toggle_eraser)
        self.button_layout.addWidget(self.toggle_button)

        self.save_button = QPushButton("絵を保存")
        self.save_button.clicked.connect(self.save_drawing)
        self.button_layout.addWidget(self.save_button)

        self.button_dock_widget = QDockWidget("ツールバー", self)

        self.button_layout.addStretch() 

        self.button_widget = QWidget(self)
        self.button_widget.setLayout(self.button_layout)
        self.button_dock_widget.setWidget(self.button_widget)


        self.addDockWidget(Qt.RightDockWidgetArea, self.button_dock_widget)
        self.button_dock_widget.setFloating(False)

        self.toolbar_menu = self.menuBar().addMenu("ツールバー")
        self.toolbar_menu.addAction("ツールバーを表示", self.toggle_toolbar)

    def choose_color(self):
        self.drawing_widget.eraser_mode = False
        color = QColorDialog.getColor()
        if color.isValid():
            self.drawing_widget.pen_color = color
            self.update_status_bar()

    def change_pen_width(self, width):
        self.drawing_widget.pen_width = width
        self.update_status_bar()

    def toggle_eraser(self):
        self.drawing_widget.eraser_mode = not self.drawing_widget.eraser_mode
        self.update_status_bar()

    def save_drawing(self):
        default_dir = "./img/saved"
        default_path = os.path.join(default_dir, "untitled.png")
        if not os.path.exists(default_dir):
            os.makedirs(default_dir)
        file_path, _ = QFileDialog.getSaveFileName(self, "絵を保存", default_path, "PNG Files (*.png);;JPEG Files (*.jpg);;All Files (*)")
        if file_path:
            self.drawing_widget.save_drawing(file_path)

    def update_status_bar(self):
        color = self.drawing_widget.pen_color
        width = self.drawing_widget.pen_width
        tool = "消しゴム" if self.drawing_widget.eraser_mode else "ペン"
        self.status_label.setText(f"{tool} - 色: <span style='color: {color.name()};'>{color.name()}</span>, 太さ: {width}")
        self.status_label.setTextFormat(Qt.RichText)

    def toggle_toolbar(self):
        self.button_dock_widget.setVisible(not self.button_dock_widget.isVisible())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())
