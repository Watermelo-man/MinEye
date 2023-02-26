from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication, QMainWindow
import sys

    # caution: path[0] is reserved for script path (or '' in REPL)
sys.path.insert(1, "C:/Projects/orereco/universal_model")

#from  universal_model.universal_model import *



# Только для доступа к аргументам командной строки

# Приложению нужен один (и только один) экземпляр QApplication.
# Передаём sys.argv, чтобы разрешить аргументы командной строки для приложения.
# Если не будете использовать аргументы командной строки, QApplication([]) тоже работает



#Kernel = kernel("ourmodels/onlygold.pt","cuda:0")



class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        self.setGeometry(400,400,500,300)
        #self.setWindowTitle("My App")
        videowindow = QtWidgets.QLabel(self)
        videowindow.setText("GUI application with PyQt5")
        videowindow.show()


app = QApplication(sys.argv)

# Создаём виджет Qt — окно.
window = MainWindow()
window.show()  # Важно: окно по умолчанию скрыто.

# Запускаем цикл событий.
app.exec()


