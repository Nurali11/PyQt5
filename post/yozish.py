from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton

class Yozish(QWidget):
    def __init__(self, ism):
        super().__init__()
        self.ism = ism
        self.setFixedSize(500, 150)
        self.setWindowTitle('Post Yozish')

        self.txt = QLabel('Postni kiriting: ', self)
        self.txt.move(10, 10)
        self.txt.setStyleSheet('font-size: 20px')

        self.post = QLineEdit(self)
        self.post.move(150, 10)
        self.post.setPlaceholderText('........')
        self.post.setStyleSheet('font-size: 20px')

        self.knopka = QPushButton('Post qilish', self)
        self.knopka.move(350, 100)
        self.knopka.setStyleSheet('background: lightgreen; font-size: 20px')
        self.knopka.clicked.connect(self.filega)

        self.cancel = QPushButton('Cancel', self)
        self.cancel.move(240, 100)
        self.cancel.setStyleSheet('background: lightgrey; font-size: 20px')
        self.cancel.clicked.connect(self.close)

        self.post_error = QLabel('', self)
        self.post_error.setStyleSheet('color: red; font-size: 18px')
        self.post_error.adjustSize()
        self.post_error.move(170, 50)

    def filega(self):
        if len(self.post.text().strip()) == 0:
            self.post_error.setText("Post bo'sh bolmasin!")
            self.post_error.adjustSize()
            return
        else:
            self.post_error.setText("")

        txt = ""
        user_found = False
        with open('post.txt', 'r') as f:
            for line in f.read().splitlines():
                if len(line) > 0:
                    i = line.split(':')
                    if i[0] == self.ism:
                        txt += f"{self.ism}:{i[1]} {self.post.text()},\n"
                        user_found = True
                    else:
                        txt += line + '\n'

        if not user_found:
            txt += f"{self.ism}:{self.post.text()},\n"

        with open('post.txt', 'w') as f:
            f.write(txt)

        self.close()
