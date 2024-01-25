import cv2
import numpy as np
import os
from postProcessing import PostProcessing

# 学籍番号のクラスを作成してこんな感じで継承する
class k22136(PostProcessing):
    # これは必須
    def __init__(self):
        super().__init__()
        pass

    def adjust_saturation_and_brightness(self, input_path, output_path, saturation_factor, brightness_factor):
        # 画像を開く
        original_image = cv2.imread(input_path)

        # 彩度と明度を変更
        hsv_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2HSV)
        hsv_image[:, :, 1] = np.clip(hsv_image[:, :, 1] * saturation_factor, 0, 255)
        hsv_image[:, :, 2] = np.clip(hsv_image[:, :, 2] * brightness_factor, 0, 255)

        # 色空間を戻す
        adjusted_image = cv2.cvtColor(hsv_image, cv2.COLOR_HSV2BGR)
        
        # 画像を保存
        self.save_img(hsv_image)

    # 同じファイル名でeditフォルダ内の画像を上書き保存する関数、継承すれば使えるようになります
    def saveImage(self, img: cv2.Mat) -> None:
        cv2.imwrite(self.image_path, img)

if __name__ == "__main__":

    pp = k22136()

    # ユーザーからの入力を受け取る  
    image_path = "img/edit/iro_input.jpg"
    output_path = "img/edit/iro_input.jpg"
    saturation_factor = float(input("彩度の変更倍率を入力してください (1.0 が変更なし): "))
    brightness_factor = float(input("明度の変更倍率を入力してください (1.0 が変更なし): "))

    # 関数を呼び出して画像の彩度と明度を変更
    pp.adjust_saturation_and_brightness(image_path, output_path, saturation_factor, brightness_factor)

