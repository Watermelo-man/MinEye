import sys
import cv2
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QPixmap, QImage



class ImageWindow(QWidget):
    def __init__(self, image):
        super().__init__()
        self.title = 'Image Viewer'
        self.left = 10
        self.top = 10
        self.width = image.shape[1]
        self.height = image.shape[0]
        self.image = image
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        label = QLabel(self)
        pixmap = self.convert_cv2_to_pixmap(self.image)
        label.setPixmap(pixmap)
        label.move(0, 0)
        self.show()

    def convert_cv2_to_pixmap(self, image):
        height, width, channel = image.shape
        bytesPerLine = 3 * width
        qImg = QImage(image.data, width, height, bytesPerLine, QImage.Format_RGB888)
        return QPixmap.fromImage(qImg)

if __name__ == '__main__':
    # load the cv2 image
    image = cv2.imread('C:\\Projects\\orereco\\source\\bottle.jpg')

    # create the Qt application
    app = QApplication(sys.argv)

    # create and show the image window
    window = ImageWindow(image)
    window.show()

    # run the Qt application
    sys.exit(app.exec_())