from gui import *
from threads import ThreadOpenCV, ThreadOpenCVVideo
import time
import os

class Window(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)           

        #connections
<<<<<<< Updated upstream
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
        
=======
        self.StartButton.clicked.connect(self.start)
        self.SelectFileButton.clicked.connect(self.open)
        self.SelectModelBox.currentTextChanged.connect(self.changeModel)
        self.camera_on.clicked.connect(self.cam)
        self.camera_off.clicked.connect(self.stop_cam)

    def changeModel(self):
        path = str(os.path.dirname(os.path.abspath(__file__)))
        path = os.path.join(path,'ourmodels')
        path = os.path.join(path,self.SelectModelBox.currentText())
        #print(self.SelectModelBox.currentText)
        cont.changeModelPath(path)




>>>>>>> Stashed changes

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
<<<<<<< Updated upstream
            if Path(str(self.cont.path)).suffix in ['.mp4', '.flv', '.ts', '.mts', '.avi']:
                self.thread_vid.cont = self.cont
                self.thread_vid.start()
=======
            if Path(str(cont.path)).suffix in ['.mp4', '.flv', '.ts', '.mts', '.avi']:
                if cont.source is not None:
                    self.StartButton.clicked.disconnect(self.start)
                    self.StartButton.setText("STOP")
                    self.thread_vid = ThreadOpenCVVideo()
                    self.thread_vid.changePixmap.connect(self.setImage)
                    self.thread_vid.start()
                    self.StartButton.clicked.connect(self.stop_video)
                    self.pause.setEnabled(True)
                    self.pause.clicked.connect(self.pause_video)
                else:
                    raise AttributeError
>>>>>>> Stashed changes
            else:
                self.im = self.cont.analyseShot()
                self.display.setPixmap(QPixmap.fromImage(self.im).scaled(800, 600))
                self.display.show()
<<<<<<< Updated upstream
=======
        except:
            error = QtWidgets.QMessageBox()
            error.setWindowTitle("Error")
            error.setText("You can use only images or videos.")
            error.setIcon(QtWidgets.QMessageBox.Icon.Warning)
            error.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok|QtWidgets.QMessageBox.StandardButton.Cancel)
            error.exec()


    #Stop video
    def stop_video(self):
        try:
            self.thread_vid.stop()
            self.thread_vid.changePixmap.disconnect(self.setImage)
            del self.thread_vid
            cont.source = None
            self.StartButton.clicked.disconnect(self.stop_video)
            self.StartButton.clicked.connect(self.start)
            self.StartButton.setText("START")
            self.pause.setEnabled(False)
>>>>>>> Stashed changes
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
<<<<<<< Updated upstream
=======
            self.camera_off.setEnabled(True)
            self.camera_on.setEnabled(False)
            self.StartButton.setEnabled(False)
>>>>>>> Stashed changes
        except:
            error = QtWidgets.QMessageBox()
            error.setWindowTitle("Error")
            error.setText("Can't connect to the camera")
            error.setIcon(QtWidgets.QMessageBox.Icon.Warning)
            error.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok|QtWidgets.QMessageBox.StandardButton.Cancel)
<<<<<<< Updated upstream
            error.exec()                                     
=======
            error.exec()


    #Camera and thread stop
    def stop_cam(self):
        try:
            self.thread_cam.stop()
            self.thread_cam.changePixmap.disconnect(self.setImage)
            del self.thread_cam
            cont.source = None
            self.camera_off.setEnabled(False)
            self.camera_on.setEnabled(True)
            self.StartButton.setEnabled(True)
        except AttributeError as ex:
            print(ex)
            error = QtWidgets.QMessageBox()
            error.setWindowTitle("Error")
            error.setText("Something wrong")
            error.setIcon(QtWidgets.QMessageBox.Icon.Warning)
            error.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok|QtWidgets.QMessageBox.StandardButton.Cancel)
            error.exec()    
>>>>>>> Stashed changes


    #Show camera's picture
    def setImage(self, image):                                            
        self.display.setPixmap(QPixmap.fromImage(image).scaled(800, 600))


    #Switch camera off
    def kill_thread(self):
        self.thread_cam.stop()