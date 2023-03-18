from gui import *
from threads import ThreadOpenCV, ThreadOpenCVVideo
import time
import os

class Window(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)           

        #connections
        self.pushButton.clicked.connect(self.start)
        self.pushButton_2.clicked.connect(self.open)
        self.camera_on.clicked.connect(self.can)
        self.camera_off.clicked.connect(self.kill_thread)
        self.thread_cam = ThreadOpenCV()                                        
        self.thread_cam.changePixmap.connect(self.setImage)
        self.thread_vid = ThreadOpenCVVideo()
        self.thread_vid.changePixmap.connect(self.setImage)
       # self.comboBox.currentText

        self.comboBox.currentIndexChanged.connect(lambda : \
                                                  createContInstance(os.path.join(path, self.comboBox.currentText())))
        

    #Open file function
    def open(self):
        try:
            self.cont = contInstance
            self.cont.selectSource(1)
        except:
            print("File didn't chosen")


    #Start analysing function
    def start(self):
        try:
            if Path(str(self.cont.path)).suffix in ['.mp4', '.flv', '.ts', '.mts', '.avi']:
                self.thread_vid.cont = self.cont
                self.thread_vid.start()
            else:
                self.im = self.cont.analyseShot()
                self.display.setPixmap(QPixmap.fromImage(self.im).scaled(800, 600))
                self.display.show()
        except AttributeError as ex:
            print(ex)
            error = QtWidgets.QMessageBox()
            error.setWindowTitle("Error")
            error.setText("You can use only PIL Image or cv2 ndarray")
            error.setIcon(QtWidgets.QMessageBox.Icon.Warning)
            error.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok|QtWidgets.QMessageBox.StandardButton.Cancel)
            error.exec()             


    #Threading start
    def can(self):
        try:
            self.thread_cam.start()
        except:
            error = QtWidgets.QMessageBox()
            error.setWindowTitle("Error")
            error.setText("Can't connect to the camera")
            error.setIcon(QtWidgets.QMessageBox.Icon.Warning)
            error.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok|QtWidgets.QMessageBox.StandardButton.Cancel)
            error.exec()                                     


    #Show camera's picture
    def setImage(self, image):                                            
        self.display.setPixmap(QPixmap.fromImage(image).scaled(800, 600))


    #Switch camera off
    def kill_thread(self):
        self.thread_cam.stop()