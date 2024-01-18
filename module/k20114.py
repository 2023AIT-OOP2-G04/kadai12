import cv2
import numpy as np
import os
from abc import ABCMeta, abstractmethod

class PostProcessing(metaclass=ABCMeta):

    def __init__(self):
        project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.editFolderPath = os.path.join(project_root, "img", "edit") ##jpeg→editに
        self.outputFolderPath = os.path.join(project_root, "img", "saved")##jpeg→savedに

        os.makedirs(self.editFolderPath, exist_ok=True)
        os.makedirs(self.outputFolderPath, exist_ok=True)

    def getEditImage(self) -> np.ndarray:
        for fileName in os.listdir(self.editFolderPath):
            if fileName.endswith(('.png', '.jpg', '.jpeg', '.gif')):
                filePath = os.path.join(self.editFolderPath, fileName)
                img = cv2.imread(filePath, cv2.IMREAD_GRAYSCALE)  # グレースケールで読み込む
                return img

    def exportImage(self, fileName: str, processed_img: np.ndarray) -> None:
        cv2.imwrite(os.path.join(self.outputFolderPath, fileName), processed_img)

class K20114(PostProcessing):

    def __init__(self):
        super().__init__()

    def processImage(self, outputFileName: str) -> None:
        img = self.getEditImage()
        if img is not None:
            # 保存
            self.exportImage(outputFileName, img)

if __name__ == "__main__":
    k20114_instance = K20114()
    k20114_instance.processImage("output_image.jpg")

