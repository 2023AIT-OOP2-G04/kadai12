# 各画像処理関数が書いてあるファイルのクラスをインポート
from sample import k20000 as Sample
from k20114 import K20114 as K20114
# from k22025 import K22025 as K22025
from k22136 import k22136 as K22136
from k22136_2 import k22136_2 as k22136_2
from x22037 import x22037 as X22037


class PPManager:
    def __init__(self):
        # ここで各クラスをインスタンス化する
        self.sample = Sample()
        self.k20114 = K20114()
        # self.k22025 = K22025()
        self.k22136 = K22136()
        self.k22136_2 = k22136_2()
        self.x22037 = X22037()
        pass


# debug用
if __name__ == "__main__":
    # 使用例
    ppManager = PPManager()
    ppManager.sample.sampleFunc()
    ppManager.sample.exportImage("sample.png")
    ppManager.k20114.trim_and_save((0, 0), (100, 100))
    ppManager.k22136.adjust_saturation_and_brightness(1.0, 1.0)
    ppManager.k22136_2.resize_image(1.77)
    ppManager.x22037.lavelObject()
    ppManager.x22037.eraseOBjects(1)
