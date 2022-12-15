import cv2
from filter.img_processes import ImageProcess


class FaceRect(ImageProcess):
    def process(self, img_path: str) -> cv2.Mat:
        img = cv2.imread(img_path)
        face_cascade = cv2.CascadeClassifier(
            './filter_data/haarcascade_frontalface_default.xml'
        )
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)
        for (x, y, w, h) in faces:
            cv2.rectangle(
                img,
                (x, y),
                (x + w, y + h),
                (255, 0, 0),
                2
            )
        return img

    def get_name(self) -> str:
        return "face_rect"
