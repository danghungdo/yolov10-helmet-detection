from ultralytics import YOLOv10
import cv2


def load_model(model_path):
    return YOLOv10(model_path)


def detect_helmet(model, image):
    return model(image)[0]
