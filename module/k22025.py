from ultralytics import YOLO
import cv2
import os
from postProcessing import PostProcessing


class k22025(PostProcessing):
    # これは必須
    def __init__(self):
        super().__init__()
        pass

    def modelFunc(self):
        # 画像の読み込みは基本この関数を使う
        image = self.getEditImage()

        # モデル読み込み
        model = YOLO("yolov8x-seg.pt")

        # 入力画像
        results = model(
            image,
            project="/Users/k22025kk/work/oop2/lecture13/kadai12/img/edit",
            save=True,
            show=True,
            save_crop=True,
        )
        # ウィンドウが閉じるのを待つ
        cv2.waitKey(0)
        cv2.destroyAllWindows()


if __name__ == "__main__":
    k22025 = k22025()
    k22025.modelFunc()
    # k22025.exportImage("sample.png")
