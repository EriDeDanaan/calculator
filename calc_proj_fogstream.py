from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

import sys

class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        self.setWindowTitle("Кузнецовский калькулятор")
        self.setGeometry(500, 450, 300, 250)

        self.new_text = QtWidgets.QLabel(self)

        self.title = QtWidgets.QLabel(self)
        self.title.setText('Мы начинаем считать')
        self.title.move(100, 100)
        self.title.adjustSize()

        self.button = QtWidgets.QPushButton(self)
        self.button.move(30, 200)
        self.button.setText('Надпись на кнопке')
        self.button.setFixedWidth(200)
        self.button.adjustSize()
        self.button.clicked.connect(self.add_good)


    def add_good(self):
        self.new_text.setText('Какая-то надпись после нажатия кнопки')
        self.new_text.move(30, 50)
        self.new_text.adjustSize()


def application():
    app = QApplication(sys.argv)
    window = Window()

    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    application()
