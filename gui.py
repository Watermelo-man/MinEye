from PyQt6.QtWidgets import QApplication, QWidget
import sys
    # caution: path[0] is reserved for script path (or '' in REPL)
sys.path.insert(1, "C:/Projects/orereco/universal_model")

import universal_model.universal_model


# Только для доступа к аргументам командной строки

# Приложению нужен один (и только один) экземпляр QApplication.
# Передаём sys.argv, чтобы разрешить аргументы командной строки для приложения.
# Если не будете использовать аргументы командной строки, QApplication([]) тоже работает



#Kernel = kernel("ourmodels/onlygold.pt","cpu")

app = QApplication(sys.argv)

# Создаём виджет Qt — окно.
window = QWidget()
window.show()  # Важно: окно по умолчанию скрыто.

# Запускаем цикл событий.
app.exec()
