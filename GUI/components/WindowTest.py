import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel
from PySide6.QtCore import Signal, Slot

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Main Window")
        self.setGeometry(100, 100, 400, 300)

        self.button = QPushButton("Open Second Window", self)
        self.button.clicked.connect(self.openSecondWindow)
        self.button.setGeometry(100, 100, 200, 50)

    def openSecondWindow(self):
        self.hide()  # Hide the main window
        self.secondWindow = SecondWindow()
        self.secondWindow.closed.connect(self.show)  # Connect to the closed signal
        self.secondWindow.show()

class SecondWindow(QMainWindow):
    closed = Signal()  # Signal to indicate the window is closed

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Second Window")
        self.setGeometry(600, 100, 400, 300)

        self.label = QLabel("This is the second window.", self)
        self.label.setGeometry(100, 100, 200, 50)

    def closeEvent(self, event):
        self.closed.emit()  # Emit the closed signal
        event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)

    mainWindow = MainWindow()
    mainWindow.show()

    sys.exit(app.exec())
