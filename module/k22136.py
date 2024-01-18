import cv2
import numpy as np
import os
from postProcessing import PostProcessing
from PIL import Image, ImageEnhance

def adjust_saturation_and_brightness(image_path, saturation_factor, brightness_factor, output_path):
    # 画像を開く
    img = Image.open(image_path)

    # 彩度を変更
    enhancer = ImageEnhance.Color(img)
    img = enhancer.enhance(saturation_factor)

    # 明度を変更
    enhancer = ImageEnhance.Brightness(img)
    img = enhancer.enhance(brightness_factor)

    # 画像を保存
    img.save(output_path)

    save_img


# 処理したい画像をedit.pngとして保存し,望む場合はsavedに名前を入力して保存する
    def save_img(src_img):
        cv2.imwrite("img/edit/edit.png", src_img)
        print("保存したい場合は1を入力してください")
        flag = int(input())
        if flag == 1:
            print("保存するファイル名を入力してください")
            name = input()
            cv2.imwrite("img/saved/" + name + ".png", src_img)

if __name__ == "__main__":
    # ユーザーからの入力を受け取る  
    image_path = "img/edit/iro_input.jpg"
    output_path = "img/edit/iro_input.jpg"
    saturation_factor = float(input("彩度の変更倍率を入力してください (1.0 が変更なし): "))
    brightness_factor = float(input("明度の変更倍率を入力してください (1.0 が変更なし): "))

    # 関数を呼び出して画像の彩度と明度を変更
    adjust_saturation_and_brightness(image_path, saturation_factor, brightness_factor, output_path)

