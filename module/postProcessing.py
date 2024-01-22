import cv2
import numpy as np
import os
from abc import ABCMeta, abstractmethod


class PostProcessing(metaclass=ABCMeta):
    def __init__(self):
        self.editFolderPath = "./img/edit/"
        self.outputFolderPath = "./img/saved/"
        pass

    # editフォルダ内の画像を読み込む関数、継承すれば使えるようになります
    def getEditImage(self) -> cv2.Mat:
        for fileName in os.listdir(self.editFolderPath):
            if fileName == ".gitingore":
                continue
            filePath = self.editFolderPath + fileName
            img = cv2.imread(filePath)
        return img

    # editフォルダ内の画像をsavedフォルダへ保存する関数、継承すれば使えるようになります
    def exportImage(self, fileName: str) -> None:
        img = self.getEditImage()
        cv2.imwrite(self.outputFolderPath + fileName, img)
