import cv2
from grayscale import grayscale
result = grayscale('upload_image/neko.jpg')
cv2.imwrite('output_image/result.jpg', result)