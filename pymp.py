from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon, QPalette
from PyQt5.QtMultimedia import QMediaPlayer
from PyQt5.QtCore import Qt
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowIcon(QIcon("player.ico"))
        self.setWindowTitle("PYmediaPlayer")
        self.setGeometry(350,100, 700,500)

p = self.palette()