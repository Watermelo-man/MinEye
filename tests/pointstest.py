import sys
import cv2
import numpy as np
from PyQt6.QtCore import QTimer, Qt
from PyQt6.QtGui import QImage, QPixmap, QPainter, QPen
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel

class App(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Инициализация камеры
        self.cap = cv2.VideoCapture(0)
        self.initUI()
        
    def initUI(self):
        # Установка размеров и заголовка
        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle('OpenCV with PyQt5')
        
        # QLabel для отображения изображения с камеры
        self.display = QLabel(self)
        self.display.resize(640, 480)
        self.display.move(80, 50)

        # Кнопка для активации режима точек
        self.btn = QPushButton('Activate Points Mode', self)
        self.btn.resize(200, 40)
        self.btn.move(300, 550)
        self.btn.clicked.connect(self.activate_points_mode)

        # Таймер для обновления изображения
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(30)

        # Хранение координат двух точек
        self.point1 = None
        self.point2 = None

    def activate_points_mode(self):
        self.display.mousePressEvent = self.get_mouse_coords

    def get_mouse_coords(self, event):
        x, y = event.pos().x(), event.pos().y()
        if not self.point1:
            self.point1 = (x, y)
            #cv2.circle(frame, self.point1, 5, (0, 255, 0), -1)
        elif not self.point2:
            self.point2 = (x, y)
            #cv2.circle(frame, self.point2, 5, (0, 255, 0), -1)
        else:
            self.point1, self.point2 = (x, y), None

    def update_frame(self):
        ret, frame = self.cap.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Если есть две точки, рисуем их и линию между ними
        if self.point1:
            cv2.circle(frame, self.point1, 5, (0, 255, 0), -1)
        if self.point1 and self.point2:
            cv2.circle(frame, self.point1, 5, (0, 255, 0), -1)
            cv2.circle(frame, self.point2, 5, (0, 255, 0), -1)
            cv2.line(frame, self.point1, self.point2, (255, 0, 0), 2)
            
            
            # Рассчитать и отобразить расстояние между точками
            distance = int(np.sqrt((self.point2[0] - self.point1[0])**2 + (self.point2[1] - self.point1[1])**2))
            cv2.putText(frame, f"Distance: {distance}px", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

        # Конвертация изображения OpenCV в изображение PyQt5
        h, w, c = frame.shape
        qimg = QImage(frame.data, w, h, c * w, QImage.Format.Format_RGB888)
        pixmap = QPixmap.fromImage(qimg)
        self.display.setPixmap(pixmap)

    def closeEvent(self, event):
        self.cap.release()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.exit(app.exec())
