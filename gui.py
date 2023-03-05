import sys
import cv2
from PyQt6.QtCore import QSize, Qt, QObject, pyqtSignal
from PyQt6.QtWidgets import QApplication, QWidget, QLabel , QMainWindow, QPushButton,QVBoxLayout
from PyQt6.QtGui import QPixmap, QImage
from  control import *


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        #img = QPixmap("C:\\Users\\User\\Desktop\\orereco\\source\\0038.jpg") 
        self.setWindowTitle("Orereco")
        '''
        layout = QVBoxLayout()
        widgets = [QPushButton,QLabel]

        for w in widgets:
            layout.addWidget(w())

        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)

        '''


        self.setFixedSize(QSize(900, 600))

        button = QPushButton("Press")

        self.setCentralWidget(button)
        
        self.img = QLabel("hello")

        #img.resize(640,480)

        #self.setCentralWidget(img)


        #button.show()
        
        #img.show()


        button.clicked.connect(self.the_button_was_clicked)

    def the_button_was_clicked(self):
        im = analyseImg()
        self.img.setPixmap(QPixmap.fromImage(im).scaled(640,480))
        self.setCentralWidget(self.img)
        '''
        #self.setFixedSize(QSize(400, 300))

        button = QPushButton("Call func")       


        button.clicked.connect(self.the_button_was_clicked)


        button.show()
        
        labl = QLabel()
        md.predict(im)
        res= md.showLastShot()
        #create from numpy Qpixmap
        h,w,ch = res.shape
        bytes_per_line = ch*w
        convert_to_Qt_format = QImage(res.data, w, h, bytes_per_line, QImage.Format.Format_RGB888)
        #create from numpy Qpixmap
            
        labl.setPixmap(QPixmap.fromImage( convert_to_Qt_format).scaled(640,480))

        #self.setCentralWidget(labl)


        self.setCentralWidget(labl)
        labl.show()
        
 
    def the_button_was_clicked(self):
            print("Clicked!")
    '''

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()

""""
import sys

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton


# Подкласс QMainWindow для настройки главного окна приложения
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        button = QPushButton("Press Me!")

        self.setFixedSize(QSize(400, 300))

        # Устанавливаем центральный виджет Window.
        self.setCentralWidget(button)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()

"""