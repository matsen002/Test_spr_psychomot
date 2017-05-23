from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Authors(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        self.setGeometry(250, 250, 300, 300)
        self.setWindowTitle('Authors')
        self.initT()

    def initT(self):

        self.text = ('Autorzy:\n'
                     'Sendrowicz Mateusz\n'
                     'Patryk Milewczyk\n')
        self.show()

# tworzenie tekstu
    def paintEvent(self, event):

        qp = QPainter()
        qp.begin(self)
        self.drawText(event, qp)
        qp.end()

    def drawText(self, event, qp):

        qp.setPen(QColor(0, 0, 0))
        qp.setFont(QFont('Calibri', 12))
        qp.drawText(event.rect(), Qt.AlignCenter, self.text)

class About(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        self.setGeometry(250, 250, 500, 300)
        self.setWindowTitle('About')
        self.initT()

    def initT(self):

        self.text = ('Testy sprawnosci psychomotorycznej.\n'
                     '\n'
                     'Program sluzy do zmierzenia czasu reakcji \n'
                     'na bodzce sluchowe i wzrokowe.\n'
                     'Nalezy wybrac odpowiednie zadanie i postepowac \n'
                     'zgodnie z jego opisem.\n'
                     'Zadanie 1 bada szybkosc reakcji na bodziec wzrokowy.\n'
                     'Zadanie 2 bada szybkosc reakcji na bodziec dzwiekowy.\n\n'
                     'Wyniki podane zostana po wykonaniu wszystkich zadan.')
        self.show()

# tworzenie tekstu
    def paintEvent(self, event):

        qp = QPainter()
        qp.begin(self)
        self.drawText(event, qp)
        qp.end()

    def drawText(self, event, qp):

        qp.setPen(QColor(0, 0, 0))
        qp.setFont(QFont('Decorative', 10))
        qp.drawText(event.rect(), Qt.AlignCenter, self.text)
