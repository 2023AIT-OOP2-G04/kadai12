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
        self.MotoImage = None
        pass

    def lavelObject(self):
        image = self.getEditImage()
        self.MotoImage = image.copy()
        gray_img = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
        bin_img = cv2.threshold(gray_img, 180, 255, cv2.THRESH_BINARY_INV)[1]

        retval, labels, stats, centroids = cv2.connectedComponentsWithStats(bin_img)

        n = retval - 1
        for i in range(n):
            i += 1
            left_top = (stats[i][0], stats[i][1])
            right_bottom = (
                stats[i][0] + stats[i][2],
                stats[i][1] + stats[i][3],
            )
            statsImg = cv2.rectangle(image, left_top, right_bottom, (0, 0, 255), 1)
            statsImg = cv2.putText(
                statsImg,
                str(i),
                left_top,
                cv2.FONT_HERSHEY_PLAIN,
                1,
                (0, 0, 255),
                1,
            )
        self.saveImage(statsImg)

    def eraseOBjects(self, num):
        grayImg = cv2.cvtColor(self.MotoImage, cv2.COLOR_RGB2GRAY)
        binImg = cv2.threshold(grayImg, 180, 255, cv2.THRESH_BINARY_INV)[1]

        retval, labels, stats, centroids = cv2.connectedComponentsWithStats(binImg)
        if num > retval - 1 or num < 1:
            print("error")
            self.saveImage(self.MotoImage)
            return
        removeImg = self.MotoImage.copy()
        for i in range(stats[num][0], stats[num][0] + stats[num][2]):
            for j in range(stats[num][1], stats[num][1] + stats[num][3]):
                removeImg[j][i] = 0

        self.saveImage(removeImg)


# debug用
if __name__ == "__main__":
    x22037 = x22037()
    x22037.lavelObject()

    # 好きな番号を入力する
    print("削除したいラベルの番号を入力してください")
    num = int(input())
    x22037.eraseOBjects(num)
    # x22037.exportImage("sample.png")
