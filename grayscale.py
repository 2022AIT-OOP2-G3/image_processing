import numpy as np
import cv2
def grayscale(upload_image):
    img = cv2.imread(upload_image)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img2 = cv2.imread(upload_image, 0)
    ret, img_thresh = cv2.threshold(img2, 125, 255, cv2.THRESH_BINARY)
    return img_thresh
    # cv2.imwrite('./output_image', img_gray)
    # cv2.imwrite('./output_image', img_thresh)