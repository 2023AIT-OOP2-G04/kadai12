import sys
import os
from PySide6.QtWidgets import QApplication
from GUI.topPage import TopPage

app = QApplication(sys.argv)
topPage = TopPage()
topPage.show()
sys.exit(app.exec_())