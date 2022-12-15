from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler
import time

from filter.face_rect import FaceRect
import cv2


class EventHandler(LoggingEventHandler):
    def on_created(self, event):
        # ここに画像処理を行うクラスを追加する
        img_processes = [
            FaceRect(),
        ]

        output_path = "./output_image"
        for img_process in img_processes:
            img = img_process.process(
                event.src_path,
            )
            cv2.imwrite(
                output_path + "/" + img_process.get_name() + "/" +
                event.src_path.split("/")[-1],
                img
            )


def main():
    path = "./upload_image"
    event_handler = EventHandler()
    observer = Observer()
    observer.schedule(
        event_handler,
        path,
        recursive=True
    )
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()


if __name__ == "__main__":
    main()
