import sqlite3
import sys
from random import choice
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QMessageBox, QDialog, QLineEdit, QComboBox
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

# Подключение к базе данных
conn = sqlite3.connect('DataM.sqlite')
cur = conn.cursor()

# Проверка существования таблицы и её создание при отсутствии
cur.execute('''
    CREATE TABLE IF NOT EXISTS dict (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        word TEXT NOT NULL,
        translation TEXT NOT NULL,
        counter TEXT NOT NULL
    )
''')
conn.commit()

# ©Maria Musarskaya, 2024

class AuthorisationWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 1080, 650)
        self.setWindowTitle('Simulator for learning foreign languages')
        self.setFixedSize(1080, 650)

        # Кнопка "Training"
        self.training_button = QPushButton('Training', self)
        self.training_button.setGeometry(100, 100, 200, 50)
        self.training_button.clicked.connect(self.on_training_click)

    def on_training_click(self):
        # Проверка наличия данных в словаре
        cur.execute('SELECT COUNT(*) FROM dict')
        count = cur.fetchone()[0]

        if count == 0:
            QMessageBox.critical(self, 'Ошибка', 'Словарь пуст. Добавьте данные для тренировки.')
            return

        # Логика тренировки (пример)
        QMessageBox.information(self, 'Успех', 'Тренировка началась!')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = AuthorisationWidget()
    main_window.show()
    sys.exit(app.exec_())
