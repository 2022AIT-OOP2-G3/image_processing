from abc import ABC, abstractmethod
import cv2


class ImageProcess(ABC):
    # 画像を処理して返す
    @abstractmethod
    def process(self, img_path: str) -> cv2.Mat:
        pass

    # output_image内に作るディレクトリ名を返す
    @abstractmethod
    def get_name(self) -> str:
        pass
