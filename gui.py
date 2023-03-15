import os
import cv2
import time
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import QThread, pyqtSignal
from control import *


path = r'C:\Users\Acer\Desktop\orereco\orereco\ourmodels' # Path to folder with models


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 720)
        MainWindow.setStyleSheet("background-color: rgb(91, 91, 91);")


        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")


        #Image display 
        self.display = QtWidgets.QLabel(parent=self.centralwidget)
        self.display.setGeometry(QtCore.QRect(20, 20, 800, 600))
        self.display.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.display.setObjectName("display")


        #Start button
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(720, 630, 100, 60))
        font = QtGui.QFont()
        font.setFamily("HelveticaNowDisplay Bold")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(126, 126, 126);\n"
                                      "selection-background-color: rgb(0, 0, 0);\n"
                                      "gridline-color: rgb(0, 0, 0);")
        self.pushButton.setObjectName("pushButton")


        #Panel with model and file
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 630, 680, 60))
        font = QtGui.QFont()
        font.setFamily("HelveticaNowDisplay Bold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("border-color: rgb(0, 0, 0);")
        self.label.setFrameShape(QtWidgets.QFrame.Shape.Panel)
        self.label.setLineWidth(1)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label.setObjectName("label")


        #Select model panel
        self.comboBox = QtWidgets.QComboBox(parent=self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(150, 650, 400, 20))
        self.comboBox.setStyleSheet("background-color: rgb(134, 134, 134);")
        self.comboBox.setObjectName("comboBox")
        for pt_file in os.listdir(path):
            if pt_file.endswith(".pt"):
                self.comboBox.addItem(pt_file)


        #Select file button
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(580, 650, 80, 25))
        font = QtGui.QFont()
        font.setFamily("HelveticaNowDisplay Bold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(126, 126, 126);\n"
                                        "selection-background-color: rgb(0, 0, 0);\n"
                                        "gridline-color: rgb(0, 0, 0);")
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)


        #Contrast label
        self.contrast_big_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.contrast_big_label.setGeometry(QtCore.QRect(830, 20, 431, 601))
        font = QtGui.QFont()
        font.setFamily("HelveticaNowDisplay Bold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.contrast_big_label.setFont(font)
        self.contrast_big_label.setStyleSheet("gridline-color: rgb(0, 0, 0);")
        self.contrast_big_label.setFrameShape(QtWidgets.QFrame.Shape.Panel)
        self.contrast_big_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignTop)
        self.contrast_big_label.setObjectName("contrast_big_label")


        #Sharpness label
        self.sharpness_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.sharpness_label.setEnabled(True)
        self.sharpness_label.setGeometry(QtCore.QRect(835, 110, 111, 25))
        font = QtGui.QFont()
        font.setFamily("HelveticaNowDisplay Bold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.sharpness_label.setFont(font)
        self.sharpness_label.setAutoFillBackground(False)
        self.sharpness_label.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.sharpness_label.setLineWidth(1)
        self.sharpness_label.setObjectName("sharpness_label")


        #Accuracy label
        self.accuracy_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.accuracy_label.setEnabled(True)
        self.accuracy_label.setGeometry(QtCore.QRect(835, 200, 90, 21))
        font = QtGui.QFont()
        font.setFamily("HelveticaNowDisplay Bold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(90)
        self.accuracy_label.setFont(font)
        self.accuracy_label.setAutoFillBackground(False)
        self.accuracy_label.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.accuracy_label.setLineWidth(1)
        self.accuracy_label.setObjectName("accuracy_label")


        #Contrast slider
        self.contrast_slider = QtWidgets.QSlider(parent=self.centralwidget)
        self.contrast_slider.setGeometry(QtCore.QRect(840, 50, 411, 41))
        self.contrast_slider.setStyleSheet("background-color: rgb(105, 105, 105);")
        self.contrast_slider.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.contrast_slider.setObjectName("contrast_slider")


        #Sharpness slider
        self.sharpness_slider = QtWidgets.QSlider(parent=self.centralwidget)
        self.sharpness_slider.setGeometry(QtCore.QRect(840, 140, 411, 41))
        self.sharpness_slider.setStyleSheet("background-color: rgb(105, 105, 105);")
        self.sharpness_slider.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.sharpness_slider.setObjectName("sharpness_slider")


        #Accuracy slider
        self.accuracy_slider = QtWidgets.QSlider(parent=self.centralwidget)
        self.accuracy_slider.setGeometry(QtCore.QRect(840, 230, 411, 41))
        self.accuracy_slider.setStyleSheet("background-color: rgb(105, 105, 105);")
        self.accuracy_slider.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.accuracy_slider.setObjectName("accuracy_slider")
        MainWindow.setCentralWidget(self.centralwidget)


        #Calculate scale view button
        self.calc_scale_view_btn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.calc_scale_view_btn.setGeometry(QtCore.QRect(840, 300, 411, 41))
        font = QtGui.QFont()
        font.setFamily("HelveticaNowDisplay Bold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.calc_scale_view_btn.setFont(font)
        self.calc_scale_view_btn.setStyleSheet("background-color: rgb(126, 126, 126);\n"
                                               "selection-background-color: rgb(0, 0, 0);\n"
                                               "gridline-color: rgb(0, 0, 0);")
        self.calc_scale_view_btn.setObjectName("calc_scale_view_btn")


        #Calculate object size
        self.calc_obj_size_btn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.calc_obj_size_btn.setGeometry(QtCore.QRect(840, 350, 411, 41))
        font = QtGui.QFont()
        font.setFamily("HelveticaNowDisplay Bold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.calc_obj_size_btn.setFont(font)
        self.calc_obj_size_btn.setStyleSheet("background-color: rgb(126, 126, 126);\n"
                                             "selection-background-color: rgb(0, 0, 0);\n"
                                             "gridline-color: rgb(0, 0, 0);")
        self.calc_obj_size_btn.setObjectName("calc_obj_size_btn")


        #Turn on camera
        self.camera_on = QtWidgets.QPushButton(parent=self.centralwidget)
        self.camera_on.setGeometry(QtCore.QRect(840, 570, 200, 41))
        font = QtGui.QFont()
        font.setFamily("HelveticaNowDisplay Bold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.camera_on.setFont(font)
        self.camera_on.setStyleSheet("background-color: rgb(126, 126, 126);\n"
                                      "selection-background-color: rgb(0, 0, 0);\n"
                                      "gridline-color: rgb(0, 0, 0);")
        self.camera_on.setObjectName("camera_on")


        self.camera_off = QtWidgets.QPushButton(parent=self.centralwidget)
        self.camera_off.setGeometry(QtCore.QRect(1050, 570, 200, 41))
        font = QtGui.QFont()
        font.setFamily("HelveticaNowDisplay Bold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.camera_off.setFont(font)
        self.camera_off.setStyleSheet("background-color: rgb(126, 126, 126);\n"
                                      "selection-background-color: rgb(0, 0, 0);\n"
                                      "gridline-color: rgb(0, 0, 0);")
        self.camera_off.setObjectName("camera_off")

        
        #Menu bar
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1280, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)


        #Status bar
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    #Rename elements on the interface
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Orereco"))
        self.pushButton.setText(_translate("MainWindow", "START"))
        self.label.setText(_translate("MainWindow", "          Select Model:"))
        self.pushButton_2.setText(_translate("MainWindow", "Select File"))
        self.contrast_big_label.setText(_translate("MainWindow", " Contrast"))
        self.sharpness_label.setText(_translate("MainWindow", " Sharpness"))
        self.accuracy_label.setText(_translate("MainWindow", " Accuracy"))
        self.calc_scale_view_btn.setText(_translate("MainWindow", "Сalculate the scale of the field of view"))
        self.calc_obj_size_btn.setText(_translate("MainWindow", "Calculate size of objects"))
        self.camera_on.setText(_translate("MainWindow", "Switch the camera on"))
        self.camera_off.setText(_translate("MainWindow", "Switch the camera off"))


#Separate image processing stream from the camera
class ThreadOpenCV(QThread):
    changePixmap = pyqtSignal(QImage)

    def __init__(self):
        super().__init__()
        self.status = True

    def run(self):
        self.cont = controller()
        self.cont.selectType(2)
        self.cont.selectSource(2)

        while self.status:
            ret, frame = self.cont.source.read()
            if ret:
                self.changePixmap.emit(self.cont.analyseShot())
                if cv2.waitKey(0) == ord('q'):
                    break       
            self.msleep(1)      
            cv2.destroyAllWindows()


class Window(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)            

        #connections
        self.pushButton.clicked.connect(self.start)
        self.pushButton_2.clicked.connect(self.open)
        self.camera_on.clicked.connect(self.can)
        self.camera_off.clicked.connect(self.kill_thread)
        self.thread = ThreadOpenCV()                                         
        self.thread.changePixmap.connect(self.setImage)
        
        
    #Open file function
    def open(self):
        try:
            cont.selectSource()
        except:
            print("File didn't chosen")


    #Start analysing function
    def start(self):
        try:
            im = cont.analyseShot()
            self.display.setPixmap(QPixmap.fromImage(im).scaled(800, 600))
            self.display.show()
        except:
            error = QtWidgets.QMessageBox()
            error.setWindowTitle("Error")
            error.setText("You can use only PIL Image or cv2 ndarray")
            error.setIcon(QtWidgets.QMessageBox.Icon.Warning)
            error.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok|QtWidgets.QMessageBox.StandardButton.Cancel)
            error.exec()             

    #Threading start
    def can(self):
        try:
            self.thread.start()
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
        print("Finishing...")
        self.thread.cont.source.release()
        cv2.destroyAllWindows()
        self.status = False
        time.sleep(1)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = Window()
    w.show()
    sys.exit(app.exec())
