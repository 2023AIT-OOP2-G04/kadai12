import cv2
import numpy as np
import os
from postProcessing import PostProcessing

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

