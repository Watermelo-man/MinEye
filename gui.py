import os
from PyQt6 import QtCore, QtGui, QtWidgets


from control import *




rootdir = str(os.path.dirname(os.path.abspath(__file__)))

path = os.path.join(rootdir,'ourmodels')


class Ui_MainWindow():
    layout = None
    
    #MainWindowInstance = None

    def __init__(self) -> None:
        self.layout = QtWidgets.QGridLayout()
        #self.MainWindowInstance = MainWindow
        pass
    
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
        self.StartButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.StartButton.setGeometry(QtCore.QRect(720, 630, 100, 60))
        font = QtGui.QFont()
        font.setFamily("HelveticaNowDisplay Bold")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.StartButton.setFont(font)
        self.StartButton.setStyleSheet("background-color: rgb(126, 126, 126);\n"
                                      "selection-background-color: rgb(0, 0, 0);\n"
                                      "gridline-color: rgb(0, 0, 0);")
        self.StartButton.setObjectName("pushButton")

  


        #Pause button
        self.pause = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pause.setGeometry(QtCore.QRect(830, 630, 100, 60))
        font = QtGui.QFont()
        font.setFamily("HelveticaNowDisplay Bold")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pause.setFont(font)
        self.pause.setStyleSheet("background-color: rgb(126, 126, 126);\n"
                                      "selection-background-color: rgb(0, 0, 0);\n"
                                      "gridline-color: rgb(0, 0, 0);")
        self.pause.setEnabled(False)
        self.pause.setObjectName("pushButton")


        #Panel with model and file
        self.FileModelPanel = QtWidgets.QLabel(parent=self.centralwidget)
        self.FileModelPanel.setGeometry(QtCore.QRect(20, 630, 680, 60))
        font = QtGui.QFont()
        font.setFamily("HelveticaNowDisplay Bold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.FileModelPanel.setFont(font)
        self.FileModelPanel.setStyleSheet("border-color: rgb(0, 0, 0);")
        self.FileModelPanel.setFrameShape(QtWidgets.QFrame.Shape.Panel)
        self.FileModelPanel.setLineWidth(1)
        self.FileModelPanel.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        #self.FileModelPanel.setObjectName("FileModelPanel")


        #Select model panel
        self.SelectModelBox = QtWidgets.QComboBox(parent=self.centralwidget)
        self.SelectModelBox.setGeometry(QtCore.QRect(150, 650, 400, 20))
        self.SelectModelBox.setStyleSheet("background-color: rgb(134, 134, 134);")
        #self.SelectModelButton.setObjectName("SelectModelBox")
        for pt_file in os.listdir(path):
            if pt_file.endswith(".pt"):
                self.SelectModelBox.addItem(pt_file)

        pathm = str(os.path.dirname(os.path.abspath(__file__)))
        pathm = os.path.join(pathm,'ourmodels')
        pathm = os.path.join(pathm,self.SelectModelBox.currentText())
        #print(self.SelectModelBox.currentText)
        cont.changeModelPath(pathm)


        #Select file button
        self.SelectFileButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.SelectFileButton.setGeometry(QtCore.QRect(580, 650, 80, 25))
        font = QtGui.QFont()
        font.setFamily("HelveticaNowDisplay Bold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.SelectFileButton.setFont(font)
        self.SelectFileButton.setStyleSheet("background-color: rgb(126, 126, 126);\n"
                                        "selection-background-color: rgb(0, 0, 0);\n"
                                        "gridline-color: rgb(0, 0, 0);")
        #self.SelectFileButton.setObjectName("SelectFileButton")
        MainWindow.setCentralWidget(self.centralwidget)


        #Contrast label
        self.contrast_big_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.contrast_big_label.setGeometry(QtCore.QRect(830, 10, 431, 601))
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


        #Brightness label
        self.brigtness_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.brigtness_label.setEnabled(True)
        self.brigtness_label.setGeometry(QtCore.QRect(835, 85, 111, 25))
        font = QtGui.QFont()
        font.setFamily("HelveticaNowDisplay Bold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.brigtness_label.setFont(font)
        self.brigtness_label.setAutoFillBackground(False)
        self.brigtness_label.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.brigtness_label.setLineWidth(1)
        self.brigtness_label.setObjectName("sharpness_label")


        #Accuracy label
        self.accuracy_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.accuracy_label.setEnabled(True)
        self.accuracy_label.setGeometry(QtCore.QRect(840, 157, 90, 21))
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

        #IOU label
        self.IOU_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.IOU_label.setEnabled(True)
        self.IOU_label.setGeometry(QtCore.QRect(840, 230, 90, 21))
        font = QtGui.QFont()
        font.setFamily("HelveticaNowDisplay Bold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(90)
        self.IOU_label.setFont(font)
        self.IOU_label.setAutoFillBackground(False)
        self.IOU_label.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.IOU_label.setLineWidth(1)
        self.IOU_label.setObjectName("IOU_label")

        #Contrast slider
        self.contrast_slider = QtWidgets.QSlider(parent=self.centralwidget)
        self.contrast_slider.setGeometry(QtCore.QRect(840, 40, 311, 30))
        self.contrast_slider.setStyleSheet("background-color: rgb(105, 105, 105);")
        self.contrast_slider.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.contrast_slider.setObjectName("contrast_slider")
        self.contrast_slider.setRange(0,160)
        self.contrast_slider.setSingleStep(1)
        #contrast label
        self.contrast_num_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.contrast_num_label.setGeometry(QtCore.QRect(1170, 40, 75, 30))
        self.contrast_num_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("HelveticaNowDisplay Bold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.contrast_num_label.setFont(font)
        self.contrast_num_label.setStyleSheet("gridline-color: rgb(0, 0, 0);")
        self.contrast_num_label.setFrameShape(QtWidgets.QFrame.Shape.Panel)
        
        self.contrast_num_label.setObjectName("accuracy_big_label")
        self.contrast_num_label.setText('0')


        #brightness slider
        self.brightness_slider = QtWidgets.QSlider(parent=self.centralwidget)
        self.brightness_slider.setGeometry(QtCore.QRect(840, 115, 311, 30))
        self.brightness_slider.setStyleSheet("background-color: rgb(105, 105, 105);")
        self.brightness_slider.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.brightness_slider.setObjectName("sharpness_slider")
        self.brightness_slider.setRange(-200,200)
        #brightness label
        self.brightness_num_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.brightness_num_label.setGeometry(QtCore.QRect(1170, 115, 75, 30))
        self.brightness_num_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("HelveticaNowDisplay Bold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.brightness_num_label.setFont(font)
        self.brightness_num_label.setStyleSheet("gridline-color: rgb(0, 0, 0);")
        self.brightness_num_label.setFrameShape(QtWidgets.QFrame.Shape.Panel)
        
        self.brightness_num_label.setObjectName("accuracy_big_label")
        self.brightness_num_label.setText('0')


        #Accuracy slider
        self.accuracy_slider = QtWidgets.QSlider(parent=self.centralwidget)
        
        self.accuracy_slider.setGeometry(QtCore.QRect(842, 185, 311, 30))
        self.accuracy_slider.setStyleSheet("background-color: rgb(105, 105, 105);")
        self.accuracy_slider.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.accuracy_slider.setObjectName("accuracy_slider")
        MainWindow.setCentralWidget(self.centralwidget)
        self.accuracy_slider.setRange(1,100)
        self.accuracy_slider.setSingleStep(1)
        self.accuracy_slider.setValue(50)


        self.accuracy_num_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.accuracy_num_label.setGeometry(QtCore.QRect(1170, 185, 75, 30))
        self.accuracy_num_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("HelveticaNowDisplay Bold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.accuracy_num_label.setFont(font)
        self.accuracy_num_label.setStyleSheet("gridline-color: rgb(0, 0, 0);")
        self.accuracy_num_label.setFrameShape(QtWidgets.QFrame.Shape.Panel)
        
        self.accuracy_num_label.setObjectName("accuracy_big_label")
        self.accuracy_num_label.setText('0.5')

        
        #IOU slider
        self.IOU_slider = QtWidgets.QSlider(parent=self.centralwidget)
        
        self.IOU_slider.setGeometry(QtCore.QRect(842, 255, 311, 30))
        self.IOU_slider.setStyleSheet("background-color: rgb(105, 105, 105);")
        self.IOU_slider.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.IOU_slider.setObjectName("IOU_slider")
        MainWindow.setCentralWidget(self.centralwidget)
        self.IOU_slider.setRange(1,100)
        self.IOU_slider.setSingleStep(1)
        self.IOU_slider.setValue(70)


        self.IOU_num_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.IOU_num_label.setGeometry(QtCore.QRect(1170, 255, 75, 30))
        self.IOU_num_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("HelveticaNowDisplay Bold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.IOU_num_label.setFont(font)
        self.IOU_num_label.setStyleSheet("gridline-color: rgb(0, 0, 0);")
        self.IOU_num_label.setFrameShape(QtWidgets.QFrame.Shape.Panel)
        
        self.IOU_num_label.setObjectName("accuracy_big_label")
        self.IOU_num_label.setText('0.7')
        
   
        #Count table
        self.count_table = QtWidgets.QTableWidget(self)
        #table.move(840, 400)
        self.count_table.setGeometry(QtCore.QRect(840, 400, 200, 150))
        self.count_table.setRowCount(1)
        #self.table.setRowCount(len(numbers))
        self.count_table.setColumnCount(2)
        self.count_table.setHorizontalHeaderLabels(['Minerals','Amount'])
        self.count_table.setStyleSheet("background-color: rgb(105, 105, 105);")

        '''
        for i, num in enumerate(numbers):
            item = QtWidgets.QTableWidgetItem(str(num))
            self.table.setItem(i, 0, item)
        '''

        #Count table
        self.size_table = QtWidgets.QTableWidget(self)
        #table.move(840, 400)
        self.size_table.setGeometry(QtCore.QRect(1050, 400, 200, 150))
        self.size_table.setRowCount(1)
        #self.table.setRowCount(len(numbers))
        self.size_table.setColumnCount(2)
        self.size_table.setHorizontalHeaderLabels(['Minerals','Size (px)'])
        self.size_table.setStyleSheet("background-color: rgb(105, 105, 105);")
        


        #Calculate scale view button
        self.calc_scale_view_btn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.calc_scale_view_btn.setGeometry(QtCore.QRect(840, 300, 311, 41))
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


        #scale unit size
        self.scale_unit_size = QtWidgets.QLineEdit(self)
        self.scale_unit_size.setGeometry(QtCore.QRect(1170, 300, 75, 41))

        font = QtGui.QFont()
        font.setFamily("HelveticaNowDisplay Bold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(90)
        self.scale_unit_size.setFont(font)
        self.scale_unit_size.setAutoFillBackground(False)
       # self.scale_unit_size.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        #self.scale_unit_size.setLineWidth(1)
        

       



        self.scale_unit_size.setStyleSheet("background-color: rgb(126, 126, 126);\n"
                                             "selection-background-color: rgb(0, 0, 0);\n"
                                             "gridline-color: rgb(0, 0, 0);")
        self.scale_unit_size.setPlaceholderText("Scale (mm)")
        regexpvalid = QtCore.QRegularExpression("^(?:\d+\.\d+|\d+)$")
        double_validator = QtGui.QRegularExpressionValidator(regexpvalid)
       
        self.scale_unit_size.setValidator(double_validator)




        #Calculate object size
        self.calc_obj_size_btn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.calc_obj_size_btn.setGeometry(QtCore.QRect(840, 350, 311, 41))#411
        font = QtGui.QFont()
        font.setFamily("HelveticaNowDisplay Bold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.calc_obj_size_btn.setFont(font)

        self.detailed_report = QtWidgets.QPushButton(parent=self.centralwidget)
        self.detailed_report.setGeometry(QtCore.QRect(1170, 350, 75, 41))
        font = QtGui.QFont()
        font.setFamily("HelveticaNowDisplay Bold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.detailed_report.setFont(font)



        self.calc_obj_size_btn.setStyleSheet("background-color: rgb(126, 126, 126);\n"
                                             "selection-background-color: rgb(0, 0, 0);\n"
                                             "gridline-color: rgb(0, 0, 0);")
        self.calc_obj_size_btn.setObjectName("calc_obj_size_btn")
        
        
       # self.calc_obj_size_btn.setObjectName("calc_obj_size_btn")

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

        #Turn off camera
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
        MainWindow.setWindowTitle(_translate("LolWindow", "MinEYE"))
        self.StartButton.setText(_translate("MainWindow", "START"))
        self.pause.setText(_translate("MainWindow", "PAUSE"))     
        self.FileModelPanel.setText(_translate("MainWindow", "Select Model:"))
        self.SelectFileButton.setText(_translate("MainWindow", "Select File"))
        self.contrast_big_label.setText(_translate("MainWindow", " Sharpness"))
        self.brigtness_label.setText(_translate("MainWindow", " Brigthness"))
        self.accuracy_label.setText(_translate("MainWindow", " Accuracy"))
        self.calc_scale_view_btn.setText(_translate("MainWindow", "Сalculate the scale of the field of view"))
        self.calc_obj_size_btn.setText(_translate("MainWindow", "Calculate size of objects"))
        self.camera_on.setText(_translate("MainWindow", "Switch the camera on"))
        self.camera_off.setText(_translate("MainWindow", "Switch the camera off"))
        self.detailed_report.setText(_translate("MainWindow", "Report"))
        self.IOU_label.setText(_translate("MainWindow","IoU"))