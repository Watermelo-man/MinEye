from PyQt6.QtCore import QThread, pyqtSignal
from PyQt6.QtGui import QImage
from control import cont
import cv2


class ThreadOpenCVVideo(QThread):
    changePixmap = pyqtSignal(QImage)
    flag = False

    def __init__(self):
        super().__init__()
        self.status = True
        self.recordStatus = 0

        #self.run()

    def run(self):
        try:
            while self.status:
                if self.recordStatus == 0:
                    self.changePixmap.emit(cont.analyseShot())
                    
                # if self.recordStatus == 1 and self.flag == False:
                #     cont.selectType(1)
                #     self.flag = True
        except AttributeError as ex:
            print(ex)

    def stop(self):
        self.status = False
        cont.source.release()
        cv2.destroyAllWindows()
        self.quit()