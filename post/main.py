from PyQt5.QtWidgets import QApplication
from post import MyWindow

if __name__ == "__main__":
    app = QApplication([])
    win = MyWindow()
    win.show()
    app.exec_()
