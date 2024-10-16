from PyQt5.QtWidgets import QApplication, QWidget, QPushButton

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(250, 150)
        self.setWindowTitle('Main')

        self.login = QPushButton("Login", self)
        self.login.move(10, 20)
        self.login.setStyleSheet('background: grey; font-size: 20px')
        self.login.clicked.connect(self.login_)

        self.kirish = QPushButton('Kirish', self)
        self.kirish.move(140, 20)
        self.kirish.setStyleSheet('background: grey; font-size: 20px')
        self.kirish.clicked.connect(self.kirish_)

        self.chiqish = QPushButton('Chiqish', self)
        self.chiqish.move(75, 100)
        self.chiqish.setStyleSheet('background: grey; font-size: 20px')
        self.chiqish.clicked.connect(self.close)

    def kirish_(self):
        from kirish import Registr
        self.registr = Registr()
        self.registr.show()

    def login_(self):
        from login import Login
        self.login_window = Login()  
        self.login_window.show()
