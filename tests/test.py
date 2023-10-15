import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QVBoxLayout

class TextEditExample(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Создаем поле с текстом (QLineEdit)
        self.text_edit = QLineEdit(self)
        self.text_edit.setPlaceholderText("Введите текст сюда")
        self.text_edit.setText("1")
        # Создаем вертикальное расположение виджетов
        layout = QVBoxLayout()
        layout.addWidget(self.text_edit)

        # Устанавливаем размещение для главного окна
        self.setLayout(layout)

        self.setWindowTitle('Пример текстового поля')
        self.setGeometry(100, 100, 300, 100)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = TextEditExample()
    ex.show()
    sys.exit(app.exec())