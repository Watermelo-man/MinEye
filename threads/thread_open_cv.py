from PyQt6.QtCore import QThread, pyqtSignal
from control import *
import sys
from control import cont


#Separate image processing stream from the camera
class ThreadOpenCV(QThread):
    changePixmap = pyqtSignal(QImage)


    def __init__(self):
        super().__init__()
        self.status = True


    def run(self):
        try:
            while self.status:
                ret, frame = tuple(cont.source.read())
                if ret:
                    self.changePixmap.emit(cont.analyseShot())
        except AttributeError as ex:
            print(ex)


    def stop(self):
        self.status = False
        cont.source.release()
        cv2.destroyAllWindows()
        self.quit()

    