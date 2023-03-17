
from PyQt6.QtCore import QThread, pyqtSignal
import cv2
from control import *
from PyQt6.QtCore import Qt


class ThreadOpenCVVideo(QThread):
    changePixmap = pyqtSignal(QImage)


    def __init__(self):
        super().__init__()
        self.status = True
        self.cont = controller()


    def run(self):
        while self.status:
            ret, frame = self.cont.source.read()

            if ret:
                #self.changePixmap.emit(self.cont.analyseShot())
                rgbImage = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                h, w, ch = rgbImage.shape
                bytesPerLine = ch * w
                convertToQtFormat = QImage(rgbImage.data, w, h, bytesPerLine, QImage.Format.Format_RGB888)
                p = convertToQtFormat.scaled(800, 600, Qt.AspectRatioMode.KeepAspectRatio)
                self.changePixmap.emit(p)

            self.msleep(20)      
            cv2.destroyAllWindows()