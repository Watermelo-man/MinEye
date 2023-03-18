
from PyQt6.QtCore import QThread, pyqtSignal, Qt
import cv2
from control import *


class ThreadOpenCVVideo(QThread):
    changePixmap = pyqtSignal(QImage)


    def __init__(self):
        super().__init__()
        self.status = True
        self.cont = contInstance


    def run(self):
        while self.status:
            #ret, frame = tuple(self.cont.source.read())

            #if ret:
            self.changePixmap.emit(self.cont.analyseShot())
            ''' self.cont.model.predict(self.cont.source)
            self.res = self.cont.model.showLastShot()
            #self.rgbImage = cv2.cvtColor(self.res, cv2.COLOR_BGR2RGB)
            h, w, ch = self.res.shape
            bytesPerLine = ch * w
            convertToQtFormat = QImage(self.res.data, w, h, bytesPerLine, QImage.Format.Format_RGB888)
            # p = convertToQtFormat.scaled(800, 600, Qt.AspectRatioMode.KeepAspectRatio)
            self.changePixmap.emit(convertToQtFormat)'''