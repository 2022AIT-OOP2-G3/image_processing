import cv2
from filter.img_processes import ImageProcess

class mozaiku(ImageProcess):
    def process(self, img_path: str) -> cv2.Mat:
        img=cv2.imread(img_path)
        face_cascade = cv2.CascadeClassifier("./filter_data/haarcascade_frontalface_default.xml")
        src_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
        faces = face_cascade.detectMultiScale(src_gray)
        
        ratio = 0.05
        
        for x, y, w, h in faces:
            small = cv2.resize(img[y: y + h, x: x + w], None, fx=ratio, fy=ratio, interpolation=cv2.INTER_NEAREST)
            img[y: y + h, x: x + w] = cv2.resize(small, (w, h), interpolation=cv2.INTER_NEAREST)
            
        return img
    

    def get_name(self) -> str:
        return "mozaiku"