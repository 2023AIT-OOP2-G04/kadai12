import cv2
import os
from postProcessing import PostProcessing

# 学籍番号のクラスを作成してこんな感じで継承する
class K20114(PostProcessing):
#これは必須
    def __init__(self):
        super().__init__()
        pass

    def convertToGrayscaleAndSave(self):
        files = os.listdir(self.editFolderPath)

        for file_name in files:
            if file_name.endswith(('.jpg', '.jpeg', '.png')):
                input_path = os.path.join(self.editFolderPath, file_name)

                # 画像の読み込みは基本この関数を使う
                image = cv2.imread(input_path)

                # 画像を白黒に変換
                grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

                # 画像を上書き保存
                self.saveImage(grayscale_image)


# debug用
if __name__ == "__main__":
    k20114_instance = K20114()

    # 画像を白黒に変換して保存
    k20114_instance.convertToGrayscaleAndSave()

    print("画像を白黒に変換して保存しました。")
