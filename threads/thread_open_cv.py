from PyQt6.QtCore import QThread, pyqtSignal
import cv2
from control import *
import gc


#Separate image processing stream from the camera
class ThreadOpenCV(QThread):
    changePixmap = pyqtSignal(QImage)

    def __init__(self):
        super().__init__()
        self.status = True


    def run(self):
        self.cont = controller()
        self.cont.selectSource(2)

        while self.status:
            ret, frame = self.cont.source.read()

            if ret:
                self.changePixmap.emit(self.cont.analyseShot())
                if cv2.waitKey(0) == ord('q'):
                    break 
                gc.collect()

            self.msleep(1)      
            cv2.destroyAllWindows()

    