import cv2
import numpy as np
import os
from abc import ABCMeta, abstractmethod


class PostProcessing(metaclass=ABCMeta):
    def __init__(self):
        self.editFolderPath = "./img/edit/"
        self.outputFolderPath = "./img/saved/"
        self.image_path = self.getFilePath()
        pass

    # ファイル取得関数、継承すれば使えるようになります  
    def getFilePath(self) -> str:
        for fileName in os.listdir(self.editFolderPath):
            if fileName == ".gitignore" or fileName == ".DS_Store":
                continue
            filePath = self.editFolderPath + fileName
            return filePath
    
    # editフォルダ内の画像を読み込む関数、継承すれば使えるようになります
    def getEditImage(self) -> cv2.Mat:
        img = cv2.imread(self.image_path)
        return img
    
    # 同じファイル名でeditフォルダ内の画像を上書き保存する関数、継承すれば使えるようになります
    def saveImage(self, img: cv2.Mat) -> None:
        cv2.imwrite(self.image_path, img)


    # editフォルダ内の画像をsavedフォルダへ保存する関数、継承すれば使えるようになります
    def exportImage(self,fileName: str) -> None:
        img=self.getEditImage()
        cv2.imwrite(self.outputFolderPath + fileName,img)