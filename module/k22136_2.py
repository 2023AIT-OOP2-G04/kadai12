import cv2
import numpy as np
import os
from postProcessing import PostProcessing

# 学籍番号のクラスを作成してこんな感じで継承する
class k22136_2(PostProcessing):
    # これは必須
    def __init__(self):
        super().__init__()
        pass

    def resize_image(self, vertical_ratio, horizontal_ratio):
        # 画像を開く
        image = self.getEditImage()

        # 元の画像の縦横比を計算
        original_height, original_width, _ = image.shape
        original_aspect_ratio = original_width / original_height

        # ターゲットの縦横比に合わせて新しいサイズを計算
        if original_aspect_ratio > (horizontal_ratio / vertical_ratio):
            new_width = int(original_height * (horizontal_ratio / vertical_ratio))
            new_height = original_height
        else:
            new_width = original_width
            new_height = int(original_width / (horizontal_ratio / vertical_ratio))


        # 画像をリサイズ
        resized_image = cv2.resize(image, (new_width, new_height))

        # リサイズされた画像を保存
        self.saveImage(resized_image)

    
# debug用
if __name__ == "__main__":

    pp = k22136_2()

    # ユーザーによって指定された縦横比を取得
    vertical_ratio = int(input("縦の比率を入力してください: "))
    horizontal_ratio = int(input("横の比率を入力してください: "))

    # 画像を指定された縦横比にリサイズ
    pp.resize_image(vertical_ratio, horizontal_ratio) 