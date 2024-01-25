import cv2
import os
from postProcessing import PostProcessing

# 学籍番号のクラスを作成してこんな感じで継承する
class K20114(PostProcessing):
#これは必須
    def __init__(self):
        super().__init__()
        pass

    def grayScale(self):
        # 画像の読み込みは基本この関数を使う
        image = self.getEditImage()

        # グレースケール化
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # 画像の保存
        self.saveImage(gray_image)

        print("グレースケール化が完了しました.")

        

    def trim_and_save(self, top_left, bottom_right):


        # 画像の読み込みは基本この関数を使う
        image = self.getEditImage()

        # ファイル名の取得
        input_file = os.path.basename(self.image_path)

        # トリミング
        trimmed_image = image[top_left[1]:bottom_right[1], top_left[0]:bottom_right[0]]

        # トリミング結果が空でないか確認
        if not trimmed_image.size:
            print("トリミングした結果が空です。")
            return

        # トリミング結果を元の画像に上書き保存
        self.saveImage(trimmed_image)
        print("トリミングが完了しました.")

       
# debug用
if __name__ == "__main__":
    k20114_instance = K20114()

    # トリミング領域の座標の入力を受け取る
    top_left_x = int(input("左上のx座標を入力してください: "))
    top_left_y = int(input("左上のy座標を入力してください: "))
    bottom_right_x = int(input("右下のx座標を入力してください: "))
    bottom_right_y = int(input("右下のy座標を入力してください: "))

    # トリミングと保存を実行
    k20114_instance.trim_and_save((top_left_x, top_left_y), (bottom_right_x, bottom_right_y))

