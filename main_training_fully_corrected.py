
import sqlite3
import random
from PyQt5.QtWidgets import QMessageBox

# Подключение к базе данных
conn = sqlite3.connect('DataM.sqlite')  # Указываем корректное имя базы данных
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

import sys
import sqlite3
from random import choice
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, qApp, QMessageBox
from PyQt5.QtWidgets import QDialog, QLineEdit, QComboBox
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt


class AuthorisationWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 1080, 650)
        self.setWindowTitle('Simulator for learning foreign languages')
        self.setFixedSize(1080, 650)
        self.setStyleSheet(f"background-image: url('5.png'); background-position: center; background-repeat: no-repeat; background-attachment: fixed;")

        self.pixmap = QPixmap('1.png')
        self.logo = QLabel(self)
        self.logo.move(60, 20)
        self.logo.resize(305, 178)
        self.logo.setPixmap(self.pixmap)

        self.pixmap_pic1 = QPixmap('10.1.png')
        self.pic_1 = QLabel(self)
        self.pic_1.move(490, 0)
        self.pic_1.resize(190, 650)
        self.pic_1.setPixmap(self.pixmap_pic1)

        self.pixmap_pic2 = QPixmap('11.1.png')
        self.pic_2 = QLabel(self)
        self.pic_2.move(690, 0)
        self.pic_2.resize(190, 650)
        self.pic_2.setPixmap(self.pixmap_pic2)

        self.pixmap_pic3 = QPixmap('12.1.png')
        self.pic_3 = QLabel(self)
        self.pic_3.move(890, 0)
        self.pic_3.resize(190, 650)
        self.pic_3.setPixmap(self.pixmap_pic3)

        self.btn_add = QPushButton('Add word', self)
        self.btn_add.move(67, 190)
        self.btn_add.resize(314, 42)
        self.btn_add.clicked.connect(self.add_word_widget)
        style_sheet_1 = (
            "QPushButton { color: #FFFFFF; background: #003953; border: 1px solid #003953; border-radius: 10px; }"
            "QPushButton:hover { background-color: #00141C; }"
            "QPushButton:pressed { background-color: #00141C; }"
        )
        self.btn_add.setStyleSheet(style_sheet_1)

        self.btn_edit = QPushButton('Edit word', self)
        self.btn_edit.move(67, 250)
        self.btn_edit.resize(314, 42)
        self.btn_edit.clicked.connect(self.edit_word)
        style_sheet_2 = (
            "QPushButton { color: #FFFFFF; background: #003953; border: 1px solid #003953; border-radius: 10px; }"
            "QPushButton:hover { background-color: #00141C; }"
            "QPushButton:pressed { background-color: #00141C; }"
        )
        self.btn_edit.setStyleSheet(style_sheet_2)

        self.btn_remove = QPushButton('Delete word', self)
        self.btn_remove.move(67, 310)
        self.btn_remove.resize(314, 42)
        self.btn_remove.clicked.connect(self.show_remove_dialog)
        style_sheet_3 = (
            "QPushButton { color: #FFFFFF; background: #003953; border: 1px solid #003953; border-radius: 10px; }"
            "QPushButton:hover { background-color: #00141C; }"
            "QPushButton:pressed { background-color: #00141C; }"
        )
        self.btn_remove.setStyleSheet(style_sheet_3)

        self.btn_train = QPushButton('Training', self)
        self.btn_train.move(67, 400)
        self.btn_train.resize(314, 42)
        self.btn_train.clicked.connect(self.train_widget)
        style_sheet_4 = (
            "QPushButton { color: #FFFFFF; background: #003953; border: 1px solid #003953; border-radius: 10px; }"
            "QPushButton:hover { background-color: #00141C; }"
            "QPushButton:pressed { background-color: #00141C; }"
        )
        self.btn_train.setStyleSheet(style_sheet_4)

        self.btn_statistics = QPushButton('Statistics', self)
        self.btn_statistics.move(67, 490)
        self.btn_statistics.resize(314, 42)
        self.btn_statistics.clicked.connect(self.show_statistics)
        style_sheet_5 = (
            "QPushButton { color: #FFFFFF; background: #003953; border: 1px solid #003953; border-radius: 10px; }"
            "QPushButton:hover { background-color: #00141C; }"
            "QPushButton:pressed { background-color: #00141C; }"
        )
        self.btn_statistics.setStyleSheet(style_sheet_5)

        self.copyright = QLabel("©Maria Musarskaya, 2024", self)
        self.copyright.move(138, 565)
        self.copyright.resize(self.copyright.sizeHint())
        style_sheet_l = "QLabel { color: #003953; }"
        self.copyright.setStyleSheet(style_sheet_l)

    def edit_word(self):
        edit_widget = EditWordWidget()
        edit_widget.set_main_window(self)
        edit_widget.exec_()

    def show_remove_dialog(self):
        remove_dialog = RemoveWordWidget(self)
        remove_dialog.set_main_window(self)
        remove_dialog.exec_()

    def show_statistics(self):
        con = sqlite3.connect('DataM.sqlite')
        cur = con.cursor()
        total_words = cur.execute("SELECT COUNT(*) FROM dict").fetchone()[0]
        learned_words = cur.execute("SELECT COUNT(*) FROM dict WHERE counter > 10").fetchone()[0]
        con.close()

        stat_dialog = QDialog(self)
        stat_dialog.setWindowTitle('Statistics')
        stat_dialog.setGeometry(400, 300, 300, 150)

        stat_label = QLabel(f'Общее кол-во слов: {total_words}', stat_dialog)
        style_sheet_9 = "QLabel { color: #003953; }"
        stat_label.setStyleSheet(style_sheet_9)
        stat_label.setGeometry(20, 20, 260, 100)
        stat_label.setAlignment(Qt.AlignCenter)

        stat_dialog.exec_()

    def add_word_widget(self):
        adding_widget = AddingWidget()
        adding_widget.set_main_window(self)
        adding_widget.exec_()

    def train_widget(self):
        training_widget = TrainWidget()
        training_widget.set_main_window(self)
        training_widget.exec_()

    def set_main_window(self, main_window):
        self.main_window = main_window


