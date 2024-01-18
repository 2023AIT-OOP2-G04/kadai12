from ultralytics import YOLO
import cv2

# モデル読み込み
model = YOLO("yolov8x-seg.pt")

# 入力画像
results = model(
    "./img.jpg",
    project="./edit",
    save=True,
    show=True,
    save_crop=True,
)
