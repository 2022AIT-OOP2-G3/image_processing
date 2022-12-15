import numpy as np
import cv2
from filter.img_processes import ImageProcess

class GrayScale(ImageProcess):
    def process(self, img_path: str) -> cv2.Mat:
        img = cv2.imread(img_path)
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img2 = cv2.imread(img_path, 0)
        ret, img_thresh = cv2.threshold(img2, 125, 255, cv2.THRESH_BINARY)
        return img_thresh

    def get_name(self) -> str:
        return "grayscale"
    