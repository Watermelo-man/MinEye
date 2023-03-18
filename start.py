import sys
from window import Window
from PyQt6 import QtWidgets


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = Window()
    w.show()
    sys.exit(app.exec())