from gui import *
from threads import ThreadOpenCV, ThreadOpenCVVideo
from PyQt6.QtGui import QPixmap
from control import cont


class Window(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)           

        #connections
        self.pushButton.clicked.connect(self.start)
        self.pushButton_2.clicked.connect(self.open)

        self.camera_on.clicked.connect(self.cam)
        self.camera_off.clicked.connect(self.stop_cam)


    #Open file function
    def open(self):
        try:
            cont.selectSource(1)
        except:
            error = QtWidgets.QMessageBox()
            error.setWindowTitle("Error")
            error.setText("File has not been selected.")
            error.setIcon(QtWidgets.QMessageBox.Icon.Warning)
            error.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok|QtWidgets.QMessageBox.StandardButton.Cancel)
            error.exec()


    #Start analysing function
    def start(self):
        try:
            if Path(str(cont.path)).suffix in ['.mp4', '.flv', '.ts', '.mts', '.avi']:
                self.thread_vid = ThreadOpenCVVideo()
                self.thread_vid.changePixmap.connect(self.setImage)
                self.thread_vid.start()
            else:
                self.im = cont.analyseShot()
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


    #Camera and thread start
    def cam(self):
        try:
            self.thread_cam = ThreadOpenCV()                                     
            self.thread_cam.changePixmap.connect(self.setImage)
            cont.selectSource(2)
            self.thread_cam.start()
            self.camera_off.setEnabled(True)
            self.camera_on.setEnabled(False)
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
            self.camera_off.setEnabled(False)
            self.camera_on.setEnabled(True)
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