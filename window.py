from gui import *
from threads import ThreadOpenCV, ThreadOpenCVVideo
import gui_report
import time
import os

class Window(QtWidgets.QMainWindow, Ui_MainWindow):

    _calibration = False
    pause_flag = False

    def __init__(self):
        super().__init__()
        self.setupUi(self)           

        #connections

        self.pause.clicked.connect(self.pause_video)

        self.display.mousePressEvent = self.get_mouse_coords
        self.calc_scale_view_btn.setEnabled(False)
        self.calc_obj_size_btn.setEnabled(False)
        self.scale_unit_size.setEnabled(False)
        self.brightness_slider.valueChanged.connect(self.brightness_change)
        self.contrast_slider.valueChanged.connect(self.change_contrast)
        self.accuracy_slider.valueChanged.connect(self.accuracy_change)
        self.calc_scale_view_btn.clicked.connect(self.activate_points_mode)
        self.calc_obj_size_btn.clicked.connect(self.Count)
        self.StartButton.clicked.connect(self.start)
        self.SelectFileButton.clicked.connect(self.open)
        self.SelectModelBox.currentTextChanged.connect(self.changeModel)
        self.camera_on.clicked.connect(self.cam)
        self.camera_off.clicked.connect(self.stop_cam)
        self.scale_unit_size.textChanged.connect(self.change_scale)
        self.detailed_report.clicked.connect(self.report)

    def changeModel(self):
        try:
            if self.thread_cam != None:
                self.stop_cam()
            elif self.thread_vid != None:
                self.stop_video()
        except:
            pass
        path = str(os.path.dirname(os.path.abspath(__file__)))
        path = os.path.join(path,'ourmodels')
        path = os.path.join(path,self.SelectModelBox.currentText())
        #print(self.SelectModelBox.currentText)
        cont.changeModelPath(path)





    #Open file function
    def open(self):
        try:
            cont.selectSource(1)
            # self.accuracy_slider.setEnabled(True)
            # self.contrast_slider.setEnabled(True)
            # self.brightness_slider.setEnabled(True)
        except Exception as e:
            print(e)
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
                    self.calc_scale_view_btn.setEnabled(True)
                    self.scale_unit_size.setEnabled(True)
                    self.calc_obj_size_btn.setEnabled(True)

                    self.StartButton.clicked.disconnect(self.start)
                    self.StartButton.setText("STOP")
                    self.thread_vid = ThreadOpenCVVideo()
                    self.thread_vid.changePixmap.connect(self.setImage)
                    self.thread_vid.start()
                    self.StartButton.clicked.connect(self.stop_video)
                    self.pause.setEnabled(True)
                    self.SelectModelBox.setEnabled(False)
                    self.SelectFileButton.setEnabled(False)
                    self.camera_off.setEnabled(False)
                    self.camera_on.setEnabled(False)
                    self.accuracy_slider.setEnabled(True)
                    self.contrast_slider.setEnabled(True)
                    self.brightness_slider.setEnabled(True)
                    #self.pause.clicked.connect(self.pause_video)

                    
                else:
                    raise AttributeError
            else:
                self.accuracy_slider.setEnabled(True)
                self.contrast_slider.setEnabled(True)
                self.brightness_slider.setEnabled(True)
                self.calc_scale_view_btn.setEnabled(True)
                self.scale_unit_size.setEnabled(True)
                self.calc_obj_size_btn.setEnabled(True)
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
            self.calc_scale_view_btn.setEnabled(False)
            self.scale_unit_size.setEnabled(False)
            self.calc_obj_size_btn.setEnabled(False)
            self.thread_vid.stop()
            self.thread_vid.changePixmap.disconnect(self.setImage)
            del self.thread_vid
            #self.thread_vid = None
            cont.source = None
            self.StartButton.clicked.disconnect(self.stop_video)
            self.StartButton.clicked.connect(self.start)
            self.StartButton.setText("START")
            self.accuracy_slider.setEnabled(False)
            self.contrast_slider.setEnabled(False)
            self.brightness_slider.setEnabled(False)
            try:
                self.pause.clicked.disconnect(self.continue_video)
                self.pause.setText("PAUSE")
                self.pause.clicked.connect(self.pause_video)
            except:
                pass
            self.SelectModelBox.setEnabled(True)
            self.SelectFileButton.setEnabled(True)
            self.pause.setEnabled(False)
            self.camera_off.setEnabled(True)
            self.camera_on.setEnabled(True)
        except AttributeError as ex:
            print(ex)


    #Pause video
    def pause_video(self):
        try:
            self.thread_vid.recordStatus = 0#1
            self.pause.clicked.disconnect(self.pause_video)
            self.pause.setText("CONTINUE")
            self.pause.clicked.connect(self.continue_video)
            self.pause_flag = True
            cont.selectSource(3)
            cont.selectType(1)
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
            cont.selectSource(4)
            self.thread_vid.recordStatus = 0
            self.pause.clicked.disconnect(self.continue_video)
            self.pause.setText("PAUSE")
            self.pause.clicked.connect(self.pause_video)
            
            self.pause_flag = False
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
            self.calc_scale_view_btn.setEnabled(True)
            self.scale_unit_size.setEnabled(True)
            self.calc_obj_size_btn.setEnabled(True)
            self.camera_on.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                               "selection-background-color: rgb(0, 0, 0);\n"
                                               "gridline-color: rgb(0, 0, 0);")
            self.SelectFileButton.setEnabled(False)
            self.thread_cam = ThreadOpenCV()                                     
            self.thread_cam.changePixmap.connect(self.setImage)
            cont.selectSource(2)
            self.thread_cam.start()
            self.camera_off.setEnabled(True)
            self.camera_on.setEnabled(False)
            self.StartButton.setEnabled(False)
            self.accuracy_slider.setEnabled(True)
            self.contrast_slider.setEnabled(True)
            self.brightness_slider.setEnabled(True)
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
            #self.thread_cam = None
            cont.source = None
            self.camera_off.setEnabled(False)
            self.camera_on.setEnabled(True)
            self.calc_scale_view_btn.setEnabled(False)
            self.scale_unit_size.setEnabled(False)
            self.calc_obj_size_btn.setEnabled(False)
            self.StartButton.setEnabled(True)
            self.SelectFileButton.setEnabled(True)
            self.accuracy_slider.setEnabled(False)
            self.contrast_slider.setEnabled(False)
            self.brightness_slider.setEnabled(False)
            self.camera_on.setStyleSheet("background-color: rgb(126, 126, 126);\n"
                                               "selection-background-color: rgb(0, 0, 0);\n"
                                               "gridline-color: rgb(0, 0, 0);")
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
        self.display.setPixmap(QPixmap.fromImage(image))#.scaled(800, 600))


    def activate_points_mode(self):
        self.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.CrossCursor))
        self.calc_scale_view_btn.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                               "selection-background-color: rgb(0, 0, 0);\n"
                                               "gridline-color: rgb(0, 0, 0);")
        self._calibration = not self._calibration

        self.camera_off.setEnabled(not self._calibration)
        self.StartButton.setEnabled(not self._calibration)

        if not self._calibration:
            cont.point1 = None
            cont.point2 = None
            cont.point3 = None
            cont.ypixlength = 0
            cont.xpixlength = 0
            self.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
            self.calc_scale_view_btn.setStyleSheet("background-color: rgb(126, 126, 126);\n"
                                               "selection-background-color: rgb(0, 0, 0);\n"
                                               "gridline-color: rgb(0, 0, 0);")
            # if self.pause:
            #     self.setImage(cont.analyseShot())

            if type(cont.model) == universal_model.modelType.PictureModel:
                self.setImage(cont.analyseShot())
        #self.display.mousePressEvent = self.get_mouse_coords

    def get_mouse_coords(self, event):

        if self._calibration:
            x, y = event.pos().x(), event.pos().y()
        
            if not cont.point1:
                cont.set_point_1((x,y))
                #cont.point1 = (x, y)
                #cv2.circle(frame, self.point1, 5, (0, 255, 0), -1)
            elif not cont.point2:
                cont.set_point_2((x,y))
                #cont.point2 = (x, y)
                #cv2.circle(frame, self.point2, 5, (0, 255, 0), -1)
            elif not cont.point3:
                 cont.set_point_3((x,y))
                 #cont.point3 = (x,y)
            else:
                cont.set_point_1((x,y))
                cont.set_point_2(None)
                cont.set_point_3(None)
                #cont.point1, cont.point2,cont.point3  = (x, y), None , None
            
            # if self.pause:
            #     self.setImage(cont.analyseShot())

            if type(cont.model) == universal_model.modelType.PictureModel:
                self.setImage(cont.analyseShot())
                

        
    def Count(self):

        self.count_table.clear()
        self.size_table.clear()
        mineralCntDict = cont.CountShot()

        if mineralCntDict != None:
            self.count_table.setRowCount(len(mineralCntDict))
            cnt = 0
            for key, value in mineralCntDict.items():
                item = QtWidgets.QTableWidgetItem(str(key))
                self.count_table.setItem(cnt, 0, item)
                item = QtWidgets.QTableWidgetItem(str(round(value,3)))
                self.count_table.setItem(cnt, 1, item)
                cnt+=1
        mineralSize = cont.CountSquare(mineralCntDict)
        if mineralSize != None:
            self.size_table.setRowCount(len(mineralCntDict))
            cnt = 0
            for key, value in mineralSize.items():
                item = QtWidgets.QTableWidgetItem(str(key))
                self.size_table.setItem(cnt, 0, item)
                item = QtWidgets.QTableWidgetItem(str(round(value,3)))
                self.size_table.setItem(cnt, 1, item)
                cnt+=1


    def report(self):
        mineralCntDict = cont.CountShot()
        if mineralCntDict != None:
            cont.CountSquareDetailed(mineralCntDict)
            self.rep = gui_report.AnotherWindow()
            self.rep.show_table()
            self.rep.show()

    def accuracy_change(self,value):
        self.accuracy_num_label.setText(str(value/100))
        cont.change_confidence(value/100)

        # if self.pause_flag:
        #     self.setImage(cont.)

        if type(cont.model) == universal_model.modelType.PictureModel:
            self.setImage(cont.analyseShot())

        # for i, num in enumerate(mineralCntDict):
        #     item = QtWidgets.QTableWidgetItem(str(num))
        #     self.table.setItem(i, 0, item)
    
    def change_contrast(self,value):
        self.contrast_num_label.setText(str(value/10))
        cont.change_contrast(value/10)

        # if self.pause_flag:
        #     self.setImage(cont.analyseShot())

        if type(cont.model) == universal_model.modelType.PictureModel:
            self.setImage(cont.analyseShot())

    def brightness_change(self,value):
        self.brightness_num_label.setText(str(value))
        cont.change_brightness(value)

        # if self.pause_flag :
        #     self.setImage(cont.analyseShot())

        if type(cont.model) == universal_model.modelType.PictureModel:
            self.setImage(cont.analyseShot())
    
    def change_scale(self,value):
        if value != '':
            value_flt=float(value)
            cont.change_scale(value_flt)