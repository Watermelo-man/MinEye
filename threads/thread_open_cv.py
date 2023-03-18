from PyQt6.QtCore import QThread, pyqtSignal
from control import *


#Separate image processing stream from the camera
class ThreadOpenCV(QThread):
    changePixmap = pyqtSignal(QImage)
    __slots__ = 'status', "cont",

    def __init__(self):
        super().__init__()
        self.status = True


    def run(self):
        #self.cont = controller()
        self.cont = contInstance
        self.cont.selectSource(2)

        while self.status:
            #ret, frame = tuple(self.cont.source.read())
            #if ret:
            self.changePixmap.emit(self.cont.analyseShot())


    def stop(self):
        print("Finishing camera's image analysing...")
        self.cont.source.release()
        cv2.destroyAllWindows()
        self.status = False
        #self.quit()

    