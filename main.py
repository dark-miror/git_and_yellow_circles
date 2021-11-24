import sys
from random import randint

from PyQt5.uic import loadUi
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QWidget, QApplication


class Example(QWidget):
    def __init__(self):
        super().__init__()
        loadUi('UI.ui', self)
        self.initUI()
        self.flag = False

    def initUI(self):
        self.setWindowTitle('Git и желтые окружности')
        self.btn.clicked.connect(self.draw)

    def draw(self):
        self.flag = True
        self.update()

    def paintEvent(self, event):
        if self.flag:
            self.qp = QPainter()
            self.qp.begin(self)
            self.figure()
            self.qp.end()

    def figure(self):
        self.qp.setBrush(QColor(255, 255, 0))
        a = randint(50, self.width() // 5)
        x, y = randint(100 + a, self.width() - a), randint(100 + a, self.height() - a)
        self.qp.drawEllipse(x - a // 2, y - a // 2, a, a)
        self.flag = False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.showMaximized()
    sys.exit(app.exec())
