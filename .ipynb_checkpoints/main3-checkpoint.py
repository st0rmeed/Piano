import sys
from PyQt6.QtWidgets import QWidget, QLineEdit, QPushButton, QApplication, QLCDNumber, QLabel


class MorseCode(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(500, 500, 600, 300)
        self.setWindowTitle('Азбука Морзе 2')

        x, y = -40, 0

        self.alphabet_buttons = {
            'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.', 'g': '--.', 'h': '....',
            'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---', 'p': '.--.',
            'q': '--.-', 'r': '.-.', 's': '...', 't': '-', 'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-',
            'y': '-.--', 'z': '--..'
        }

        for k, v in self.alphabet_buttons.items():
            self.buttton = QPushButton(k, self)
            self.buttton.resize(40, 40)
            x += 40
            if x > 560:
                x = 0
                y += 40
            self.buttton.move(x, y)
            self.buttton.clicked.connect(self.morse)

        self.result = QLineEdit('', self)
        self.result.move(20, 100)
        self.result.resize(550, 20)

    def morse(self):
        sender = self.sender().text()
        self.result.insert(self.alphabet_buttons[sender])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MorseCode()
    ex.show()
    sys.exit(app.exec())
