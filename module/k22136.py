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

    def adjust_saturation_and_brightness(self, saturation_factor, brightness_factor):
        # 画像を開く
        image = self.getEditImage()
        
        # 彩度と明度を変更
        hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        hsv_image[:, :, 1] = np.clip(hsv_image[:, :, 1] * saturation_factor, 0, 255)
        hsv_image[:, :, 2] = np.clip(hsv_image[:, :, 2] * brightness_factor, 0, 255)

        # 色空間を戻す
        adjusted_image = cv2.cvtColor(hsv_image, cv2.COLOR_HSV2BGR)
        
        # 画像を保存
        self.saveImage(adjusted_image)

if __name__ == "__main__":

    pp = k22136()

    # ユーザーからの入力を受け取る  
    saturation_factor = float(input("彩度の変更倍率を入力してください (1.0 が変更なし): "))
    brightness_factor = float(input("明度の変更倍率を入力してください (1.0 が変更なし): "))

    # 関数を呼び出して画像の彩度と明度を変更
    pp.adjust_saturation_and_brightness(saturation_factor, brightness_factor)

