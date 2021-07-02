#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Пользователь
#
# Created:     28.06.2021
# Copyright:   (c) Пользователь 2021
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import sys
from random import choice, randrange
from PySide6 import QtGui
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QPushButton, QMessageBox

class MainWin(QPushButton):
    def __init__(self):
        super().__init__()

        self.setMouseTracking(True)
        self.setWindowFlags(Qt.Window | Qt.FramelessWindowHint);
        self.setText('> Push me <')

        self.clicked.connect(self.mouse_clicked)

        self.ss = 0
        self.ss_x = 0
        self.ss_y = 0

        self.ss = QtGui.QGuiApplication.primaryScreen().geometry();
        self.ss_x = self.ss.right()
        self.ss_y = self.ss.bottom()
##        print(f'ss -> {ss}, x -> {ss_x}, y -> {ss_y}')

    def mouse_clicked(self):
##        print(f'mouse clicked')
        mbox = QMessageBox()
        mbox.setText(f"fock u!")
        mbox.exec()
        sys.exit()
        pass

    def mouseMoveEvent(self, e):
        print(f'mouse move Eve')
        new_x = randrange(100, self.ss_x, 10)
        new_y = randrange(100, self.ss_y-50, 10)
##        print(f'new_x -> {new_x} new_y -> {new_y}')
        self.move(new_x, new_y)
        pass


def run():
    app = QApplication(sys.argv)
    win = MainWin()
    win.show()
    app.exec_()

if __name__ == '__main__':
    run()
