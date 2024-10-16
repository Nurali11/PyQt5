from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QTextEdit

class Menyu(QWidget):
    def __init__(self, ism):
        super().__init__()
        self.ism = ism
        self.setFixedSize(400, 300)
        self.setWindowTitle('Post Menu')

        self.label = QLabel(f"Welcome, {self.ism}!", self)
        self.label.setStyleSheet('font-size: 24px')
        self.label.move(50, 20)

        self.post_yozish_btn = QPushButton('Post yozish', self)
        self.post_yozish_btn.move(50, 70)
        self.post_yozish_btn.setStyleSheet('background: lightgrey; font-size: 20px')
        self.post_yozish_btn.clicked.connect(self.post_yozish)

        self.postlarimni_korish_btn = QPushButton('Postlarimni ko\'rish', self)
        self.postlarimni_korish_btn.move(50, 120)
        self.postlarimni_korish_btn.setStyleSheet('background: lightgrey; font-size: 20px')
        self.postlarimni_korish_btn.clicked.connect(self.postlarimni_korish)

        self.boshqa_postlarni_korish_btn = QPushButton('Boshqaning postlarini ko\'rish', self)
        self.boshqa_postlarni_korish_btn.move(50, 170)
        self.boshqa_postlarni_korish_btn.setStyleSheet('background: lightgrey; font-size: 20px')
        self.boshqa_postlarni_korish_btn.clicked.connect(self.boshqa_postlarni_korish)

        self.chiqish_btn = QPushButton('Chiqish', self)
        self.chiqish_btn.move(50, 220)
        self.chiqish_btn.setStyleSheet('background: lightgrey; font-size: 20px')
        self.chiqish_btn.clicked.connect(self.close)

    def post_yozish(self):
        from yozish import Yozish
        self.yozish_window = Yozish(self.ism)
        self.yozish_window.show()

    def postlarimni_korish(self):
        self.postlarim_window = PostlarimWindow(self.ism)
        self.postlarim_window.show()

    def boshqa_postlarni_korish(self):
        self.boshqa_postlar_window = BoshqaPostlarWindow(self.ism)
        self.boshqa_postlar_window.show()


class PostlarimWindow(QWidget):
    def __init__(self, ism):
        super().__init__()
        self.ism = ism
        self.setWindowTitle("Postlarimni Ko'rish")
        self.setFixedSize(400, 300)
        
        self.posts_display = QTextEdit(self)
        self.posts_display.setReadOnly(True)
        self.posts_display.move(10,10)
        self.posts_display.setFixedSize(380,280)


        self.load_posts()

    def load_posts(self):
        user_posts = ""
        with open('post.txt', 'r') as f:
            lines = f.read().splitlines() 
            for i in lines:
                if i.startswith(self.ism):
                    postlar = i.split(':')[1]
                    user_posts = postlar.strip()
                    break
        
        if user_posts:
            self.posts_display.setText(f"Yozilgan postlar:\n{user_posts}")
            self.posts_display.setStyleSheet('font-size: 20px')
        else:
            self.posts_display.setText('Hali hechqanday post yozilmagan')
            self.posts_display.setStyleSheet('font-size: 20px')


class BoshqaPostlarWindow(QWidget):
    def __init__(self, ism):
        super().__init__()
        self.ism = ism
        self.setWindowTitle("Boshqa Userlarning Postlari")
        self.setFixedSize(400, 300)

        self.posts_display = QTextEdit(self)
        self.posts_display.setReadOnly(True)
        self.posts_display.move(10,10)
        self.posts_display.setFixedSize(380,280)

        self.load_other_posts()

    def load_other_posts(self):
        other_posts = ""
        tekshiruv = False

        with open('post.txt', 'r') as f:
            lines = f.read().splitlines()
            for i in lines:
                if not i.startswith(self.ism) and len(i) > 0:
                    other_posts += f"{i}\n"
                    tekshiruv = True

        if tekshiruv:
            self.posts_display.setText(other_posts.strip())
            self.posts_display.setStyleSheet('font-size: 20px')
        else:
            self.posts_display.setText('Hali hech kim post yozmagan!')
            self.posts_display.setStyleSheet('font-size: 20px')


if __name__ == "__main__":
    app = QApplication([])
    win = Menyu("Test User")
    win.show()
    app.exec_()