class AddingWidget(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 400, 230)
        self.setWindowTitle('Adding word to the dictionary')
        self.setFixedSize(400, 230)
        self.setStyleSheet(f"background-image: url('5.png'); background-position: center; background-repeat: no-repeat; background-attachment: fixed;")

        self.label_name = QLabel('Добавление слова в словарь', self)
        self.label_name.move(100, 10)
        self.label_name.resize(self.label_name.sizeHint())
        style_sheet_1 = "QLabel { color: #003953; }"
        self.label_name.setStyleSheet(style_sheet_1)

        self.label_1 = QLabel('Иностранное слово', self)
        self.label_1.move(40, 50)
        self.label_1.resize(self.label_1.sizeHint())
        style_sheet_2 = "QLabel { color: #003953; }"
        self.label_1.setStyleSheet(style_sheet_2)

        self.word = QLineEdit(self)
        self.word.move(200, 50)
        self.word.resize(161, 20)
        style_sheet_3 = (
            "QLineEdit { color: #636364; border: 1.2px solid #636364; border-radius: 10px; }"
            "QLineEdit:focus { color: #003953; border: 1.2px solid #636364; border-radius: 10px; }"
        )
        self.word.setStyleSheet(style_sheet_3)

        self.label_2 = QLabel('Его перевод', self)
        self.label_2.move(40, 80)
        self.label_2.resize(self.label_2.sizeHint())
        style_sheet_4 = "QLabel { color: #003953; }"
        self.label_2.setStyleSheet(style_sheet_4)

        self.translation = QLineEdit(self)
        self.translation.move(200, 80)
        self.translation.resize(161, 20)
        style_sheet_5 = (
            "QLineEdit { color: #636364; border: 1.2px solid #636364; border-radius: 10px; }"
            "QLineEdit:focus { color: #003953; border: 1.2px solid #636364; border-radius: 10px; }"
        )
        self.translation.setStyleSheet(style_sheet_5)

        self.accept_btn = QPushButton('OK', self)
        self.accept_btn.move(200, 130)
        self.accept_btn.resize(self.accept_btn.sizeHint())
        self.accept_btn.clicked.connect(self.add)
        style_3 = (
            "QPushButton { color: #FFFFFF; background: #003953; border: 1px solid #003953; border-radius: 10px; }"
            "QPushButton:hover { background-color: #00141C; }"
            "QPushButton:pressed { background-color: #00141C; }"
        )
        self.accept_btn.setStyleSheet(style_3)

        self.cancel_btn = QPushButton('Cancel', self)
        self.cancel_btn.move(285, 130)
        self.cancel_btn.resize(self.cancel_btn.sizeHint())
        self.cancel_btn.clicked.connect(self.cancel)
        style_4 = (
            "QPushButton { color: #FFFFFF; background: #003953; border: 1px solid #003953; border-radius: 10px; }"
            "QPushButton:hover { background-color: #00141C; }"
            "QPushButton:pressed { background-color: #00141C; }"
        )
        self.cancel_btn.setStyleSheet(style_4)

    def add(self):
        word_to_add = self.word.text().lower()
        translation_to_add = self.translation.text().lower()

        con = sqlite3.connect('DataM.sqlite')
        cur = con.cursor()
        existing_word = cur.execute(f"SELECT COUNT(*) FROM dict WHERE word = '{word_to_add}'").fetchone()[0]

        if existing_word > 0:
            warning_msg = MyMessageBox('Это слово уже существует в словаре.', self)
            warning_msg.exec_()
        else:
            cur.execute(
                f"INSERT INTO dict(word, translation, counter) VALUES('{word_to_add}', '{translation_to_add}', 0)")
            con.commit()
            con.close()
            self.accept()

    def cancel(self):
        self.reject()

    def set_main_window(self, main_window):
        self.main_window = main_window


