# import sys
# from PySide6.QtWidgets import (
#     QApplication,
#     QMainWindow,
#     QPushButton,
#     QLabel,
#     QFileDialog,
# )
# from PySide6.QtGui import QPixmap


# class ImageApp(QMainWindow):
#     def __init__(self):
#         super().__init__()

#         self.resize(1000, 1000)
#         # 画像を表示するためのラベル
#         self.image_label = QLabel(self)
#         self.image_label.setGeometry(10, 10, 600, 400)

#         # 画像をアップロードするためのボタン
#         self.upload_button = QPushButton("画像を選択", self)
#         self.upload_button.setGeometry(10, 420, 200, 30)
#         self.upload_button.clicked.connect(self.upload_image)

#         # 画像を保存するためのボタン
#         self.save_button = QPushButton("画像を保存", self)
#         self.save_button.setGeometry(220, 420, 200, 30)
#         self.save_button.clicked.connect(self.save_image)

#         # 現在の画像のパス
#         self.current_image_path = None

#     def upload_image(self):
#         (filename,) = QFileDialog.getOpenFileName(
#             self, "画像を選択", "", "Image Files (.png .jpg .bmp)"
#         )
#         if filename:
#             self.current_image_path = filename
#             pixmap = QPixmap(filename)
#             self.image_label.setPixmap(
#                 pixmap.scaled(self.image_label.width(), self.image_label.height())
#             )

#     def save_image(self):
#         if self.current_image_path:
#             for current_image_path in self.current_image_paths:
#                 (savepath,) = QFileDialog.getSaveFileName(
#                     self, "画像を保存", "", "Image Files (.png .jpg .bmp)"
#                 )
#                 if savepath:
#                     pixmap = QPixmap(self.current_image_path)
#                     pixmap.save(savepath)


# # ここからやること
# # 画像を選択を押してから、フォルダ内の画像を選択できるようにする


# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     windowManager = ImageApp()
#     windowManager.show()
#     sys.exit(app.exec_())

import sys
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton,
    QLabel,
    QFileDialog,
)
from PySide6.QtGui import QPixmap


class ImageApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.resize(1000, 1000)
        # 画像を表示するためのラベル
        self.image_label = QLabel(self)
        self.image_label.setGeometry(10, 10, 600, 400)

        # 画像をアップロードするためのボタン
        self.upload_button = QPushButton("画像を選択", self)
        self.upload_button.setGeometry(10, 420, 200, 30)
        self.upload_button.clicked.connect(self.upload_image)

        # 画像を保存するためのボタン
        self.save_button = QPushButton("画像を保存", self)
        self.save_button.setGeometry(220, 420, 200, 30)
        self.save_button.clicked.connect(self.save_image)

        # 現在の画像のパス
        self.current_image_paths = []

    def upload_image(self):
        (filenames,) = QFileDialog.getOpenFileNames(
            self, "画像を選択", "", "Image Files (*.png *.jpg *.bmp)"
        )
        if filenames:
            self.current_image_paths = filenames
            pixmap = QPixmap(self.current_image_paths[0])
            self.image_label.setPixmap(
                pixmap.scaled(self.image_label.width(), self.image_label.height())
            )

    def save_image(self):
        for current_image_path in self.current_image_paths:
            (savepath,) = QFileDialog.getSaveFileName(
                self, "画像を保存", "", "Image Files (*.png *.jpg *.bmp)"
            )
            if savepath:
                pixmap = QPixmap(current_image_path)
                pixmap.save(savepath)


# ここからやること
# 画像を選択を押してから、フォルダ内の画像を選択できるようにする


if __name__ == "__main__":
    app = QApplication(sys.argv)
    windowManager = ImageApp()
    windowManager.show()
    sys.exit(app.exec_())
