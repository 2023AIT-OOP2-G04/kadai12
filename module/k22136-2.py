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

    def resize_image(self,input_path, output_path, target_aspect_ratio):
        # 画像を開く
        original_image = cv2.imread(input_path)

        # 元の画像の縦横比を計算
        original_height, original_width, _ = original_image.shape
        original_aspect_ratio = original_width / original_height

        # ターゲットの縦横比に合わせて新しいサイズを計算xs
        if original_aspect_ratio > target_aspect_ratio:
            new_width = int(original_height * target_aspect_ratio)
            new_height = original_height
        else:
            new_width = original_width
            new_height = int(original_width / target_aspect_ratio)

        # 画像をリサイズ
        resized_image = cv2.resize(original_image, (new_width, new_height))

        # リサイズされた画像を保存
        self.save_img(resized_image)

    # 処理したい画像をedit.pngとして保存し,望む場合はsavedに名前を入力して保存する
    def save_img(self,src_img):
        cv2.imwrite("img/edit/edit.png", src_img)
        print("保存したい場合は1を入力してください")
        flag = int(input())
        if flag == 1:
            print("保存するファイル名を入力してください")
            name = input()
            cv2.imwrite("img/saved/" + name + ".png", src_img)
    
# debug用
if __name__ == "__main__":

    pp = k22136()

    # ユーザーによって指定された縦横比を取得
    user_aspect_ratio = float(input("縦横比を入力してください（例: 1.77）: "))

    # 例: 入力画像のパスと出力画像のパス
    image_path = "img/edit/tateyoko_input.jpg"
    output_path = "img/edit/tateyoko_input.jpg"

    # 画像を指定された縦横比にリサイズ
    pp.resize_image(image_path, output_path, user_aspect_ratio) 