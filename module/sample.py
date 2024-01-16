import cv2
import numpy as np
import os
from postProcessing import PostProcessing

# 学籍番号のクラスを作成してこんな感じで継承する
class k20000(PostProcessing):
    # これは必須
    def __init__(self):
        super().__init__()
        pass

    def sampleFunc(self):
        # 画像の読み込みは基本この関数を使う
        image=self.getEditImage()
        
        cv2.imshow("sample",image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


# debug用
if __name__ == "__main__":
    k20000=k20000()
    k20000.sampleFunc()
    k20000.exportImage("sample.png")

    
