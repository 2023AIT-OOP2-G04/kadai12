from PySide6.QtWidgets import QWidget, QApplication, QLabel
from PySide6.QtCore import Qt, QRect, QPoint
from PySide6.QtGui import QPainter, QPen, QPixmap
import sys

class ImageWidget(QWidget):
    def __init__(self, image_path, parent=None):
        super().__init__(parent)
        self.pixmap = QPixmap(image_path)
        self.drag_start = None
        self.drag_end = None

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drag_start = event.pos()
            self.drag_end = None
            self.update()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton and self.drag_start is not None:
            self.drag_end = event.pos()
            self.update()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            if self.drag_start is not None and self.drag_end is not None:
                print(f"Dragged from {self.drag_start} to {self.drag_end}")
                self.drag_start = None
                self.drag_end = None
                self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawPixmap(self.rect(), self.pixmap)

        if self.drag_start is not None and self.drag_end is not None:
            rect = QRect(self.drag_start, self.drag_end)
            painter.setPen(QPen(Qt.red, 2, Qt.SolidLine))
            painter.drawRect(rect)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    image_path = "./img/edit/aaa.jpg"  # 画像のパスに置き換えてください
    widget = ImageWidget(image_path)
    widget.show()
    sys.exit(app.exec())
