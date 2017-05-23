import numpy as np
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
import time
import winsound
import menu
import matplotlib.pyplot as plt

Freq = 1000 # Set Fr# equency To 2500 Hertz
Dur = 250 # Set Duration To 1000 ms == 1 second

class PsychoTesty(QMainWindow):

    def __init__(self):
        super(PsychoTesty, self).__init__()

        self.left = 200
        self.top = 200
        self.height = 400
        self.width = 600

        self.start()
        self.initUi()

        self.liczba_podejsc_probnych = 1
        self.liczba_wlasciwych_pomiarow = 3

    def initUi(self):
        # Nowa sesja
        startAction = QAction(QIcon('exit.png'), '&Start', self)
        startAction.triggered.connect(self.start)
        # Exit
        exitAction = QAction(QIcon('exit.png'), '&Exit', self)
        exitAction.setStatusTip('Exit application')  # zamykanie
        exitAction.triggered.connect(self.zamknij)
        # About
        helpAction = QAction(QIcon('exit.png'), '&About', self)
        helpAction.triggered.connect(self.about)  # wywolanie kolejnego okna
        # Authors
        authorsAction = QAction(QIcon('exit.png'), '&Authors', self)
        authorsAction.triggered.connect(self.authors)
        self.ab = None
        self.au = None
        self.statusBar()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')  # umieszczenie w menu "File"
        fileMenu.addAction(startAction)
        fileMenu.addAction(exitAction)
        fileMenu2 = menubar.addMenu('&Help')
        fileMenu2.addAction(helpAction)  # umiezczenie w menu "About"
        fileMenu2.addAction(authorsAction)  # umiezczenie w menu "Authors"

        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setWindowTitle('Testy sprawnosci psychomotorycznej')

        btn1 = QPushButton('Zadanie 1', self)
        btn1.clicked.connect(self.zad1_wywolanie)
        btn1.move( 50, 50)

        btn2 = QPushButton('Zadanie 2', self)
        btn2.clicked.connect(self.zad2_wywolanie)
        btn2.move(200, 50)

        self.show()

    def about(self):
        self.ab = menu.About()
        self.ab.show()

    def authors(self):
        self.au = menu.Authors()
        self.au.show()

    def zamknij(self):
        sys.exit()

    def start(self):
        self.x = 0
        self.y = 0

        self.zad1_wynik = []
        self.zad2_wynik = []
        self.wybrano = 0

        self.timerGlowny()

        self.zad1_nr_podejscia = 0
        self.zad2_nr_podejscia = 0

        self.zad1_koniec = False
        self.zad2_koniec = False

        self.repaint()
        
    def timerGlowny(self):
        self.timer = QBasicTimer()
        self.timer_zad1 = QBasicTimer()
        self.timer_zad2 = QBasicTimer()
        self.timer.start(100, self)
        
    def zad1_wywolanie(self):
        if not self.zad1_koniec:
            self.wybrano = 11
        self.repaint()

    def zad2_wywolanie(self):
        if not self.zad2_koniec:
            self.wybrano = 21
        self.repaint()

    def zad1_zacznij(self):
        rand = 1000 + 3000 * np.random.rand()
        self.timer_zad1.start(rand, self)
        
    def zad2_zacznij(self):
        rand = 1000 + 3000 * np.random.rand()
        self.timer_zad2.start(rand, self)

    def rysuj(self, paint, i):

        paint.setRenderHint(QPainter.Antialiasing)

        paint.setPen(Qt.black)
        paint.setFont(QFont('Arial', 10))

        if i == 0:

            paint.setBrush(Qt.white)
            paint.drawRect(self.x, self.y, self.width, self.height - self.y)

            paint.drawText(self.x + 100, self.y + 150, 'Gdy bedziesz gotow, wybierz zadanie')
            paint.drawText(self.x + 100, self.y + 170, 'Zadanie 1 bada szybkosc reakcji na bodziec wzrokowy')
            paint.drawText(self.x + 100, self.y + 190, 'Zadanie 2 bada szybkosc reakcji na bodziec dzwiekowy')

        if i == 11 or i == 12:

            paint.setBrush(Qt.white)
            paint.drawRect(self.x, self.y, self.width, self.height - self.y)

            paint.drawText(self.x + 100, self.y + 150, 'Zadanie pierwsze polega na wcisnieciu')
            paint.drawText(self.x + 100, self.y + 170, 'klawisza "s" po zobaczeniu czerwonego prostokata')
            paint.drawText(self.x + 100, self.y + 190, 'Pierwsze ' + str(self.liczba_podejsc_probnych) + ' podejscia nie licza sie do wyniku')
            paint.drawText(self.x + 100, self.y + 210, 'Kolejne ' + str(self.liczba_wlasciwych_pomiarow) + ' licza sie do wyniku')

            paint.drawText(self.x + 100, self.y + 250, 'Gdy bedziesz gotowy, wcisnij "s" aby rozpoczac')

        if i == 12:

            paint.setBrush(Qt.red)
            paint.setPen(Qt.darkRed)
            paint.drawRect(20, 150, 20, 20)

        if i == 13:

            paint.setBrush(Qt.white)
            paint.drawRect(self.x, self.y, self.width, self.height - self.y)

            paint.drawText(self.x + 100, self.y + 150, 'Zadanie pierwsze polega na wcisnieciu')
            paint.drawText(self.x + 100, self.y + 170, 'klawisza "s" po zobaczeniu czerwonego prostokata')

            if self.zad1_nr_podejscia <= self.liczba_podejsc_probnych:
                paint.drawText(self.x + 100, self.y + 210, 'Proba nr ' + str(self.zad1_nr_podejscia))
            else:
                paint.drawText(self.x + 100, self.y + 210, 'Pomiar nr ' + str(self.zad1_nr_podejscia - self.liczba_podejsc_probnych))

            paint.drawText(self.x + 100, self.y + 310, 'Aby kontynuowac, wybierz odpowiednie zadanie')
        
        if i == 21:
            
            paint.setBrush(Qt.white)
            paint.drawRect(self.x, self.y, self.width, self.height - self.y)

            paint.drawText(self.x + 100, self.y + 150, 'Zadanie drugie polega na wcisnieciu')
            paint.drawText(self.x + 100, self.y + 170, 'klawisza "s" po uslyszeniu sygnalu dzwiekowego')
            paint.drawText(self.x + 100, self.y + 190, 'Pierwsze ' + str(self.liczba_podejsc_probnych) + ' podejscia nie licza sie do wyniku')
            paint.drawText(self.x + 100, self.y + 210, 'Kolejne ' + str(self.liczba_wlasciwych_pomiarow) + ' licza sie do wyniku')

            paint.drawText(self.x + 100, self.y + 250, 'Gdy bedziesz gotowy, wcisnij "s" aby rozpoczac')

        if i == 23:
            
            paint.setBrush(Qt.white)
            paint.drawRect(self.x, self.y, self.width, self.height - self.y)

            paint.drawText(self.x + 100, self.y + 150, 'Zadanie drugie polega na wcisnieciu')
            paint.drawText(self.x + 100, self.y + 170, 'klawisza "s" po uslyszeniu sygnalu dzwiekowego')

            if self.zad2_nr_podejscia <= self.liczba_podejsc_probnych:
                paint.drawText(self.x + 100, self.y + 210, 'Proba nr ' + str(self.zad2_nr_podejscia))
            else:
                paint.drawText(self.x + 100, self.y + 210, 'Pomiar nr ' + str(self.zad2_nr_podejscia - self.liczba_podejsc_probnych))

            paint.drawText(self.x + 100, self.y + 310, 'Aby kontynuowac, wybierz odpowiednie zadanie')

        if i == 99:

            paint.setBrush(Qt.white)
            paint.drawRect(self.x, self.y, self.width, self.height - self.y)

            paint.drawText(self.x + 100, self.y + 150, 'Wykonano wszystkie mozliwe podejscia dla tego zadania')
            paint.drawText(self.x + 100, self.y + 170, 'Wykonaj pozostale, aby zobaczyc wyniki')

        if self.zad1_koniec and self.zad2_koniec:

            paint.setBrush(Qt.white)
            paint.drawRect(self.x, self.y, self.width, self.height - self.y)

            sredni_czas_zad1 = 0
            sredni_czas_zad2 = 0

            paint.drawText(self.x + 50, self.y + 150, 'Zestawienie wynikow:\n')

            paint.drawText(self.x + 50, self.y + 170, 'Zadanie 1:')
            for j in range(len(self.zad1_wynik)+1):
                if j != len(self.zad1_wynik):
                    paint.drawText(self.x + 50, self.y + 190 + 20 * j, str('{liczba:.4f}'.format(liczba = self.zad1_wynik[j])))
                    sredni_czas_zad1 += self.zad1_wynik[j]
                else:
                    paint.drawText(self.x + 50, self.y + 190 + 20 * (j+1), 'Srednia:')
                    paint.drawText(self.x + 50, self.y + 190 + 20 * (j+2), str('{liczba:.4f}'.format(liczba = sredni_czas_zad1/j)))

            ile = self.zad1_nr_podejscia - self.liczba_podejsc_probnych
            t = np.linspace(0, ile, ile)
            plt.plot(t,self.zad1_wynik, 'x')

            paint.drawText(self.x + 200, self.y + 170, 'Zadanie 2:')
            for j in range(len(self.zad2_wynik)+1):
                if j != len(self.zad2_wynik):
                    paint.drawText(self.x + 200, self.y + 190 + 20 * j, str('{liczba:.4f}'.format(liczba = self.zad2_wynik[j])))
                    sredni_czas_zad2 += self.zad2_wynik[j]
                else:
                    paint.drawText(self.x + 200, self.y + 190 + 20 * (j+1), 'Srednia:')
                    paint.drawText(self.x + 200, self.y + 190 + 20 * (j+2), str('{liczba:.4f}'.format(liczba = sredni_czas_zad2/j)))

            ile = self.zad2_nr_podejscia - self.liczba_podejsc_probnych
            t = np.linspace(0, ile, ile)
            plt.plot(t, self.zad2_wynik, 'o')
            plt.show()

    def paintEvent(self, event):

        paint = QPainter()
        paint.begin(self)
        self.rysuj(paint, self.wybrano)
        paint.end()

    def keyPressEvent(self, event):

        key = event.key()

        if key == Qt.Key_S:
            if self.wybrano == 11:
                self.zad1_zacznij()
            elif self.wybrano == 12:
                self.stop = time.clock()
                if self.zad1_nr_podejscia >= self.liczba_podejsc_probnych:
                    self.zad1_wynik.append(self.stop - self.start)
                self.zad1_nr_podejscia += 1
                self.wybrano = 13
                self.repaint()
                if self.zad1_nr_podejscia >= self.liczba_podejsc_probnych + self.liczba_wlasciwych_pomiarow:
                    self.zad1_koniec = True
                    self.wybrano = 99
                self.timer_zad1 = QBasicTimer()
            elif self.wybrano == 21:
                self.zad2_zacznij()
            elif self.wybrano == 22:
                self.stop = time.clock()
                self.wybrano = 23
                if self.zad2_nr_podejscia >= self.liczba_podejsc_probnych:
                    self.zad2_wynik.append(self.stop - self.start)
                self.zad2_nr_podejscia += 1
                self.repaint()
                if self.zad2_nr_podejscia >= self.liczba_podejsc_probnych + self.liczba_wlasciwych_pomiarow:
                    self.zad2_koniec = True
                    self.wybrano = 99
                self.timer_zad2 = QBasicTimer()

        elif key == Qt.Key_Escape:
            sys.exit()

        else:
            super(PsychoTesty, self).keyPressEvent(event)

    def timerEvent(self, event):

        if event.timerId() == self.timer_zad1.timerId() and self.wybrano == 11:
            self.wybrano = 12
            self.repaint()
            self.start = time.clock()

        if event.timerId() == self.timer_zad2.timerId() and self.wybrano == 21:
            self.wybrano = 22
            self.start = time.clock()
            winsound.Beep(Freq, Dur)

def main():
    app = QApplication(sys.argv)
    testy = PsychoTesty()
    sys.exit(app.exec_())

#if __name__ == '__main__':
main()