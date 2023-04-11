from gui import *
from threads import ThreadOpenCV, ThreadOpenCVVideo
import time
import os

class Window(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)           

        #connections
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





    #Open file function
    def open(self):
        try:
            cont.selectSource(1)
        except:
            error = QtWidgets.QMessageBox()
            error.setWindowTitle("Error")
            error.setText("You can use only images or videos.")
            error.setIcon(QtWidgets.QMessageBox.Icon.Warning)
            error.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok|QtWidgets.QMessageBox.StandardButton.Cancel)
            error.exec()


    #Start analysing function
    def start(self):
        try:
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
            else:
                self.im = cont.analyseShot()
                self.display.setPixmap(QPixmap.fromImage(self.im).scaled(800, 600))
                self.display.show()
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
        except AttributeError as ex:
            print(ex)


    #Pause video
    def pause_video(self):
        try:
            self.thread_vid.recordStatus = 1
            self.pause.clicked.disconnect(self.pause_video)
            self.pause.setText("CONTINUE")
            self.pause.clicked.connect(self.continue_video)
        except:
            error = QtWidgets.QMessageBox()
            error.setWindowTitle("Error")
            error.setText("Something wrong")
            error.setIcon(QtWidgets.QMessageBox.Icon.Warning)
            error.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok|QtWidgets.QMessageBox.StandardButton.Cancel)
            error.exec()


    #Continue video
    def continue_video(self):
        try:
            self.thread_vid.recordStatus = 0
            self.pause.clicked.disconnect(self.continue_video)
            self.pause.setText("PAUSE")
            self.pause.clicked.connect(self.pause_video)
        except:
            error = QtWidgets.QMessageBox()
            error.setWindowTitle("Error")
            error.setText("Something wrong")
            error.setIcon(QtWidgets.QMessageBox.Icon.Warning)
            error.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok|QtWidgets.QMessageBox.StandardButton.Cancel)
            error.exec()


    #Camera and thread start
    def cam(self):
        try:
            self.thread_cam = ThreadOpenCV()                                     
            self.thread_cam.changePixmap.connect(self.setImage)
            cont.selectSource(2)
            self.thread_cam.start()
            self.camera_off.setEnabled(True)
            self.camera_on.setEnabled(False)
            #self.pushButton.setEnabled(False)
        except:
            error = QtWidgets.QMessageBox()
            error.setWindowTitle("Error")
            error.setText("Can't connect to the camera")
            error.setIcon(QtWidgets.QMessageBox.Icon.Warning)
            error.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok|QtWidgets.QMessageBox.StandardButton.Cancel)
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
            #self.pushButton.setEnabled(True)
        except AttributeError as ex:
            print(ex)
            error = QtWidgets.QMessageBox()
            error.setWindowTitle("Error")
            error.setText("Something wrong")
            error.setIcon(QtWidgets.QMessageBox.Icon.Warning)
            error.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok|QtWidgets.QMessageBox.StandardButton.Cancel)
            error.exec()    


    #Show camera's picture
    def setImage(self, image):                                            
        self.display.setPixmap(QPixmap.fromImage(image).scaled(800, 600))
