import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget

class NumberTable(QMainWindow):
    def __init__(self, numbers):
        super().__init__()

        self.setWindowTitle('Таблица с числами')
        
        # Создаем центральный виджет для главного окна
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        # Создаем макет
        layout = QVBoxLayout()

        # Создаем QTableWidget
        self.table = QTableWidget()
        #self.table.move(100, 100)
        # Устанавливаем количество строк и столбцов
        self.table.setRowCount(len(numbers))
        self.table.setColumnCount(1)
        
        # Заполняем таблицу числами из массива
        for i, num in enumerate(numbers):
            item = QTableWidgetItem(str(num))
            self.table.setItem(i, 0, item)

        layout.addWidget(self.table)
        central_widget.setLayout(layout)
        


        for i, num in enumerate(numbers):
            item = QTableWidgetItem(str(num))
            self.table.setItem(i, 0, item)
if __name__ == '__main__':
    app = QApplication(sys.argv)

    numbers = [1, 2, 3, 4, 5]  # Пример массива
    window = NumberTable(numbers)
    window.show()

    sys.exit(app.exec())