from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout
from PyQt5.QtGui import QIcon, QPalette
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtCore import Qt
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowIcon(QIcon("icon.ico"))
        self.setWindowTitle("PYmediaPlayer")
        self.setGeometry(350,100, 700,500)

        p = self.palette()
        p.setColor(QPalette.Window, Qt.GlobalColor.darkGreen)
        self.setPalette(p)



    def create_player(self):

        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)

        VideoWidget = QVideoWidget()


        self.openBtn = QPushButten('Open Video') # type: ignore

        hbox = QHBoxLayout()
        hbox.setContentsMargins(0,0,0)

        hbox.addWidget(self.openBtn)




        vbox = QVideoWidget()


app = QApplication(sys.argv) # type: ignore
window = Window()
window.show()
sys.exit(app.exec_())