import sys
import cv2
import numpy as np
import os
import random
from postProcessing import PostProcessing


class x22037(PostProcessing):
    # これは必須
    def __init__(self):
        super().__init__()
        pass

    # 処理したい画像をedit.pngとして保存し,望む場合はsavedに名前を入力して保存する
    def save_img(self, src_img, image):
        cv2.imwrite("img/edit/edit.png", src_img)
        print("保存したい場合は1を入力してください")
        flag = int(input())
        if flag == 1:
            for fileName in os.listdir(self.editFolderPath):
                if fileName == ".gitignore":
                    continue
                self.exportImage(fileName)
            print("保存しました")

    def eraseOBjects(self):
        # 画像の読み込みは基本この関数を使う
        image = self.getEditImage()

        gray_img = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
        bin_img = cv2.threshold(gray_img, 180, 255, cv2.THRESH_BINARY_INV)[1]

        retval, labels, stats, centroids = cv2.connectedComponentsWithStats(bin_img)
        # 好きな番号を入力する
        print("削除したいラベルの番号を入力してください")
        num = int(input())

        remove_img = image.copy()
        for i in range(stats[num][0], stats[num][0] + stats[num][2]):
            for j in range(stats[num][1], stats[num][1] + stats[num][3]):
                remove_img[j][i] = 0

        self.save_img(remove_img, image)
        cv2.imshow("remove.png", remove_img)
        cv2.waitKey(0)


# debug用
if __name__ == "__main__":
    x22037 = x22037()
    x22037.eraseOBjects()
    # x22037.exportImage("sample.png")