class MyMessageBox(QMessageBox):
    def __init__(self, text, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Предупреждение')
        self.setIcon(QMessageBox.Warning)
        self.setText(text)

        self.custom_button = QPushButton('OK', self)
        self.custom_button.resize(100, 20)
        self.custom_button.setStyleSheet(
            "QPushButton { color: #FFFFFF; background: #003953; border: 1px solid #003953; border-radius: 10px; }"
            "QPushButton:hover { background-color: #00141C; }"
            "QPushButton:pressed { background-color: #00141C; }"
        )

        self.custom_button.clicked.connect(self.accept)
        self.addButton(self.custom_button, QMessageBox.AcceptRole)
        self.setStyleSheet(
            "QMessageBox { background-color: #F5F5DC; }"
            "QMessageBox QLabel { color: #003953; }"
        )


class EditWordWidget(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 400, 230)
        self.setWindowTitle('Editing word in the dictionary')
        self.setFixedSize(400, 230)
        self.setStyleSheet(f"background-image: url('5.png'); background-position: center; background-repeat: no-repeat; background-attachment: fixed;")

        self.label_edit_name = QLabel('Редактирование перевода', self)
        self.label_edit_name.move(100, 10)
        self.label_edit_name.resize(self.label_edit_name.sizeHint())
        style_sheet_1 = "QLabel { color: #003953; }"
        self.label_edit_name.setStyleSheet(style_sheet_1)

        self.label_edit = QLabel('Выберите слово для редактирования:', self)
        self.label_edit.move(40, 50)
        self.label_edit.resize(self.label_edit.sizeHint())
        style_sheet_2 = "QLabel { color: #003953; }"
        self.label_edit.setStyleSheet(style_sheet_2)

        self.word_to_edit = QComboBox(self)
        self.word_to_edit.move(300, 50)
        self.word_to_edit.resize(90, 21)
        self.word_to_edit.setStyleSheet("QComboBox { background-color: #003953; }")
        self.populate_word_combo_box()

        self.label_new_translation = QLabel('Новый перевод:', self)
        self.label_new_translation.move(40, 80)
        self.label_new_translation.resize(self.label_new_translation.sizeHint())
        style_sheet_4 = "QLabel { color: #003953; }"
        self.label_new_translation.setStyleSheet(style_sheet_4)

        self.new_translation = QLineEdit(self)
        self.new_translation.move(160, 80)
        self.new_translation.resize(161, 20)
        style_sheet_5 = (
            "QLineEdit { color: #636364; border: 1.2px solid #636364; border-radius: 10px; }"
            "QLineEdit:focus { color: #003953; border: 1.2px solid #636364; border-radius: 10px; }"
        )
        self.new_translation.setStyleSheet(style_sheet_5)

        self.accept_btn = QPushButton('OK', self)
        self.accept_btn.move(200, 130)
        self.accept_btn.resize(self.accept_btn.sizeHint())
        self.accept_btn.clicked.connect(self.edit)
        style_3 = (
            "QPushButton { color: #FFFFFF; background: #003953; border: 1px solid #003953; border-radius: 10px; }"
            "QPushButton:hover { background-color: #00141C; }"
            "QPushButton:pressed { background-color: #00141C; }"
        )
        self.accept_btn.setStyleSheet(style_3)

        self.cancel_btn = QPushButton('Cancel', self)
        self.cancel_btn.move(285, 130)
        self.cancel_btn.resize(self.cancel_btn.sizeHint())
        self.cancel_btn.clicked.connect(self.cancel)
        style_4 = (
            "QPushButton { color: #FFFFFF; background: #003953; border: 1px solid #003953; border-radius: 10px; }"
            "QPushButton:hover { background-color: #00141C; }"
            "QPushButton:pressed { background-color: #00141C; }"
        )
        self.cancel_btn.setStyleSheet(style_4)

    def populate_word_combo_box(self):
        con = sqlite3.connect('DataM.sqlite')
        cur = con.cursor()
        result = cur.execute("SELECT word FROM dict").fetchall()
        words = [str(x[0]) for x in result]
        self.word_to_edit.addItems(words)
        con.close()

    def edit(self):
        selected_word = self.word_to_edit.currentText()
        new_translation = self.new_translation.text().lower()
        con = sqlite3.connect('DataM.sqlite')
        cur = con.cursor()
        cur.execute(f"UPDATE dict SET translation = '{new_translation}' WHERE word = '{selected_word}'")
        con.commit()
        con.close()
        self.accept()

    def cancel(self):
        self.reject()

    def set_main_window(self, main_window):
        self.main_window = main_window


class RemoveWordWidget(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 400, 230)
        self.setWindowTitle('Editing word in the dictionary')
        self.setFixedSize(400, 230)
        self.setStyleSheet(f"background-image: url('5.png'); background-position: center; background-repeat: no-repeat; background-attachment: fixed;")

        self.label = QLabel('Введите иностранное слово для удаления:', self)
        self.label.move(100, 40)
        self.label.resize(self.label.sizeHint())
        style_1 = "QLabel { color: #003953; }"
        self.label.setStyleSheet(style_1)

        self.word_input = QLineEdit(self)
        self.word_input.move(108, 70)
        self.word_input.resize(161, 20)
        style_2 = (
            "QLineEdit { color: #636364; border: 1.2px solid #636364; border-radius: 10px; }"
            "QLineEdit:focus { color: #003953; border: 1.2px solid #636364; border-radius: 10px; }"
        )
        self.word_input.setStyleSheet(style_2)

        self.accept_btn = QPushButton('OK', self)
        self.accept_btn.move(200, 130)
        self.accept_btn.resize(self.accept_btn.sizeHint())
        self.accept_btn.clicked.connect(self.remove_word)
        style_3 = (
            "QPushButton { color: #FFFFFF; background: #003953; border: 1px solid #003953; border-radius: 10px; }"
            "QPushButton:hover { background-color: #00141C; }"
            "QPushButton:pressed { background-color: #00141C; }"
        )
        self.accept_btn.setStyleSheet(style_3)

        self.cancel_btn = QPushButton('Cancel', self)
        self.cancel_btn.move(285, 130)
        self.cancel_btn.resize(self.cancel_btn.sizeHint())
        self.cancel_btn.clicked.connect(self.reject)
        style_4 = (
            "QPushButton { color: #FFFFFF; background: #003953; border: 1px solid #003953; border-radius: 10px; }"
            "QPushButton:hover { background-color: #00141C; }"
            "QPushButton:pressed { background-color: #00141C; }"
        )
        self.cancel_btn.setStyleSheet(style_4)

    def remove_word(self):
        word_to_remove = self.word_input.text().lower()
        con = sqlite3.connect('DataM.sqlite')
        cur = con.cursor()
        cur.execute(f"DELETE FROM dict WHERE word = '{word_to_remove}'")
        con.commit()
        con.close()
        self.accept()

    def set_main_window(self, main_window):
        self.main_window = main_window


class TrainWidget(QDialog):
    def __init__(self):
        super().__init__()
        self.minim = '0'
        self.initUI()

    def initUI(self):
        self.setGeometry(350, 300, 350, 275)
        self.setWindowTitle('Trainer')
        self.setFixedSize(350, 275)
        self.setStyleSheet(f"background-image: url('5.png'); background-position: center; background-repeat: no-repeat; background-attachment: fixed;")

        self.label_3 = QLabel('Напиши перевод слова:', self)
        self.label_3.move(20, 40)
        self.label_3.resize(151, 41)
        style_sheet_1 = "QLabel { color: #003953; }"
        self.label_3.setStyleSheet(style_sheet_1)

        self.word = QLineEdit(self)
        self.word.move(190, 50)
        self.word.resize(111, 21)
        style_sheet_2 = (
            "QLineEdit { color: #636364; border: 1.2px solid #636364; border-radius: 10px; }"
            "QLineEdit:focus { color: #003953; border: 1.2px solid #636364; border-radius: 10px; }"
        )
        self.word.setStyleSheet(style_sheet_2)
        self.set_word()

        self.label_4 = QLabel('Мой вариант:', self)
        self.label_4.move(20, 80)
        self.label_4.resize(91, 21)
        style_sheet_3 = "QLabel { color: #003953; }"
        self.label_4.setStyleSheet(style_sheet_3)

        self.option = QLineEdit(self)
        self.option.move(190, 80)
        self.option.resize(111, 21)
        style_sheet_4 = (
            "QLineEdit { color: #636364; border: 1.2px solid #636364; border-radius: 10px; }"
            "QLineEdit:focus { color: #003953; border: 1.2px solid #636364; border-radius: 10px; }"
        )
        self.option.setStyleSheet(style_sheet_4)

        self.btn_check = QPushButton('Проверить', self)
        self.btn_check.move(120, 110)
        self.btn_check.resize(self.btn_check.sizeHint())
        self.btn_check.clicked.connect(self.check)
        style_sheet_5 = (
            "QPushButton { color: #FFFFFF; background: #003953; border: 1px solid #003953; border-radius: 10px; }"
            "QPushButton:hover { background-color: #00141C; }"
            "QPushButton:pressed { background-color: #00141C; }"
        )
        self.btn_check.setStyleSheet(style_sheet_5)

        self.label_res = QLabel('Результат:', self)
        self.label_res.move(50, 150)
        self.label_res.resize(71, 21)
        style_sheet_6 = "QLabel { color: #003953; }"
        self.label_res.setStyleSheet(style_sheet_6)

        self.my_status = QLineEdit(self)
        self.my_status.move(190, 150)
        self.my_status.resize(111, 21)
        style_sheet_7 = (
            "QLineEdit { color: #636364; border: 1.2px solid #636364; border-radius: 10px; }"
            "QLineEdit:focus { color: #003953; border: 1.2px solid #636364; border-radius: 10px; }"
        )
        self.my_status.setStyleSheet(style_sheet_7)

        self.btn_show_ans = QPushButton('Показать ответ:', self)
        self.btn_show_ans.move(30, 190)
        self.btn_show_ans.resize(self.btn_show_ans.sizeHint())
        self.btn_show_ans.clicked.connect(self.show_answer)
        style_sheet_8 = (
            "QPushButton { color: #FFFFFF; background: #003953; border: 1px solid #003953; border-radius: 10px; }"
            "QPushButton:hover { background-color: #00141C; }"
            "QPushButton:pressed { background-color: #00141C; }"
        )
        self.btn_show_ans.setStyleSheet(style_sheet_8)

        self.answer = QLineEdit(self)
        self.answer.move(190, 190)
        self.answer.resize(111, 21)
        style_sheet_9 = (
            "QLineEdit { color: #636364; border: 1.2px solid #636364; border-radius: 10px; }"
            "QLineEdit:focus { color: #003953; border: 1.2px solid #636364; border-radius: 10px; }"
        )
        self.answer.setStyleSheet(style_sheet_9)

        self.make_new_word = QPushButton('Новое слово', self)
        self.make_new_word.move(110, 230)
        self.make_new_word.resize(self.make_new_word.sizeHint())
        self.make_new_word.clicked.connect(self.set_word)
        style_sheet_10 = (
            "QPushButton { color: #FFFFFF; background: #003953; border: 1px solid #003953; border-radius: 10px; }"
            "QPushButton:hover { background-color: #00141C; }"
            "QPushButton:pressed { background-color: #00141C; }"
        )
        self.make_new_word.setStyleSheet(style_sheet_10)

    def set_word(self):
        con = sqlite3.connect('DataM.sqlite')
        cur = con.cursor()
        result = cur.execute(f"""SELECT word FROM dict
        WHERE counter = {self.minim}
""").fetchall()
        result = [str(x[0]) for x in result]
        self.word.setText(f'{choice(result)}')
        con.commit()
        con.close()

    def check(self):
        try_ = self.option.text()
        con = sqlite3.connect('DataM.sqlite')
        cur = con.cursor()
        result = cur.execute(f"""SELECT translation FROM dict
        WHERE word = '{self.word.text().lower()}'""").fetchall()
        if try_ == str(result[0][0]):
            self.my_status.setText('Да, это верно.')
        else:
            self.my_status.setText('Нет, это неверно')
        con.commit()
        con.close()

    def show_answer(self):
        if self.btn_show_ans.text() == 'Показать ответ:':
            con = sqlite3.connect('DataM.sqlite')
            cur = con.cursor()
            result = cur.execute(f"""SELECT translation FROM dict
                    WHERE word = '{self.word.text().lower()}'""").fetchall()
            self.answer.setText(f'{str(result[0][0])}')
            self.btn_show_ans.setText('Спрятать ответ:')
            con.commit()
            con.close()
        else:
            self.answer.setText('')
            self.btn_show_ans.setText('Показать ответ:')

    def set_main_window(self, main_window):
        self.main_window = main_window


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = AuthorisationWidget()
    ex.show()
    sys.exit(app.exec())