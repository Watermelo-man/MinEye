
from PyQt6.QtCore import QThread, pyqtSignal
from PyQt6.QtGui import QImage
from control import cont


class ThreadOpenCVVideo(QThread):
    changePixmap = pyqtSignal(QImage)


    def __init__(self):
        super().__init__()
        self.status = True


    def run(self):
        try:
            while cont.source.isOpened():
                ret, frame = tuple(cont.source.read())
                if ret:
                    self.changePixmap.emit(cont.analyseShot())
        except AttributeError as ex:
            print(ex)
