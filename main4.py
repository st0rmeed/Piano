import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget
from PyQt6.QtCore import Qt, QUrl
from PyQt6.QtMultimedia import QSoundEffect

# создание нот, путей к папке со звуковыми файлами, а так же сопоставление нот с соответствующими клавишами
notes = {
    'A': {'key': Qt.Key.Key_A, 'sound': './sounds/1.wav'},
    'S': {'key': Qt.Key.Key_S, 'sound': './sounds/2.wav'},
    'D': {'key': Qt.Key.Key_D, 'sound': './sounds/3.wav'},
    'F': {'key': Qt.Key.Key_F, 'sound': './sounds/4.wav'},
    'G': {'key': Qt.Key.Key_G, 'sound': './sounds/5.wav'},
}


class Piano(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Piano')
        self.setGeometry(100, 100, 800, 200)

        # политика фокуса для получения событий клавиатуры
        self.setFocusPolicy(Qt.FocusPolicy.StrongFocus)

        layout = QVBoxLayout()

        # добавление каждой кнопки в лейаут, а так же подключение сигналов нажатия на кнопку
        # создание словаря, в котором для каждой ноты хранится соотв кнопка
        self.buttons = {}
        for note, data in notes.items():
            button = QPushButton(note)
            button.clicked.connect(lambda _, n=note: self.play_note(n))
            layout.addWidget(button)
            self.buttons[note] = button

        # установка лейаута
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        # словарь, сопоставляющий коды клавиш с нотами
        self.key_mapping = {data['key']: note for note, data in notes.items()}

    # метод, воспроизводящий звук для данной ноты
    def play_note(self, note):
        # путь к звуковому файлу
        sound_file = notes[note]['sound']
        # воспроизведение звука
        sound_effect = QSoundEffect(self)
        sound_effect.setSource(QUrl.fromLocalFile(sound_file))
        sound_effect.play()

    # метод, обрабатывающий нажатие клавиши
    def keyPressEvent(self, event):
        # получение кнопки, на которую нажали
        key = event.key()
        # если кнопка находится в данных нотах, то воспроизводится звук
        if key in self.key_mapping:
            note = self.key_mapping[key]
            self.play_note(note)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Piano()
    window.show()
    sys.exit(app.exec())
