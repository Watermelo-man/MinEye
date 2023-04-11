from PyQt6.QtCore import QThread, pyqtSignal
from PyQt6.QtGui import QImage
from control import cont
import cv2


#Separate image processing stream from the camera
class ThreadOpenCV(QThread):
    changePixmap = pyqtSignal(QImage)


    def __init__(self):
        super().__init__()
        self.status = True
        #self.run()

    def run(self):
        try:
            while self.status:
                self.changePixmap.emit(cont.analyseShot())
                #print('hiiiiii')
        except AttributeError as ex:
            print(ex)


    def stop(self):
        self.status = False
        cont.source.release()
        cv2.destroyAllWindows()
        self.quit()
