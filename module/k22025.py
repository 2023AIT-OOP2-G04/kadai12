from ultralytics import YOLO
import cv2
import os
from postProcessing import PostProcessing


class k22025(PostProcessing):
    # これは必須
    def __init__(self):
        super().__init__()
        pass

    def resize_image(input_path):
        # 画像を読み込む
        image = cv2.imread(input_path)

        new_width = 800
        new_height = 600

        # リサイズ
        resized_image = cv2.resize(image, (new_width, new_height))

        # リサイズ後の画像を保存
        cv2.imwrite(image, resized_image)

        # ウィンドウに表示する場合
        # cv2.imshow("Resized Image", resized_image)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()

    def modelFunc(self):
        # 画像の読み込みは基本この関数を使う
        image = self.getEditImage()
        self.resize_image(image)

        # モデル読み込み
        model = YOLO("yolov8x-seg.pt")

        # 入力画像
        results = model(
            image,
            project=".img/tmp",
            save=True,
            show=True,
            save_crop=True,
        )
        # ウィンドウが閉じるのを待つ
        # デバッグ用
        # cv2.waitKey(0)
        cv2.destroyAllWindows()


if __name__ == "__main__":
    k22025 = k22025()
    k22025.modelFunc()
    # k22025.exportImage("sample.png")
