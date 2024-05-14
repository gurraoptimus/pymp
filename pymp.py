from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon, QPalette
from PyQt5.QtMultimedia import QMediaPlayer, QtMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtCore import Qt
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowIcon(QIcon("player.ico"))
        self.setWindowTitle("PYmediaPlayer")
        self.setGeometry(350,100, 700,500)

p = self.palette()
p.setColor(QPalette.Window, Qt.GlobalColor.red)
self.setPalette(p)



def create_player(self):


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec_())
